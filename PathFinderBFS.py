from copy import deepcopy

class PathFinder:
    '''This class traces the path from source to destination'''
    # Constructor to initialize the class
    def __init__(self):
        self.tree = {}
        self.matrix = []
        self.__size = 0
        self.__start = 0
        self.__end = 0
        self.obstacles = []

    # Method to print the contents of the matrix
    def printMatrix(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(self.matrix[i][j], end=" ")
            print()
        print()

    # Method to check is the end point is reachable or not
    def checkEsurround(self):
        nodes = self.tree[self.__end]
        if len(nodes) > 0:
            return False
        return True

    # Method to find path using the breadth first search
    def pathFindBFS(self, start, end):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in self.tree[vertex] - set(path):
                if next == end:
                    return path + [next]
                else:
                    queue.append((next, path + [next]))

    # trace the path found on the matrix
    def setPath(self, path):
        for val in path:
            self.findpos(val, "#")
        self.findpos(self.__start, "S") # Replace the start and end positions
        self.findpos(self.__end, "E")

    # method to find the row and col for a given node in the tree
    def findpos(self, num, val):
        row = num // self.__size
        col = num % self.__size - 1

        if num % self.__size == 0:
            row = row - 1
            col = self.__size - 1

        if row >= 0 and col >= 0 and row < self.__size and col < self.__size:
            self.matrix[row][col] = val


    # Method to set up the tree and matrix
    def setup(self, size, start, end, obstacles):
        self.__size = size
        self.__start = start
        self.__end = end
        self.obstacles = obstacles

        # Iterating through all nodes and finding child of each
        for node in range(1, self.__size*self.__size + 1):
            subnodes = []
            children = []
            subnodes.append(node - 1)
            subnodes.append(node + 1)
            subnodes.append(node - self.__size)
            subnodes.append(node + self.__size)

            children = deepcopy(subnodes)

            if node % self.__size == 0 and (node + 1) in children:  # removing invalid from right border
                children.remove(node + 1)
            if ((node - 1) % self.__size) == 0 and (node - 1) in children: # removing invalid from left border
                children.remove(node - 1)

            for i in subnodes:
                if (i < 1) and (i in children):
                    children.remove(i);
                if (i > self.__size * self.__size) and (i in children):
                    children.remove(i)
                if (str(i) in obstacles) and (i in children):
                    children.remove(i)

            self.tree[node] = set(children)

        # setting up the matrix for printing
        row = []
        for i in range(self.__size):
            for j in range(self.__size):
                row.append("-")
            self.matrix.append(row)
            row = []

        self.findpos(start,"S")
        self.findpos(end,"E")
        for val in obstacles:
            self.findpos(int(val),"O")

