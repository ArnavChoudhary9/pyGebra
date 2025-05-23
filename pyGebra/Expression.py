from enum import Enum
from typing import List

class ExpressionType(Enum):
    """Enum for different types of expressions."""
    NUMBER = 1
    VARIABLE = 2
    OPERATOR = 3
    
class Expression:
    """Class representing a mathematical expression."""
    
    Type: ExpressionType
    
    Value: int | float | str | None
    Operator: str | None
    Left: 'Expression | None'
    Right: 'Expression | None'

    def __init__(self, data, left: 'Expression | None' = None, right: 'Expression | None' = None):
        """Initialize the expression with a value."""
        
        if isinstance(data, (int, float)):
            self.Type = ExpressionType.NUMBER
            self.Value = data
            
        elif isinstance(data, str):
            if data in ['+', '-', '*', '/']:
                self.Type = ExpressionType.OPERATOR
                self.Operator = data
                self.Left = left
                self.Right = right
                if left is None or right is None:
                    raise ValueError("Left and right operands must be provided for an operator.")

            else:
                self.Type = ExpressionType.VARIABLE
                self.Value = data          
        else:
            raise ValueError("Invalid data type for expression.")
        
    def __str__(self):
        """Return a string representation of the expression."""
        
        if self.Type == ExpressionType.NUMBER:
            return str(self.Value)
        
        elif self.Type == ExpressionType.VARIABLE:
            return str(self.Value)
        
        elif self.Type == ExpressionType.OPERATOR:
            if self.Left is None or self.Right is None:
                raise ValueError("Left and right operands must be provided for an operator.")
            return f"({self.Left} {self.Operator} {self.Right})"

        else:
            raise ValueError("Invalid expression type.")
