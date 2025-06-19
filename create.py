import os

OPERATORS = [
    {
        "name": "ymonmean",
        "num_inputs": 1,
        "num_outputs": 1,
        "parameters": {}
    },
    {
        "name": "sub",
        "num_inputs": 2,
        "num_outputs": 1,
        "parameters": {}
    },
    {
        "name": "mergetime",
        "num_inputs": float("inf"),
        "num_outputs": 1,
        "parameters": {}
    },
    {
        "name": "remapbil",
        "num_inputs": 1,
        "num_outputs": 1,
        "parameters": {
            "grid": "grid to remap to"
            }
    },
    {
        "name": "setllonlatbox",
        "num_inputs": 1,
        "num_outputs": 1,
        "parameters": {
            "lon1": "left longitude",
            "lon2": "right longitude",
            "lat1": "lower latitude",
            "lat2": "upper latitude"
        }
    }
]

def make_arguments(op):
    params = list(op["parameters"].keys())
    extra_files = []
    if op["num_inputs"] != float("inf"):
        extra_files = [f"ifile{i}" for i in range(2, int(op["num_inputs"]) + 1)]
    return extra_files, params

def make_docstring(op):
    if not op["parameters"]:
        return f"CDO operator: {op['name']}"
    lines = [f"CDO operator: {op['name']}", "Parameters:"]
    for k, v in op["parameters"].items():
        lines.append(f"    {k}: {v}")
    return "\n".join(lines)

TEMPLATE = '''
from cdo_operator import CdoOperator
inf=float("inf")
def {name}({signature}):
    """
    {docstring}
    """
    operator = CdoOperator(name="{name}",
                           num_inputs={num_inputs}, 
                           num_outputs={num_outputs}, 
                           parameters={parameters_list})
    return self._new_op(operator, {files_list}, {parameters_dic})
'''

out_dir="pycdo/operators"

for op in OPERATORS:
    extra_files, parameters = make_arguments(op)
    parameters_list = "[" + ", ".join(parameters) + "]"
    parameters_dic = "{" + ", ".join([f'"{par}": {par}' for par in parameters]) + "}"
    files_list = "[" + ", ".join(extra_files) + "]"
    name = op["name"]
    code = TEMPLATE.format(
        name = op["name"],
        docstring = make_docstring(op),
        num_inputs = op["num_inputs"],
        num_outputs = op["num_outputs"],
        parameters_list = parameters_list,
        parameters_dic = parameters_dic,
        files_list = files_list,
        signature = "self, " + ", ".join(extra_files + parameters)
    )
    
    with open(os.path.join(out_dir, f"{name}.py"), "w") as f: 
        f.write(code)