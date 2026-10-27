
import pytest

from unit_converter.length import convert_length


def test_mile_to_meters():
    assert convert_length(1, "mi", "m") == pytest.approx(1609.344)


def test_meters_to_kilometers():
    assert convert_length(1000, "m", "km") == pytest.approx(1)


def test_kilometers_to_miles():
    assert convert_length(1, "km", "mi") == pytest.approx(1000 / 1609.344)


def test_zero_length():
    assert convert_length(0, "m", "km") == pytest.approx(0)


def test_negative_length_raises_value_error():
    with pytest.raises(ValueError):
        convert_length(-1, "m", "km")


def test_unknown_unit_raises_value_error():
    with pytest.raises(ValueError):
        convert_length(1, "yard", "m")
