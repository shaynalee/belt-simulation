import pytest
from belt_simulator.belt import Belt
from belt_simulator.worker import Worker


@pytest.fixture
def belt():
    belt = Belt(3, ['A', 'B', None])

@pytest.fixture
def worker():
    return Worker(position=1, side='left')

def test_pick_component(belt, worker):
    belt = Belt(3, ['A', 'B', None])
    belt.slots = [None, 'A', 'B']
    worker = Worker(position=1, side='left')
    picked = worker.pick(belt)
    assert picked == True
    assert worker.left_hand == 'A'
    assert belt[1] is None

def test_assemble_and_tick():
    worker = Worker(position=0, side='left')
    worker.left_hand = 'A'
    worker.right_hand = 'B'
    assert worker.assemble() is True
    for _ in range(3):
        worker.tick()
    assert worker.left_hand == 'P'
    assert worker.right_hand is None

def test_place_product():
    belt = Belt(3, ['A', 'B', None])
    belt.slots = [None, None, None]
    worker = Worker(position=0, side='left')
    worker.left_hand = 'P'
    placed = worker.place(belt)
    assert placed is True
    assert worker.left_hand is None
    assert belt[0] == 'P'

def test_worker_action_starts_assembly():
    worker = Worker(position=0, side='left')
    available_workers = {0: set([worker])}

    worker.left_hand = 'A'
    worker.right_hand = 'B'

    # Should begin assembling
    worker.action(belt, available_workers)

    assert worker.assemble_tick == 3
    assert worker not in available_workers[0]

def test_worker_becomes_available_after_assembly():
    worker = Worker(position=0, side='left')
    available_workers = {0: set()}

    worker.assemble_tick = 1  # 1 tick left

    worker.action(None, available_workers)

    # Should have just finished
    assert worker.left_hand == 'P'
    assert worker.assemble_tick == 0
    assert worker in available_workers[0]

def test_worker_places_product():
    worker = Worker(position=1, side='left')
    belt = Belt(3, ['A', 'B', None])
    belt.slots = [None, None, None]
    available_workers = {1: set([worker])}

    worker.left_hand = 'P'

    worker.action(belt, available_workers)

    assert belt[1] == 'P'
    assert worker.left_hand is None
