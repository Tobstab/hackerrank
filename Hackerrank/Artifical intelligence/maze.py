#wall = %
#pac =P
#path = -
#food = .
#using DFS
#percepts are wall,path or food
#actions are up,down,left or right

#need to check up,down,left, right and see what the percept is 
#need to check what level it is on
maze =[]
stack=[]
nodelvl =0
searching = True
pacPos = input()
foodPos = input()
mazeSize = input()
x_pac= pacPos[0]
y_pac= pacPos[1]

for i in range(int(mazeSize[0])):
    maze.append(input())
#loop to check nodes
while searching:
    freenodes=[]
    #check up
    if maze[x_pac][y_pac+1] == "-":
        freenodes.append(x_pac,y_pac+1)
    #check left
    if maze[x_pac-1][y_pac] == "-":
        freenodes.append(x_pac-1,y_pac)
    #check right
    if maze[x_pac+1][y_pac] == "-":
        freenodes.append(x_pac+1,y_pac)
    #check down
    if maze[x_pac][y_pac-1] == "-":
        freenodes.append(x_pac,y_pac-1)
    stack.append(freenodes)
    if nodelvl == 0:
        
print(pacPos,"\n"
     ,foodPos,"\n",
     mazeSize,"\n",
     maze)