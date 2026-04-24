import argparse
parser=argparse.ArgumentParser(description="Hello Everyone, This is the tutorial.")

parser.add_argument("name",help="Enter your name")
parser.add_argument("--age",type=int,help="Enter your age")

args=parser.parse_args()
print(f"Hello {args.name}")
if args.age:
    print(f"You are {args.age} years old.")