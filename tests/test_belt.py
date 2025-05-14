import pytest
from belt_simulator.simulator import Belt


@pytest.fixture
def belt():
    belt = Belt(3, ['A', 'B', None])
    belt.slots = ['A', 'B', None]
    return belt

def test_initialization(belt):
    assert len(belt) == 3
    for item in belt.slots:
        assert item in ['A', 'B', None]

def test_shift(belt):
    belt.shift()
    assert belt.lost_count == 1
    assert len(belt) == 3

def test_clear_products(belt):
    belt.slots = ['P', 'P', 'A']
    belt.clear_products()
    assert belt.assembled_count == 2

