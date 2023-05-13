import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="show square of a number")
args = parser.parse_args()
print(args.square**2)