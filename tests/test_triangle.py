from src.triangle import Triangle
import pytest


@pytest.mark.parametrize("side_a, side_b, side_c",
                         [
                             (-4, 4, 4),
                             (4, 0, 4),
                             (4, 0, False)

                         ],
                         ids=["negative value", "zero value", "logical"]
                         )
def test_triangle_negative_zero_and_logical_value(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize("side_a, side_b, side_c",
                         [
                             (2, 2, 6),
                         ])
def test_triangle_sum_of_two_dies_less_than_third_side(side_a, side_b, side_c):
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        raise ValueError("123")
    Triangle(4, 4, 9)


def test_triangle_get_area():
    t = Triangle(4, 4, 4)
    assert t.get_area == 6.928203230275509


def test_triangle_get_perimeter():
    t = Triangle(4, 4, 4)
    assert t.get_perimetr == 12
