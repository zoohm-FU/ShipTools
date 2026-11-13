
import pytest

from calculations import (
    battery_energy_kwh,
    estimated_runtime_hours,
    knots_to_kmh,
    kmh_to_knots,
    knots_to_ms,
    ms_to_knots,
    meters_to_kilometers,
    kilometers_to_meters,
    meters_to_centimeters,
    centimeters_to_meters,
    meters_to_millimeters,
    millimeters_to_meters,
    kg_to_tons,
    tons_to_kg,
    kg_to_grams,
    grams_to_kg,
)


def test_battery_energy():
    assert battery_energy_kwh(400, 200) == 80


def test_estimated_runtime():
    assert estimated_runtime_hours(400, 200, 0.9, 20) == pytest.approx(3.6)


def test_invalid_battery_values():
    with pytest.raises(ValueError):
        battery_energy_kwh(-400, 200)


def test_invalid_runtime_values():
    with pytest.raises(ValueError):
        estimated_runtime_hours(400, 200, 1.1, 20)

    with pytest.raises(ValueError):
        estimated_runtime_hours(400, 200, 0.9, 0)


def test_speed_conversions():
    assert knots_to_kmh(10) == pytest.approx(18.52)
    assert kmh_to_knots(18.52) == pytest.approx(10)
    assert knots_to_ms(10) == pytest.approx(5.14444)
    assert ms_to_knots(5.14444) == pytest.approx(10)


def test_length_conversions():
    assert meters_to_kilometers(1000) == 1
    assert kilometers_to_meters(1) == 1000
    assert meters_to_centimeters(2) == 200
    assert centimeters_to_meters(200) == 2
    assert meters_to_millimeters(2) == 2000
    assert millimeters_to_meters(2000) == 2


def test_weight_conversions():
    assert kg_to_tons(1500) == 1.5
    assert tons_to_kg(1.5) == 1500
    assert kg_to_grams(2) == 2000
    assert grams_to_kg(2000) == 2
