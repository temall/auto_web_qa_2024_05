from src.square import Square
import pytest


@pytest.mark.parametrize("side_a",
                         [-3, 0, False],
                         ids=["negative value", "zero value", 'logical']
                         )
def test_square_negative_and_zero_value(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


def test_square_get_area():
    s = Square(3)
    assert s.get_area == 9


def test_square_get_perimeter():
    s = Square(3)
    assert s.get_perimetr == 12
