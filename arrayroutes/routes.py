# The idea of this one is:
# Try to find the number of ways to go from the top-left to the bottom-right of an array
# Movement only horizontally and vertically.
# A '1' in a cell indicates open cell, can move there; '0' indicates closed cell.

def width(a):
    return len(a[0])

def height(a):
    return len(a)

def abletomoveright(a,x,y):
    return x + 1 < width(a) and a[y][x+1] == 1

def abletomoveleft(a,x,y):
    return x > 1 and a[y][x-1] == 1

def abletomoveup(a,x,y):
    return y > 1 and a[y-1][x] == 1

def abletomovedown(a,x,y):
    return y + 1 < height(a) and a[y+1][x] == 1

def alldestinations(a,x,y,paths):
    outers = []
    if abletomoveright(a,x,y): outers.append((x+1,y))
    #if abletomoveleft(a,x,y): outers.append((x-1,y))
    #if abletomoveup(a,x,y): outers.append((x,y-1))
    # Huh. They didn't want moving backwards to be an option.
    if abletomovedown(a,x,y): outers.append((x,y+1))
    #returnpaths = []
    for path in outers:
        if path not in paths:
            returnpaths.append(path)
    return returnpaths

class Path:
    def __init__(self,head,body):
        self.head = head
        self.body = body
    def __str__(self):
        returnthing = '(' + str(self.head[0]) + ',' + str(self.head[1]) + '): '
        for destination in self.body:
            returnthing += '(' + str(destination[0]) + ',' + str(destination[1]) + ') '
        return returnthing

def numberOfRoutes(a):
    pathstoconsider = [Path((0,0),[(0,0)])]
    routes = 0
    while len(pathstoconsider) > 0:
        path = pathstoconsider.pop()
        for nextplace in alldestinations(a,path.head[0],path.head[1],path.body):
            if nextplace == (width(a)-1,height(a)-1):
                routes += 1
            else:
                pathstoconsider.append(Path(nextplace,[nextplace] + path.body))
    return routes
