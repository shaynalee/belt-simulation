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

def test_component_generator(belt):
    assert belt.component_generator() in ['A', 'B', None]

def test_shift_lost_count(belt):
    belt.slots = ['B', 'P', 'A']
    belt.shift()

    assert belt.lost_count == 1
    assert len(belt) == 3

def test_shift_assembled_count(belt):
    belt.slots = ['P', 'P', 'A']
    belt.shift()

    assert belt.assembled_count == 1
    assert len(belt) == 3

def test_empty_slots_error(capsys):
    belt = Belt(0, ['A', 'B'])
    belt.slots = []
    belt.shift()

    captured = capsys.readouterr()
    assert "Error: Belt shift failed" in captured.out

# Added for 100% coverage lol
def test_belt_get_set():
    belt = Belt(3, ['A', 'B'])
    belt.set(1, 'B')
    assert belt.get(1) == 'B'