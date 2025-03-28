import pytest
from water_flow import (
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)

def test_pressure_loss_from_fittings():
    assert pytest.approx(pressure_loss_from_fittings(0.00, 3), abs=0.001) == 0.000
    assert pytest.approx(pressure_loss_from_fittings(1.65, 0), abs=0.001) == 0.000
    assert pytest.approx(pressure_loss_from_fittings(1.65, 2), abs=0.001) == -0.109
    assert pytest.approx(pressure_loss_from_fittings(1.75, 2), abs=0.001) == -0.122
    assert pytest.approx(pressure_loss_from_fittings(1.75, 5), abs=0.001) == -0.306

def test_reynolds_number():
    assert pytest.approx(reynolds_number(0.048692, 0.00), abs=1) == 0
    assert pytest.approx(reynolds_number(0.048692, 1.65), abs=1) == 80069
    assert pytest.approx(reynolds_number(0.048692, 1.75), abs=1) == 84922
    assert pytest.approx(reynolds_number(0.286870, 1.65), abs=1) == 471729
    assert pytest.approx(reynolds_number(0.286870, 1.75), abs=1) == 500318

def test_pressure_loss_from_pipe_reduction():
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692), abs=0.001) == 0.000
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692), abs=0.001) == -163.744
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692), abs=0.001) == -184.182

def test_kpa_to_psi():
    assert pytest.approx(kpa_to_psi(0), abs=0.001) == 0.000
    assert pytest.approx(kpa_to_psi(101.325), abs=0.001) == 14.696
    assert pytest.approx(kpa_to_psi(200), abs=0.001) == 29.007
    assert pytest.approx(kpa_to_psi(500), abs=0.001) == 72.518
    assert pytest.approx(kpa_to_psi(1000), abs=0.001) == 145.038

if __name__ == "__main__":
    pytest.main()
