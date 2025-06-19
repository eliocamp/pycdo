class CdoOperator:
    def __init__(self, name, num_inputs=1, num_outputs=1, parameters=None):
        """
        Represents a CDO operator.

        :param name: Name of the CDO operator (e.g., 'add', 'sub', 'timmean')
        :param num_inputs: Number of input files required
        :param num_outputs: Number of output files produced
        :param parameters: List of parameter names this operator accepts
        """
        self.name = name
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.parameters = parameters or []

    def __repr__(self):
        return (f"CdoOperator(name='{self.name}', "
                f"num_inputs={self.num_inputs}, "
                f"num_outputs={self.num_outputs}, "
                f"parameters={self.parameters})")

