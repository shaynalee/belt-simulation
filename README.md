# PLEASE READ

Firstly, thank you, I had fun doing the exercise as it made me think of how an actual factory would work and it pushed me to consider various cases and actions when implementing this out. 


## IMPORTANT NOTE
- To run the application, use Python v3.10+ and run `python -m pip install -r requirements.txt`.
- You may run the simulation by entering `python -m belt_simulation` in the command-line. Although by default _tick_ has been set to 100 and _belt-length_ to 3, user may re-adjust these values via the terminal. E.g.: `python -m belt_simulator --ticks 100 --belt-length 3`. 
- All the tests are in `tests\` directory. Run `pytest` to run the tests.
- If you'd like to see the test coverage, run `pytest --cov=belt_simulator --cov-report=term-missing` in the command-line.


## Functional and Non-Functional Requirements
_The decision behind the design and implementation of the application were made based off these assumptions._

**Functional Requirements**
1. Conveyer Belt Behaviour
- Default Case: 100 ticks
- Components (`A`, `B`, `None`) will appear in the slots on the belt.
- The belt shifts **right to left** one tick at a time.

2. Worker Behaviour
- Default case: 3 pairs of workers, one on each side of the belt.
- Assumption 1: The number of workers is determined by the working length of the conveyer belt. E.g: If belt length = 3, there are 3 pairs of workers. If belt length = 100, there are 100 pairs of workers.
- Assumption 2: Efficient assembly, clearance of components and minimization of redundant actions is decided by a scoring system of the workers, which later determines the actions taken by them using a max heap. This ensures that only 1 worker at a certain belt position may take action towards the component on the belt.
- Workers exist on each side of the belt.
- Workers may pick up components (`A`, `B`) directly in front of them at their respective position.
- Workers can hold both `A` and `B` to form product `P` in 4 ticks.
- Upon assembly, worker puts the product `P` back onto the belt.

3. Track Count
- Count no. of assembled products upon it being shifted off at the end of the belt.
- Count no. of components lost due to not being picked up at the end of the belt.

4. Run Simulation for Configurable Ticks and Belt Length
- Accept `--ticks` and `--belt-length` as command-line parameters.

5. Support Unit Testing, Basic Integration and Smoke Testing
- Provide testable logic for all components with a 100% coverage.
- Has a simulation in `simulator.py` using print statements to visualize the before and after of belt states at each tick in `line 31` and `line 64`. (Currently commented out to prevent a wall of text.)

**Non-Functional Requirements**
1. Maintainability
- Code is refactored to be modular and organized by their responsibility (`belt.py`, `worker.py`, etc.)
- Uses unit tests and fixtures for regression protection.

2. Readability
- Follows standard naming conventions and OOP principles.
- Has clear comments, logging and test outputs. 

3. Testability
- Pytest framework used with fixtures.

4. Configurability
- Simulation behaviour (tick count, belt length) is adjustable via command line

5. Extensibility
- Easy to add new worker types, belt behaviours or scoring logic to determine which worker to priotize picking/replacing the component.


## Exercise

There is a factory production line around a single a conveyor belt.

Components (of type A and B) come onto the start of the belt at random intervals; workers must take one component of each type from the belt as they come past, and combine them to make a finished product.

The belt is divided into fixed-size slots; each slot can hold only one component or one finished product. There are a number of worker stations on either side of the belt, spaced to match the size of the slots on the belt.

The production line may look like this, where A represents a component of type A, B represents a component of type B, and P represents the finished product:

       v   v   v   v   v          workers
     ---------------------
  -> | A |   | B | A | P | ->     conveyor belt
     ---------------------
       ^   ^   ^   ^   ^          workers

In each unit of time, the belt moves forwards one position, and there is time for a worker on one side of each slot to EITHER take an item from the slot or replace an item onto the belt. The worker opposite them can't touch the same belt slot while they do this. So you can't have one worker picking something from a slot while their counterpart puts something down in the same place.

Once a worker has collected one of both types of component, they can begin assembling the finished product. This takes an amount of time, so they will only be ready to place the assembled product back on the belt on the fourth subsequent slot. While they are assembling the product, they can't touch the conveyor belt. Workers can only hold two items (component or product) at a time: one in each hand.

Create a simulation of this, with three pairs of workers. At each time interval, the slot at the start of the conveyor belt should have an equal (1/3) chance of containing nothing, a component A or a component B.

Run the simulation for 100 steps, and compute how many finished products come off the production line, and how many components of each type go through the production line without being picked up by any workers.

A few things to note:
- The code does not have to be production quality, but we will be looking for evidence that it's written to be somewhat flexible, and that a third party would be able to read and maintain it.
- Flexibility in the solution is preferred, but we are also looking for a sensible decision on where this adds too much complexity.
- Be sure to state your assumptions, how the solution was tested and document the output from running the simulator.
- GenAI is great but please refrain from using AI assistants for this challenge, we want to evaluate your non-AI-assisted technical ability.