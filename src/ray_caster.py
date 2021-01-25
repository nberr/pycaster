import sys

# my files
import data
import vector_math
import collisions
import cast

def check_args(argv):
    return False



if __name__ == "__main__":
    argv = sys.argv

    if len(argv) < 2:
        print("Must provide a filename")
        exit(1)
    else:
        try:
            with open(argv[1], "r") as input:
                if check_args(argv):
                    print("good args")
                else:
                    print("usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]")
        except IOError as e:
            print("Could not open file %s." % e)
