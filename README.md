# PLEASE READ

Firstly, thank you, I had fun doing the exercise as it pushed me to consider various cases and actions when implementing this out. 


## GENERAL NOTES


- To run the application, use Python >= v3.10.5 and run `python -m pip install -r requirements.txt`
- All the tests are in `tests\` directory. Run `pytest` to run the tests.  
- You may run the simulation by entering `python -m belt_simulation` in the terminal. Although by default _tick_ has been set to 100 and _belt-length_ to 3, user may re-adjust these values via teh terminal. E.g.: `python -m belt_simulator --ticks 100 --belt-length 3`. It is basic and does not handle exceptions.
- `tqvm` and `logging` has been added to track the progress of the main loop in the application.


## EXERCISE

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