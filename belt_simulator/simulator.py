import heapq
import logging
import random
import time
from tqdm import tqdm

from belt_simulator.belt import Belt
from belt_simulator.worker import Worker

logging.basicConfig(level = logging.INFO)

def run_simulation(ticks = 100, belt_length = 3, belt = None, all_workers = None, available_workers = None):
    start_time = time.time()

    # If statements are for mock cases
    if belt is None:
        belt = Belt(belt_length, ['A', 'B', None])

    if all_workers is None:
        left_workers = [Worker(i, 'left') for i in range(belt_length)]
        right_workers = [Worker(i, 'right') for i in range(belt_length)]
        all_workers = left_workers + right_workers

    if available_workers is None:
        available_workers = {i: set() for i in range(belt_length)}
        for worker in all_workers:
            available_workers[worker.position].add(worker)

    for t in tqdm(range(ticks)):
        claimed_slot = {}
        belt.print_state(t, "Before")

        for i in range(belt_length):
            component = belt[i]

            heap = []
            for worker in available_workers[i]:
                score = 0
                # Highest Score goes to completing the assembly of components
                if component not in worker.holding() and 'P' in worker.holding():
                    score = 3
                # If worker doesn't have the component, pick it up
                elif ('A' in worker.holding() and component == 'B') or ('B' in worker.holding() and component == 'A'):
                    score = 2
                # If worker doesn't have the component, pick it up
                elif component not in worker.holding() and None in worker.holding():
                    score = 1
                # Ignore if component is already in worker's hand
                elif component in worker.holding():
                    score = 0

                heapq.heappush(heap, (-score, id(worker), worker))

            if heap:
                _, _, best_worker = heapq.heappop(heap)
                claimed_slot[i] = best_worker

        for i, worker in claimed_slot.items():
            worker.pick(belt)

        for worker in all_workers:
            worker.action(belt, available_workers)

        belt.print_state(t, "After")
        belt.shift()

    logging.info(f"Assembled Count: {belt.assembled_count}, Lost Count: {belt.lost_count}")
    logging.info(f"Elapsed Time: {time.time() - start_time}")
    return {"Assembled": belt.assembled_count, "Lost": belt.lost_count}