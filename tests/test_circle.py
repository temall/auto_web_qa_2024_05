from src.circle import Circle
import pytest


@pytest.mark.parametrize("radius",
                         [
                             (-2),
                             0,
                             False
                         ],
                         ids=["negative value", "zero value", 'logical']
                         )
def test_circle_negative_zero_adn_logical_value(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_get_area():
    c = Circle(5)
    assert c.get_area == 78.53981633974483


def test_circle_get_perimetr():
    c = Circle(5)
    assert c.get_perimeter == 31.41592653589793
