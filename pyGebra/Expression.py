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
    Operands: List['Expression'] | None

    def __init__(self, data, operands: List['Expression'] | None = None):
        """Initialize the expression with a value."""
        
        if isinstance(data, (int, float)):
            self.Type = ExpressionType.NUMBER
            self.Value = data
            
        elif isinstance(data, str):
            if data in ['+', '-', '*', '/']:
                self.Type = ExpressionType.OPERATOR
                self.Operator = data
                self.Operands = operands
                if operands is None:
                    raise ValueError("Operands must be provided for an operator.")
                
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
            if self.Operands is None:
                raise ValueError("Operands must be provided for an operator.")
            return f"({self.Operands[0]} {self.Operator} {self.Operands[1]})"
        
        else:
            raise ValueError("Invalid expression type.")
