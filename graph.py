import random
import math
import time
import heapq

#------------------------------------------------------------------------------------------------------------------
# Graph Classes and methods
#------------------------------------------------------------------------------------------------------------------

#base node class
class Node():
    #val is just a interger index of a node
    def __init__(self, Val =1):
        self.val = Val
        
class GridNode(Node):
    def __init__(self, Val,x,y):
        self.val = Val
        self.x = x
        self.y = y
        
# base graph class for nodes        
class Graph():
    #node val is assumed to be a one dimentional possition
    def __init__(self):
        self.nodes = []
        #edges is a two dimentional array listing the connections between nodes
        # null = none, else int = cost
        self.edges = []
    def addNode(self,Val):
        self.nodes.append(Node(Val))
        #generate a column to edges with the proper length
        temp = [[]]*(len(self.edges)+1)
        #add a row to the other nodes
        for i in range(len(self.edges)):
            self.edges[i].append([])
        #add the new column
        self.edges.append(temp)
    def addUndirectedEdge(self,first,second):
        #first and second are interge indexs of nodes
        #check if path exists already and if not add
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [0]
        if(len(self.edges[second][first]) == 0):
            self.edges[second][first] = [0] 
    def removeUndirectedEdge(self,first,second):
        #check if path exists and remove if it exists
        if(len(edges[first][second]) > 0):
            self.edges[first][second] = []
        if(len(edges[second][first]) >0):
            self.edges[second][first] = []
    def getAllNodes(self):
        return self.nodes
    def printGraph(self):
        print('This Graph has: ' + str(len(self.nodes)) + ' nodes.')
        print('The Connections are as follows:')
        for i in range(len(self.nodes)):
            print("\nnode: " + str(i) + ' has connections too:')
            k = 0
            for j in self.edges[i]:
                if (len(j) != 0):
                    print('Node ' + str(k) + ' with a cost of ' + str(j[0]))
                k+=1
            
            
#extend graph with directed edges
class DirectedGraph(Graph):    
    def adddirectedEdge(self,first,second):
        #first and second are interge indexs of nodes
        #check if path exists already and if not add
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [0]
    def removedirectedEdge(self,first,second):
        if(len(self.edges[first][second]) > 0):
            self.edges[first][second] = []
            
#exteds graph with directed and undriected methods with a cost
class WeightedGraph(Graph): 
    def addUndirectedEdge(self,first,second,cost):
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [cost]
        if(len(self.edges[second][first]) == 0):
            self.edges[second][first] = [cost]
    def adddirectedEdge(self,first,second,cost):
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [cost]
    def removedirectedEdge(self,first,second):
        if(len(self.edges[first][second]) > 0):
            self.edges[first][second] = []
            
class GridGraph(Graph):
    def addGridNode(self,x,y,val):
        self.nodes.append(GridNode(x,y,val))
        #generate a column to edges with the proper length
        temp = [[]]*(len(self.edges)+1)
        #add a row to the other nodes
        for i in range(len(self.edges)):
            self.edges[i].append([])
        #add the new column
        self.edges.append(temp)
    def addUndirectedEdge(self,first,second):
        if(first.x-1 <= second.x <= first.x+1):
            if(first.y == second.y):
                self.edges[first.x*int(math.sqrt(len(self.nodes)))+first.y][second.x*int(math.sqrt(len(self.nodes)))+second.y] = [1]
                self.edges[second.x*int(math.sqrt(len(self.nodes)))+second.y][first.x*int(math.sqrt(len(self.nodes)))+first.y] = [1]
        if(first.y-1 <= second.y <= first.y+1):
            if(first.x == second.x):
                self.edges[first.x*int(math.sqrt(len(self.nodes)))+first.y][second.x*int(math.sqrt(len(self.nodes)))+second.y] = [1]
                self.edges[second.x*int(math.sqrt(len(self.nodes)))+second.y][first.x*int(math.sqrt(len(self.nodes)))+first.y] = [1]
    def removedirectedEdge(self,first,second):
        if(len(self.edges[first][second]) > 0):
            self.edges[first][second] = []
            self.edges[second][first] = []
           

#----------------------------------------------------------------------------------------------------------------------
# Graph building methods
#----------------------------------------------------------------------------------------------------------------------


def createRandomUnweightedGraphIter(n):
    graph = Graph()
    for i in range(n):
        graph.addNode(i)
    for i in range(n):
        graph.addUndirectedEdge(random.randint(0,n-1),random.randint(0,n-1))
    return graph


def createLinkedList(n):
    graph = Graph()
    for i in range(n):
        graph.addNode(i)
        if(i == 0):
            continue
        graph.addUndirectedEdge((i-1),i)
    return graph

           
def createRandomDAGIter(n):
    graph = DirectedGraph()
    for i in range(n):
        graph.addNode(i)
    for i in range(n):
        x=random.randint(0,n-1)
        y=random.randint(x,n-1)
        while(x >= y):
            x=random.randint(0,n-1)
            y =random.randint(x,n-1)
        graph.adddirectedEdge(x,y)
    return graph

           
def createRandomCompleteWeightedGraphIter(n):
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(n)
    for i in range(len(graph.nodes)):
        for j in range(len(graph.nodes)):
            if(i==j):
                continue
            graph.adddirectedEdge(i,j,random.randint(1,n))
    return graph


#Renamed method as python does not support overloading
def createWeightedLinkedList(n):
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(1)
    for i in(range(n)):
        if(i == 0):
            continue
        graph.adddirectedEdge((i-1),i,1)
    return graph


def createRandomGridGraph(n):
    graph = GridGraph()
    for i in range(n):
        for j in range(n):
            graph.addGridNode(i,j,i)
    for i in range(n):
        for j in range(n):
            if(random.random()>0.5):
                if(i-1 >0):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*(i-1)+j)])
            if(random.random()>0.5):
                if(i+1 < n):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*(i+1)+j)])
            if(random.random()>0.5):
                if(j-1 > 0):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*i+j-1)])
            if(random.random()>0.5):
                if(j+1 < n):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*i+j-1)])
    return graph
                

#-------------------------------------------------------------------------------------------------------------------
# Search Methods
#-------------------------------------------------------------------------------------------------------------------


class GraphSearch():
    def DFSiter(self,start,stop,graph):
        #graph is need here just to get the connected nodes
        visited = []
        search = [start]
        while (len(search) > 0):
            temp = search.pop()
            if(temp in visited):
                continue
            visited.append(temp)
            if (temp == stop):
                return visited
            for i in graph.edges[temp]:
                if(len(i) > 0):
                    search.append(i[0])
        return None
        
    def DFSrec(self,start,stop):
        ret = []
        def DFSrecsearch(start,stop):
            if(start == stop):
                ret.append(start)
                return
            if(start in ret):
                return
            for i in start.edges():
                DFSrecsearch(i[0],stop)
        DFSrecsearch(start,stop)
        if(stop in ret):
            return ret
        return None
    def BFSrec(self,start,stop,graph):
        #ret is return
        ret = []
        queue = []
        
        def BFSrecsearch(self,start,stop,graph):
            if(start == stop):
                ret.append(start)
                return
            if(start in ret):
                if(len(queue) > 0):
                    BFSrecsearch(self,queue.pop(0),stop,graph)
                    return
                return
            ret.append(start)
            for i in range(len(graph.edges[start])):
                if(len(graph.edges[start][i])>0):
                    queue.append(i)
            BFSrecsearch(self,queue.pop(0),stop,graph)
            
            
        BFSrecsearch(self,start,stop,graph)
        if(len(ret)>0):
            return ret
        return None
    def BFSiter(self,start,stop,graph):
        visited = []
        search = [start]
        while (len(search) > 0):
            temp = search.pop(0)
            if(temp in visited):
                continue
            visited.append(temp)
            if(temp == stop):
                return visited
            for i in range(len(graph.edges[temp])):
                if(len(graph.edges[temp][i])>0):
                    search.append(i)
        return None
    
class TopSort():
    def Khans(self,DirectedGraph):
        graph = DirectedGraph
        ret =[]
        visited = 0
        indegree=[0]*len(graph.nodes)
        for i in range(len(graph.edges)):
            for j in range(len(graph.edges)):
                if(len(graph.edges[i][j]) > 0):
                    indegree[j] +=1
        queue = []
import random
import math
import time
import heapq

#------------------------------------------------------------------------------------------------------------------
# Graph Classes and methods
#------------------------------------------------------------------------------------------------------------------

#base node class
class Node():
    #val is just a interger index of a node
    def __init__(self, Val =1):
        self.val = Val
        
class GridNode(Node):
    def __init__(self, Val,x,y):
        self.val = Val
        self.x = x
        self.y = y
        
# base graph class for nodes        
class Graph():
    #node val is assumed to be a one dimentional possition
    def __init__(self):
        self.nodes = []
        #edges is a two dimentional array listing the connections between nodes
        # null = none, else int = cost
        self.edges = []
    def addNode(self,Val):
        self.nodes.append(Node(Val))
        #generate a column to edges with the proper length
        temp = [[]]*(len(self.edges)+1)
        #add a row to the other nodes
        for i in range(len(self.edges)):
            self.edges[i].append([])
        #add the new column
        self.edges.append(temp)
    def addUndirectedEdge(self,first,second):
        #first and second are interge indexs of nodes
        #check if path exists already and if not add
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [0]
        if(len(self.edges[second][first]) == 0):
            self.edges[second][first] = [0] 
    def removeUndirectedEdge(self,first,second):
        #check if path exists and remove if it exists
        if(len(edges[first][second]) > 0):
            self.edges[first][second] = []
        if(len(edges[second][first]) >0):
            self.edges[second][first] = []
    def getAllNodes(self):
        #returns the list of nodes
        return self.nodes
    def printGraph(self):
        #prints out each node, its connections and their cost
        print('This Graph has: ' + str(len(self.nodes)) + ' nodes.')
        print('The Connections are as follows:')
        #iterate though edges to print cost and connections
        for i in range(len(self.nodes)):
            print("\nnode: " + str(i) + ' has connections too:')
            k = 0
            for j in self.edges[i]:
                if (len(j) != 0):
                    print('Node ' + str(k) + ' with a cost of ' + str(j[0]))
                k+=1
            
            
#extend graph with directed edges
class DirectedGraph(Graph):    
    def adddirectedEdge(self,first,second):
        #first and second are interge indexs of nodes
        #check if path exists already and if not add
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [0]
    def removedirectedEdge(self,first,second):
        if(len(self.edges[first][second]) > 0):
            self.edges[first][second] = []
   

#exteds graph with directed and undriected methods with a cost
class WeightedGraph(Graph): 
    def addUndirectedEdge(self,first,second,cost):
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [cost]
        if(len(self.edges[second][first]) == 0):
            self.edges[second][first] = [cost]
    def adddirectedEdge(self,first,second,cost):
        if(len(self.edges[first][second]) == 0):
            self.edges[first][second] = [cost]
    def removedirectedEdge(self,first,second):
        if(len(self.edges[first][second]) > 0):
            self.edges[first][second] = []
            
            
#extend the grap class to be a grid
class GridGraph(Graph):
    def addGridNode(self,x,y,val):
        self.nodes.append(GridNode(x,y,val))
        #generate a column to edges with the proper length
        temp = [[]]*(len(self.edges)+1)
        #add a row to the other nodes
        for i in range(len(self.edges)):
            self.edges[i].append([])
        #add the new column
        self.edges.append(temp)
    def addUndirectedEdge(self,first,second):
        #check if neighbor
        if(first.x-1 <= second.x <= first.x+1):
            if(first.y == second.y):
                #calculate possition of neigbor in list of nodes
                self.edges[first.x*int(math.sqrt(len(self.nodes)))+first.y][second.x*int(math.sqrt(len(self.nodes)))+second.y] = [1]
                self.edges[second.x*int(math.sqrt(len(self.nodes)))+second.y][first.x*int(math.sqrt(len(self.nodes)))+first.y] = [1]
        #determing if next node is neighbor
        if(first.y-1 <= second.y <= first.y+1):
            if(first.x == second.x):
                #cacluate th posistion of the neighbor
                self.edges[first.x*int(math.sqrt(len(self.nodes)))+first.y][second.x*int(math.sqrt(len(self.nodes)))+second.y] = [1]
                self.edges[second.x*int(math.sqrt(len(self.nodes)))+second.y][first.x*int(math.sqrt(len(self.nodes)))+first.y] = [1]
    def removedirectedEdge(self,first,second):
        if(len(self.edges[first][second]) > 0):
            self.edges[first.x*int(math.sqrt(len(self.nodes)))+first.y][second.x*int(math.sqrt(len(self.nodes)))+second.y] = []
            self.edges[second.x*int(math.sqrt(len(self.nodes)))+second.y][first.x*int(math.sqrt(len(self.nodes)))+first.y] = []
           

#----------------------------------------------------------------------------------------------------------------------
# Graph building methods
#----------------------------------------------------------------------------------------------------------------------


def createRandomUnweightedGraphIter(n):
    #creates a random uneighted graph
    graph = Graph()
    for i in range(n):
        graph.addNode(i)
    for i in range(n):
        graph.addUndirectedEdge(random.randint(0,n-1),random.randint(0,n-1))
    return graph


def createLinkedList(n):
    #creates a doubly linked list
    graph = Graph()
    for i in range(n):
        graph.addNode(i)
        if(i == 0):
            continue
        graph.addUndirectedEdge((i-1),i)
    return graph

           
def createRandomDAGIter(n):
    #Creates a Directed acyclic graph
    graph = DirectedGraph()
    for i in range(n):
        graph.addNode(i)
    for i in range(n):
        x=random.randint(0,n-1)
        y=random.randint(x,n-1)
        while(x >= y):
            #Ensure no cycles by generating a second node that is alwasy farther along that the first
            x=random.randint(0,n-1)
            y =random.randint(x,n-1)
        graph.adddirectedEdge(x,y)
    return graph

           
def createRandomCompleteWeightedGraphIter(n):
    #creates a complete graph with random edge weights
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(n)
    for i in range(len(graph.nodes)):
        for j in range(len(graph.nodes)):
            if(i==j):
                continue
            graph.adddirectedEdge(i,j,random.randint(1,n))
    return graph


#Renamed method as python does not support overloading
def createWeightedLinkedList(n):
    #creates a weighted singly linked list
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(1)
    for i in(range(n)):
        if(i == 0):
            continue
        graph.adddirectedEdge((i-1),i,1)
    return graph


def createRandomGridGraph(n):
    graph = GridGraph()
    for i in range(n):
        for j in range(n):
            graph.addGridNode(i,j,i)
    for i in range(n):
        for j in range(n):
            #50/50 chance to generate each edge
            if(random.random()>0.5):
                if(i-1 >0):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*(i-1)+j)])
            if(random.random()>0.5):
                if(i+1 < n):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*(i+1)+j)])
            if(random.random()>0.5):
                if(j-1 > 0):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*i+j-1)])
            if(random.random()>0.5):
                if(j+1 < n):
                    graph.addUndirectedEdge(graph.nodes[(n*i+j)],graph.nodes[(n*i+j-1)])
    return graph
                

#-------------------------------------------------------------------------------------------------------------------
# Search Methods
#-------------------------------------------------------------------------------------------------------------------


class GraphSearch():
    def DFSiter(self,start,stop,graph):
        #graph is need here just to get the connected nodes
        visited = []
        search = [start]
        while (len(search) > 0):
            temp = search.pop()
            if(temp in visited):
                continue
            visited.append(temp)
            if (temp == stop):
                return visited
            for i in graph.edges[temp]:
                if(len(i) > 0):
                    search.append(i[0])
        return None
        
    def DFSrec(self,start,stop):
        #ret is the return list
        ret = []
        
        #helper method for dfsrec
        def DFSrecsearch(start,stop):
            if(start == stop):
                ret.append(start)
                return
            if(start in ret):
                return
            for i in start.edges():
                DFSrecsearch(i[0],stop)
        DFSrecsearch(start,stop)
        if(stop in ret):
            return ret
        return None
    
    
    def BFSrec(self,start,stop,graph):
        #ret is return
        ret = []
        queue = []
        
        #Helper method for bfsrec
        def BFSrecsearch(self,start,stop,graph):
            if(start == stop):
                ret.append(start)
                return
            if(start in ret):
                if(len(queue) > 0):
                    BFSrecsearch(self,queue.pop(0),stop,graph)
                    return
                return
            ret.append(start)
            for i in range(len(graph.edges[start])):
                if(len(graph.edges[start][i])>0):
                    queue.append(i)
            BFSrecsearch(self,queue.pop(0),stop,graph)
            
        BFSrecsearch(self,start,stop,graph)
        if(len(ret)>0):
            return ret
        return None
    
    
    def BFSiter(self,start,stop,graph):
        visited = []
        search = [start]
        while (len(search) > 0):
            temp = search.pop(0)
            if(temp in visited):
                continue
            visited.append(temp)
            if(temp == stop):
                return visited
            for i in range(len(graph.edges[temp])):
                if(len(graph.edges[temp][i])>0):
                    search.append(i)
        return None
    
class TopSort():
    #does a khans top sort
    def Khans(self,DirectedGraph):
        graph = DirectedGraph
        ret =[]
        visited = 0
        indegree=[0]*len(graph.nodes)
        #calculat indegree of each node
        for i in range(len(graph.edges)):
            for j in range(len(graph.edges)):
                if(len(graph.edges[i][j]) > 0):
                    indegree[j] +=1
        queue = []
        for i in range(len(indegree)):
            if (indegree[i] == 0):
                queue.append(i)
        while(len(queue) > 0):
            temp = queue.pop(0)
            ret.append(temp)
            for i in range(len(graph.edges[temp])):
                if(len(graph.edges[temp][i]) > 0):
                    indegree[i] -=1
                if(indegree[i] == 0 and (i not in ret) and i not in queue):
                    queue.append(i)
            visited+=1
            if(visited>len(graph.nodes)):
                break
        return(ret)
    
    def mDFS(self,DirectedGraph):
        #helper function
        def mDFSort(self,index,visit,stack):
            visit[index] = True
            for i in range(len(graph.edges[index])):
                if(len(graph.edges[index][i])>0):
                    if(not visit[i]):
                        mDFSort(self,i,visit,stack)
            stack.insert(0,index)
            
        graph = DirectedGraph
        stack = []
        visit=[False]*len(graph.nodes)
        for i in range(len(visit)):
            if(not visit[i]):
                mDFSort(self,i,visit,stack)
        return stack
    

#assuming node zero as start
#prints a path to each node
#followed by a distance list
def dijsktras(WeightedGraph):
    graph = WeightedGraph
    path = [[] for _ in range(len(graph.nodes))]
    distance = [math.inf]*len(graph.nodes)
    distance[0] = 0
    print(path)
    visit = [False]*len(graph.nodes)
    #run on every node
    for i in range(len(graph.nodes)):
        min = math.inf
        #find the next smallest node
        for j in range(len(distance)):
            if(distance[j]<min and visit[j] == False):
                min = distance[j]
                next = j         
        visit[next] = True
        #iterate through that nodes edges and update
        for k in range(len(graph.edges[next])):
            if(len(graph.edges[next][k])>0):
                new = distance[next] + graph.edges[next][k][0]
                if (new < distance[k]):
                    distance[k] = new
                    path[k].append(next)
                    print(path)
    path.append(distance)
    return path      


def astar(start,end,graph):
    path = []
    distance = [math.inf]*len(graph.nodes)
    estdist = [math.inf]*len(graph.nodes)
    #calculate manhattan distance hurestic
    for i in range(len(estdist)):
        estdist[i] = (abs(graph.nodes[end].x - graph.nodes[i].x) +abs(graph.nodes[end].y - graph.nodes[i].y))
    distance[0] = 0
    visit = [False]*len(graph.nodes) 
    pq = []
    heapq.heappush(pq,(0,0))
    #start searching
    while(len(pq) > 0):
        temp = heapq.heappop(pq)
        visit[temp[1]] = True
        #break if reched goal
        if (temp[1] == end):
            path.append(temp[1])
            break
        j = 0
        #iterate through the edges of the current node and update
        for i in range(len(graph.edges[temp[1]])):
            if(len(graph.edges[temp[1]][i])>0 and not visit[i]):
                distance[i] = distance[temp[1]]+ graph.edges[temp[1]][i][0]
                if(((distance[i]+estdist[i]),i) not in pq):
                    heapq.heappush(pq,((distance[i]+estdist[i]),i))
                    j+=1
        if(j >0):
            path.append(temp[1])
            print(temp[1])
            
    return path

#-------------------------------------------------------------------------
# Start of code for testing methods and classes
#-------------------------------------------------------------------------


print('Random undirected graph with five nodes\n')
temp = createRandomUnweightedGraphIter(5)
temp.printGraph()

print('\nLinked list graph with 5 nodes\n')
temp = createLinkedList(5)
temp.printGraph()

print('\nRandom graph with five nodes\n')
temp = createRandomDAGIter(5)
temp.printGraph()

print('Random weighted complete directed graph with five nodes\n')
temp = createRandomCompleteWeightedGraphIter(5)
temp.printGraph()


print('\nWeighted Linked list graph with 5 nodes\n')
temp = createWeightedLinkedList(5)
temp.printGraph()


search = GraphSearch()
topsearch = TopSort()


#python recursion limit hits on 10k length recursive
temp = createLinkedList(100)
print('\nRecursive BFT search on linked list')
print(search.BFSrec(0,len(temp.nodes),temp))


temp = createLinkedList(10000)
print('Built list')
print('\nIterative BFT search on lined list')
#build time of 10K lined list is a min or so
#While this is improved over the last methods its still memory heavy
print(search.BFSiter(0,len(temp.nodes)-1,temp))


print('\nRandom Graph for topological sorts')
temp =createRandomDAGIter(1000)
#temp.printGraph()

print('\nKhans top sort on randomDAG Graph\n')
print(topsearch.Khans(temp))

print('\nmDFS on the same randomDAG Graph')
print(topsearch.mDFS(temp))

temp =createRandomCompleteWeightedGraphIter(5)
temp.printGraph()
print(dijsktras(temp))

temp = createRandomGridGraph(5)
temp.printGraph()
print('finished graph')
print(astar(0,len(temp.nodes)-1,temp))
 


