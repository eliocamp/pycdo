import os

OPERATORS = [
    {
        "command": "ymonmean",
        "n_input": 1,
        "n_output": 1,
        "params": {}
    },
    {
        "command": "sub",
        "n_input": 2,
        "n_output": 1,
        "params": {}
    },
    {
        "command": "mergetime",
        "n_input": float("inf"),
        "n_output": 1,
        "params": {}
    },
    {
        "command": "remapbil",
        "n_input": 1,
        "n_output": 1,
        "params": {
            "grid": "grid to remap to"
            }
    },
    {
        "command": "sellonlatbox",
        "n_input": 1,
        "n_output": 1,
        "params": {
            "lon1": "left longitude",
            "lon2": "right longitude",
            "lat1": "lower latitude",
            "lat2": "upper latitude"
        }
    }
]

def make_arguments(op):
    params = list(op["params"].keys())
    extra_files = []
    if op["n_input"] != float("inf"):
        extra_files = [f"ifile{i}" for i in range(2, int(op["n_input"]) + 1)]
    return extra_files, params

def make_docstring(op):
    if not op["params"]:
        return f"CDO operator: {op['command']}"
    lines = [f"CDO operator: {op['command']}", "Parameters:"]
    for k, v in op["params"].items():
        lines.append(f"    {k}: {v}")
    return "\n".join(lines)

TEMPLATE = '''
from ..cdo_operator import CdoOperator
inf=float("inf")
def {command}({signature}):
    """
    {docstring}
    """
    operator = CdoOperator(command="{command}",
                           n_input={n_input}, 
                           n_output={n_output}, 
                           params={params_list})
    return self._new_op(operator, {files_list}, {params_dic})
'''

out_dir="pycdo/operators"
all = []

for op in OPERATORS:
    extra_files, params = make_arguments(op)
    params_dic = "{" + ", ".join([f'"{par}": {par}' for par in params]) + "}"
    files_list = "[" + ", ".join(extra_files) + "]"
    command = op["command"]

    all.append(f"from .{command} import {command}")

    code = TEMPLATE.format(
        command = op["command"],
        docstring = make_docstring(op),
        n_input = op["n_input"],
        n_output = op["n_output"],
        params_list = str(params),
        params_dic = params_dic,
        files_list = files_list,
        signature = "self, " + ", ".join(extra_files + params)
    )
    
    with open(os.path.join(out_dir, f"{command}.py"), "w") as f: 
        f.write(code)


    
with open(os.path.join(out_dir, "__init__.py"), "w") as f: 
    f.write("\n".join(all))
