import argparse
from belt_simulator.simulator import run_simulation


def main():
    parser = argparse.ArgumentParser(description="Run belt simulator.")
    parser.add_argument("--ticks", type=int, default=100)
    parser.add_argument("--belt-length", type=int, default=3)
    args = parser.parse_args()

    run_simulation(ticks=args.ticks, belt_length=args.belt_length)


if __name__ == "__main__":
    main()