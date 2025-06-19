import os
import importlib
from .cdo_options import cdo_options
from .cdo_operator import CdoOperator

import tempfile
import subprocess

def cdo(input):
    return CdoOperation(input=input)

class CdoOperation:
    def __init__(self, input=None, operator = None, parameters = None):        
        if operator is None: 
            operator = CdoOperator(name="noop", num_inputs=0, num_outputs=self._get_num_outputs(input), parameters=[])
    
        self.operator = operator
        if input is None:
            self.input = []
        elif isinstance(input, list):
            self.input = input
        else:
            self.input = [input]

        self.parameters = parameters or {}
        
    @staticmethod
    def _get_num_outputs(input): 
        if input is None: 
            return 0
        if isinstance(input, CdoOperation): 
            return input.operator.num_outputs

        if isinstance(input, str): 
            return 1       

        if isinstance(input, list): 
            return float("inf")

    def _new_op(self, operator, inputs, parameters=None):
        
        prev_output = self.operator.num_outputs + len(inputs)
        
        this_input = operator.num_inputs

        zero_input = this_input == 0 
        unequal_values = this_input != prev_output and this_input != float("inf") 

        operation_incompatible = zero_input or unequal_values

        if operation_incompatible: 
            raise ValueError(f"Chaining error: {operator.name} expects {this_input} but {self.operator.name} outputs {prev_output} files.")

        inputs = [self] + inputs
        return CdoOperation(inputs, operator, parameters)

    def build(self, top_level=True, options=None, options_replace=False):
        """
        Build the CDO command as a string.
        If an input is a CdoOperation, recursively build its command (without 'cdo') and wrap in parentheses.
        Only the top-level operation should be prefixed with 'cdo'.
        """

        if self.operator.name == "noop":
            # Just return the input file(s)
            return " ".join(self.input)

        cmd = []
        if top_level:
            cmd.append("cdo")
            options = _combine_options(cdo_options.get(), options, replace=options_replace)
            options_str = " ".join(options)
            cmd.append(options_str)

        # Operator name and parameters
        op_str = f"-{self.operator.name}"
        if self.parameters:
            param_values = [str(self.parameters[parameter]) for parameter in self.operator.parameters]
            op_str += "," + ",".join(param_values)
        cmd.append(op_str)

        # Build input strings
        input_strs = []
        for inp in self.input:
            if isinstance(inp, CdoOperation):
                # Recursively build without 'cdo' and wrap in parentheses
                input_strs.append(f"{inp.build(top_level=False)}")
            else:
                input_strs.append(str(inp))
        cmd.extend(input_strs)

        return " ".join(cmd)

    def execute(self, output_file=None, options=None):
        """
        Build the CDO command, append the output file, and execute it as a system call.
        If output_file is not provided, use a random temporary file.

        :param output_file: Path to the output file (optional).
        :return: (returncode, output_file)
        """
        if output_file is None:
            fd, output_file = tempfile.mkstemp()
            os.close(fd)  # Close the file descriptor, CDO will write to the path

        cmd = f"{self.build(options = options)} {output_file}"
        result = subprocess.run(cmd, shell=True)
        return result.returncode, output_file

    def __repr__(self):
        return("CDO operation.\n"+ self.build() + " {output}")


# operators_dir = os.path.join(os.path.dirname(__file__), "operators")
# for fname in os.listdir(operators_dir):
#     print()
#     if fname.endswith(".py") and not fname.startswith("__"):
#         modname = f"operators.{fname[:-3]}"
#         print(modname)
# mod = importlib.import_module("pycdo.operators")
# for attr in dir(OPERATORS):
#     func = getattr(mod, attr)
#     if callable(func):
#         setattr(CdoOperation, attr, func)


def _combine_options(global_options=None, user_options=None, replace=False):
    """
    Combine or replace global and user options.
    - If replace=True: use user_options only.
    - If replace=False: combine global_options and user_options.
    """

    def to_list(opts):
        if opts is None or opts == "":
            return []
        if isinstance(opts, list):
            return opts
        if isinstance(opts, str):
            return [opts]
        raise TypeError("Options must be a string or a list of strings.")

    if replace:
        return to_list(user_options)

    if user_options is None:
        return to_list(global_options)
    
    # Combine both (as list or string)
    return to_list(global_options) + to_list(user_options)