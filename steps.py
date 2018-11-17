# class definiton for a stair - makes coding eZ
class Stair:
    steps = 0

    def __init__(self, steps):
        self.steps = steps

    def getSteps(self):
        return int(self.steps)


class Path:
    def __init__(self):
        self.movesTaken = []

    def pathLength(self):
        length = 0
        for i in range(0, len(self.movesTaken)):
            length += self.movesTaken[i]
        return int(length)

    def numberOfMoves(self):
        return len(self.movesTaken)

    def addToPath(self, x):
        self.movesTaken.append(x)

    def getMovesTaken(self):
        return self.movesTaken

    def canBeExploredMore(self, stair):
        return (self.pathLength() < stair.getSteps())


stair = Stair(10)
possibleSteps = [1, 2]
paths = []


def takeStep(stair, path):
    steps = stair.getSteps()
    pathLength = path.pathLength()
    print("Current Path length: " + str(pathLength))
    print("Steps = " + str(steps))


def explore(stair):
    for i in range(0, len(possibleSteps)):
        path = Path()
        path.addToPath(possibleSteps[i])
        paths.append(path)

    for path in paths:
        pathLength = path.pathLength()
        for x in range(0, len(possibleSteps)):
            step = possibleSteps[x]
            totalLength = pathLength + step
            if(totalLength < stair.getSteps()):
                node = path.addToPath(step)
                paths.append(node)


def main():
    if(stair != None):
        explore(stair)
        printResults(paths)


def printResults(results):
    print("Successful paths include: ")
    for i in range(0, len(results)):
        path = results[i]
        if(path is not None):
            if(path.canBeExploredMore == False):
                printPath(path)


def printPath(path):
    print(path.getMovesTaken())


main()
