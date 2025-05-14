import heapq
import random
import time
from tqdm import tqdm # type: ignore


class Belt:
    def __init__(self, length, choices):
        self.length = length
        self.choices = choices
        self.slots = [random.choice(choices) for _ in range(length)]
        self.lost_count = 0
        self.assembled_count = 0

    def get(self, i):
        return self.slots[i]
    
    def set(self, i, item):
        self.slots[i] = item

    def shift(self):
        item = self.slots.pop(0)
        if item in ['A', 'B']:
            self.lost_count += 1
        self.slots.append(random.choice(self.choices))

    def clear_products(self):
        for i in range(self.length):
            if self.slots[i] == 'P':
                self.assembled_count += 1
                # self.slots[i] = None

    def print_state(self, tick, label = ""):
        visual = ''.join([c if c else '-' for c in self.slots])
        if label in ['Before', 'After']:
            print(f"Tick {tick + 1:03}: {visual} | {label}")
        elif label:
            print(f"{label}")

    def __getitem__(self, index):
        return self.slots[index]
    
    def __setitem__(self, index, value):
        self.slots[index] = value

    def __len__(self):
        return self.length

class Worker:
    def __init__(self, position, side):
        self.left_hand = None
        self.right_hand = None
        self.position = position
        self.side = side
        self.assemble_tick = 0
    
    def is_full(self):
        return self.left_hand and self.right_hand
    
    def holding(self):
        return [self.left_hand, self.right_hand]
    
    def assemble(self):
        if 'A' in self.holding() and 'B' in self.holding():
            self.assemble_tick = 3
            return True
        return False

    def tick(self):
        if self.assemble_tick > 0:
            self.assemble_tick -= 1
            if self.assemble_tick == 0 :
                self.left_hand = 'P'
                self.right_hand = None

    def place(self, belt):
        if belt[self.position] is None and self.left_hand == 'P':
            belt[self.position] = 'P'
            self.left_hand = None
            return True
        return False
    
    def exchange_with_belt(self, belt):
        if self.left_hand == 'P' and belt[self.position] in ['A', 'B']:
            if self.right_hand is None and belt[self.position] not in self.holding():
                self.right_hand = belt[self.position]
                belt[self.position] = 'P'
                self.left_hand = None
                return True
        return False
    
    def pick(self, belt):
        if not self.is_full() and belt[self.position] in ['A', 'B'] and belt[self.position] not in self.holding():
            if self.left_hand is None:
                self.left_hand = belt[self.position]
            else:
                self.right_hand = belt[self.position]
            belt[self.position] = None
            return True
        return False

    def action(self, belt, available_workers):
        # Decrease ticker if assemble_time > 0
        if self.assemble_tick > 0:
            self.tick()
            # Just became available after assembling
            if self.assemble_tick == 0:
                available_workers[self.position].add(self)
            return
        
        # If worker has both A and B, assemble
        if self.is_full() and 'A' in self.holding() and 'B' in self.holding():
            if self.assemble():
                available_workers[self.position].discard(self)
            return
        
        # If tick has reached 0, if there's an item on the belt or free slots  at worker position, place item back
        if self.left_hand == 'P':
            if self.exchange_with_belt(belt):
                return
            self.place(belt)
            return
                
start_time = time.time()
belt_length = 3
belt = Belt(belt_length, ['A', 'B', None])
ticks = 100

left_workers = [Worker(i, 'left') for i in range(belt_length)]
right_workers = [Worker(i, 'right') for i in range(belt_length)]
all_workers = left_workers + right_workers
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

            heapq.heappush(heap, (-score, random.random(), worker))

        if heap:
            _, _, best_worker = heapq.heappop(heap)
            claimed_slot[i] = best_worker

    for i, worker in claimed_slot.items():
        worker.pick(belt)

    for worker in all_workers:
        worker.action(belt, available_workers)

    belt.print_state(t, "After")
    belt.clear_products()
    belt.shift()

belt.print_state(t, f"Assembled Count: {belt.assembled_count}, Lost Count: {belt.lost_count}")
belt.print_state(t, f"Elapsed Time: {time.time() - start_time}")