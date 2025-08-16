import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from calculator import Calculator

def test_calculator():
    calc = Calculator()
    
    # Test addition
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    print("+ Addition tests passed")
    
    # Test subtraction
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    print("+ Subtraction tests passed")
    
    # Test multiplication
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6
    print("+ Multiplication tests passed")
    
    # Test division
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5
    print("+ Division tests passed")
    
    # Test division by zero
    try:
        calc.divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
        print("+ Division by zero handling passed")
    
    # Test power
    assert calc.power(2, 3) == 8
    assert calc.power(5, 2) == 25
    print("+ Power tests passed")
    
    print("\nAll calculator tests passed!")

if __name__ == "__main__":
    test_calculator()