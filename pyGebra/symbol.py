class Symbol:
    """
    A class representing a symbol in the context of a mathematical expression.
    """

    def __init__(self, name: str):
        """
        Initialize the Symbol with a name.

        :param name: The name of the symbol.
        """
        self.name = name

    def __repr__(self):
        return f"Symbol({self.name})"

    def __str__(self):
        return self.name
