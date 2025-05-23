from pyGebra import *

def test_expression_number():
    e = Expression(5)
    assert e.Type == ExpressionType.NUMBER
    assert e.Value == 5

def test_expression_variable():
    e = Expression("x")
    assert e.Type == ExpressionType.VARIABLE
    assert e.Value == "x"
    
def test_expression_operation():
    e1 = Expression('x')
    e2 = Expression(3)
    e3 = Expression("+", e1, e2)
    assert e3.Type == ExpressionType.OPERATOR
    assert e3.Operator == "+"
    assert e3.Left == e1
    assert e3.Right == e2
