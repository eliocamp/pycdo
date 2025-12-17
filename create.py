import os
import json


# n_input or n_output can be "Inf", parse it correctly
def inf_hook(obj):
    for k, v in obj.items():
        if isinstance(v, str) and v.lower() == "inf":
            obj[k] = float("inf")
    return obj

with open('operators.json', 'r') as file:
    OPERATORS = json.load(file, object_hook=inf_hook)

OPERATORS = list(OPERATORS.values())


def make_arguments(op):
    # For now arguments are all "optional". 
    if not op["params"]:
        params = []
    else:
        params = list(op["params"]["optional"].keys())

    extra_files = []
    if op["n_input"] != float("inf"):
        extra_files = [f"ifile{i}" for i in range(2, int(op["n_input"]) + 1)]
    return extra_files, params

def make_docstring(op):
    if not op["params"]:
        return f"CDO operator: {op['command']}"
    lines = [f"CDO operator: {op['command']}", "Parameters:"]
    for k, v in op["params"]["optional"].items():
        lines.append(f"    {k}: {v}")
    return "\n".join(lines)



TEMPLATE='''
    def {fun_name}({signature}):
        r"""
        {docstring}
        """
        operator = CdoOperator(command="{command}",
                               n_input={n_input}, 
                               n_output={n_output}, 
                               params={params_list})
                               
        return self._new_op(operator, {files_list}, {params_dic})
'''

all_ops = []

for op in OPERATORS:
    fun_name = op["command"]

    # "not" is reserved word so we can't use it as a function name :(
    if (op["command"] == "not"):
        fun_name = "negate"
        
    print(op["command"])
    extra_files, params = make_arguments(op)
    params_dic = "{" + ", ".join([f'"{par}": {par}' for par in params]) + "}"
    files_list = "[" + ", ".join(extra_files) + "]"
    command = op["command"]

    # Make all arguments optional
    params_default = [param + " = None" for param in params]
    code = TEMPLATE.format(
        fun_name = fun_name,
        command = op["command"],
        docstring = make_docstring(op),
        n_input = op["n_input"],
        n_output = op["n_output"],
        params_list = str(params),
        params_dic = params_dic,
        files_list = files_list,
        signature = ", ".join(["self"] + extra_files + params_default)
    )
    
    all_ops.append(code)



operation_file = "pycdo/cdo_operation.py"
marker = "## <<start operators>>"

with open(operation_file, "r") as f:
    lines = []
    for line in f:
        lines.append(line)
        if "## <<start operators>>" in line:
            break



code = "".join(lines) + "".join(all_ops)


with open(operation_file, "w") as f: 
    f.write(code)


