import logging
from PathFinderBFS import PathFinder

'''
This file contains the driver program to trace the path from source to destination
'''

def main():
    inputlist = []
    try:
        with open("assignment5_input.txt") as fin:  # Read the contents of the file input.txt 
            for line in fin:
                line = line.replace("\n", "")  # Removing the \n from the end of the line
                if line != "":
                    inputlist.append(line)  # Adding line to list only if the line has any contents
    except FileNotFoundError as e:
        print("Could not find the file.")
        logging.error("Could not find the file.")
        exit()
    except Exception as e:
        print(type(e), e)
        logging.error(type(e), e)
        exit()

    size = int(inputlist[0])  # Extracting the size of the matrix from the input list
    inputlist.pop(0)
    pos = inputlist[0].split(" ")  # Extracting the starting and ending positions from the input list
    startpos = int(pos[0])
    endpos = int(pos[1])
    inputlist.pop(0)

    pathfinder = PathFinder()
    pathfinder.setup(size, startpos, endpos, inputlist)
    print("Input Matrix: ")
    pathfinder.printMatrix()  # Printing the initial Matrix

    print("Note: This algorithm uses iteration, hence it can take time for large sizes. Please wait")
    print()

    # Check if Ending position is reachable
    if not pathfinder.checkEsurround():
        path = pathfinder.pathFindBFS(startpos,endpos)
        if path is None:
            print("Destination Unreachable")
        else:
            pathfinder.setPath(path)
            print("Path Traced: ", path)
            print("\nOutput Matrix:")
            pathfinder.printMatrix()
    else:
        print("Ending position surrounded on all sides!")
        print("Destination unreachable")


if __name__ == '__main__':
    main()
