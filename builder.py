import argparse
from BuilderOptions import *
from Constants import *
from BuilderHandler import *
if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--x", type=int, default=3)
    parser.add_argument("--y", type=int, default=3)
    parser.add_argument("--o", type=int, default=1)
    parser.add_argument("--c", type=str, default="./whaleExampleModel.candl")
    parser.add_argument("--l", type=str, default="")
    parser.add_argument("--f", type=str, default=Constants.SPC_OUT)
    args = parser.parse_args()

    o = BuilderOptions()
    o.setOptions(args.x, args.y, args.o, args.f+".spc", args.c)
    print("The script will run with the following values: ")
    print(f"> grid horizontal dimension : "+ str(o.x))
    print(f"> grid vertical dimension : "+ str(o.y))
    print(f"> complex objects  : "+ str(o.nco))

    BuilderHandler().build(o)