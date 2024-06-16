from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize("side_a, side_b",
                         [
                             (-2, 2),
                             (2, 0)
                         ],
                         ids=["negative value", "zero value"]
                         )
def test_rectangle_negative_and_zero_value(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("side_a, side_b", [
    (22, 2),
    (2, 22)
])
def test_rectangle_get_area(side_a, side_b):
    r = Rectangle(side_a, side_b)
    assert r.get_area == r.get_area


@pytest.mark.parametrize("side_a, side_b", [
    (2, 22),
    (22, 2)
])
def test_rectangle_get_perimeter(side_a, side_b):
    r = Rectangle(side_a, side_b)
    assert r.get_perimetr == r.get_perimetr
