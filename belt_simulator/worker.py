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
            