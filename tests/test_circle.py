# test_circle.py
import pytest
from Sourcecode.circle import calculate_area

def test_calculate_area():
    # Test normal case
    assert calculate_area(1) == pytest.approx(3.141592653589793, rel=1e-9)
    assert calculate_area(2) == pytest.approx(12.566370614359172, rel=1e-9)
    assert calculate_area(0) == 0  # Area of circle with radius 0 should be 0

    # Test edge case with negative radius (should raise ValueError)
    with pytest.raises(ValueError):
        calculate_area(-1)

