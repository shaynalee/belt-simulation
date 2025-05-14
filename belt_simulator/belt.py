import random


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
        try:
            item = self.slots.pop(0)
            if item in ['A', 'B']:
                self.lost_count += 1
            self.slots.append(random.choice(self.choices))
        except Exception as e:
            print(f"Error: Belt shift failed")

    def clear_products(self):
        for i in range(self.length):
            if self.slots[i] == 'P':
                self.assembled_count += 1

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

