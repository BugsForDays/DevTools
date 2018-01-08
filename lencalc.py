import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text", help="txt to calc len")
args = parser.parse_args()

print(str(len(args.text)))
