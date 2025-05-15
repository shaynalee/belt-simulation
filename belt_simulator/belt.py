import random


class Belt:
    def __init__(self, length, choices):
        self.length = length
        self.choices = choices
        self.slots = [self.component_generator() for _ in range(length)]
        self.lost_count = 0
        self.assembled_count = 0

    def get(self, i):
        return self.slots[i]
    
    def set(self, i, item):
        self.slots[i] = item

    def component_generator(self):
        return random.choice(self.choices)

    def shift(self):
        try:
            item = self.slots.pop(0)
            if item in ['A', 'B']:
                self.lost_count += 1
            elif item == 'P':
                self.assembled_count += 1
            self.slots.append(self.component_generator())
        except IndexError as e:
            print(f"Error: Belt shift failed due to empty slots. ")

    def print_state(self, tick = 0, label = ""):
        visual = ''.join([c if c else '-' for c in self.slots])
        print(f"Tick {tick + 1:03}: {visual} | {label}")

    def __getitem__(self, index):
        return self.slots[index]
    
    def __setitem__(self, index, value):
        self.slots[index] = value

    def __len__(self):
        return self.length

