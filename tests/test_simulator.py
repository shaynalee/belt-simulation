from unittest import mock
import pytest
from belt_simulator.belt import Belt
from belt_simulator.simulator import run_simulation

# Basic Integration Test
@mock.patch("belt_simulator.belt.Belt.component_generator", side_effect=['A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A'])
def test_run_simulation_basic(mock_gen):
    belt = Belt(2, ['A', 'B', None])
    result = run_simulation(ticks=8, belt_length=2, belt=belt)

    assert result["Assembled"] == 1
    assert result["Lost"] == 1

# Smoke Test
def test_simulation_runs_without_crashing():
    run_simulation(ticks=100, belt_length=2000)
