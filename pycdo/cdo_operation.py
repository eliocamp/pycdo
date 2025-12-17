import os
import importlib
from .cdo_options import cdo_options, combine_options
from .cdo_operator import CdoOperator
from inspect import getmembers, isfunction

import tempfile
import subprocess

inf=float("inf")

def cdo(input) -> "CdoOperation":
    return CdoOperation.noop(ifile=input)

class CdoOperation:
    @staticmethod
    def noop(ifile):
        if (isinstance(ifile, list)):
            n_input = len(ifile)
            input = ifile
        else:
            n_input = 1
            input = [ifile]

        noop_operator = CdoOperator(command = "", n_input = n_input, n_output = n_input, params = [])
        return CdoOperation(input = input, operator = noop_operator, params = {})
    
    def __init__(self, input, operator: "CdoOperator", params: dict = {}):
        self.operator = operator
        self.params = params
        self.input = input
        
    @staticmethod
    def _get_n_output(input): 
        if input is None: 
            return 0
        if isinstance(input, CdoOperation): 
            return input.operator.n_output

        if isinstance(input, str): 
            return 1       

        if isinstance(input, list): 
            return float("inf")

    def _new_op(self, operator, inputs, params=None):
        prev_output = self.operator.n_output + len(inputs)
        
        this_input = operator.n_input

        zero_input = this_input == 0 
        unequal_values = this_input != prev_output and this_input != float("inf") 

        operation_incompatible = zero_input or unequal_values

        if operation_incompatible: 
            raise ValueError(f"Chaining error: {operator.command} expects {this_input} but {self.operator.command} outputs {prev_output} files.")

        inputs = [self] + inputs
        return CdoOperation(inputs, operator, params)

    def build(self, top_level=True, options=None, options_replace=False):
        """
        Build the CDO command as a string.
        If an input is a CdoOperation, recursively build its command (without 'cdo') and wrap in parentheses.
        Only the top-level operation should be prefixed with 'cdo'.
        """

        cmd = []
        if top_level:
            cmd.append("cdo")
            options = combine_options(cdo_options.get(), options, replace=options_replace)
            options_str = " ".join(options)
            cmd.append(options_str)

        # Operator command and params
        op_str = f"-{self.operator.command}"
        if self.params:
            param_values = [str(self.params[parameter]) for parameter in self.operator.params]
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

## <<start operators>>
    @staticmethod
    def sellonlatbox(lon1, lon2):
        operator = CdoOperator(command="sellonlatbox",
                        n_input=1, 
                        n_output=1, 
                        params=["lon1", "lon2"])
        return CdoOperation(input = [], operator = operator, params = {"lon1": lon1, "lon2": lon2})


