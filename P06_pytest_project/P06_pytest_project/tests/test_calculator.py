import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected


    def test_subtract(self):
        # Arrange
        a = 4321
        b = 1234
        cal = Calculator()
        
        # Act
        result = cal.subtract(a, b)
        
        # Assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # Arrange
        a = 20
        b = 5
        cal = Calculator()
        
        # Act
        result = cal.multiply(a, b)
        
        # Assert
        expected = 100
        assert result == expected

    def test_divide(self):
        # Arrange
        a = 20
        b = 4
        cal = Calculator()
        
        # Act
        result = cal.divide(a, b)
        
        # Assert
        expected = 5.0
        assert result == expected

    