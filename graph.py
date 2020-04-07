import random
import math
import time
import sys
class Node():
    def __init__(self, Val =1):
        self.edges = []
        self.val = Val
    def addEdge(self,cost,node):
        if([node,cost] not in self.edges):
            self.edges.append([node,cost])
    def removeEdge(self,cost,node):
        while([node,cost] in self.edges):
            del edges[[node,cost]]
class Graph():
    #node val is assumed to be a one dimentional possition
    def __init__(self):
        self.nodes = []
    def addNode(self,Val):
        self.nodes.append(Node(Val))
    def addUndirectedEdge(self,first,second):
        cost = 0
        first.addEdge(cost,second)
        second.addEdge(cost,first)
    def removeUndirectedEdge(self,first,second):
        cost = 0
        first.removeEdge(cost,second)
        second.removeEdge(cost,first)
    def getAllNodes(self):
        return self.nodes
    def printGraph(self):
        print('This Graph has: ' + str(len(self.nodes)) + ' nodes.')
        print('The Connections are as follows:')
        for i in range(len(self.nodes)):
            print("\nnode: " + str(i) + ' has connections too:')
            for j in range(len(self.nodes[i].edges)):
                print('To node ' + str(self.nodes.index(self.nodes[i].edges[j][0])) + ' with a cost of '+ str(self.nodes[i].edges[j][1]))
class DirectedGraph(Graph):
    
    def adddirectedEdge(self,first,second):
        cost = 0
        first.addEdge(cost,second)
    def removedirectedEdge(self,first,second):
        cost = 0
        first.removeEdge(cost,second)
                
class WeightedGraph(Graph): 
    def addUndirectedEdge(self,first,second,cost = None):
        if (cost == None):
            cost = abs(first.val-second.val)
        first.addEdge(cost,second)
        second.addEdge(cost,first)
    def removeUndirectedEdge(self,first,second,cost = None):
        if (cost == None):
            cost = abs(first.val-second.val)
        first.removeEdge(cost,second)
        second.removeEdge(cost,first)
    def adddirectedEdge(self,first,second,cost = None):
        if (cost == None):
            cost = abs(first.val-second.val)
        first.addEdge(cost,second)
    def removedirectedEdge(self,first,second,cost = None):
        if (cost == None):
            cost = abs(first.val-second.val)
        first.removeEdge(cost,second)
                
def createRandomUnweightedGraphIter(n):
    graph = Graph()
    for i in range(n):
        graph.addNode(1)
    t = random.randint(1,n)
    temp = list(range(t))
    random.shuffle(temp)
    for i in temp:
        graph.addUndirectedEdge(graph.nodes[random.randint(0,n-1)],graph.nodes[random.randint(0,n-1)])
    return graph
print('Random directed graph with five nodes\n')
temp = createRandomUnweightedGraphIter(5)
temp.printGraph()

def createLinkedList(n):
    graph = Graph()
    for i in range(n):
        graph.addNode(1)
    for i in(range(n)):
        if(i == 0):
            continue
        graph.addUndirectedEdge(graph.nodes[i-1],graph.nodes[i])
    return graph
print('\nLinked list graph with 5 nodes\n')
temp = createLinkedList(5)
temp.printGraph()

def createRandomDAGIter(n):
    graph = DirectedGraph()
    for i in range(n):
        graph.addNode(1)
    t = random.randint(1,n)
    temp = list(range(t))
    random.shuffle(temp)
    for i in temp:
        x=0
        y=0
        while(x == y):
            x =random.randint(0,n-1)
            y =random.randint(0,n-1)
        graph.adddirectedEdge(graph.nodes[x],graph.nodes[y])
    return graph
print('\nRandom graph with five nodes\n')
temp = createRandomDAGIter(5)
temp.printGraph()

def createRandomCompleteWeightedGraphIter(n):
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(1)
    for i in graph.nodes:
        for j in graph.nodes:
            if(i==j):
                continue
            graph.adddirectedEdge(i,j,random.randint(1,n))
    return graph
print('Random weighted complete directed graph with five nodes\n')
temp = createRandomCompleteWeightedGraphIter(5)
temp.printGraph()
#Renamed method as python does not support overloading
def createWeightedLinkedList(n):
    graph = WeightedGraph()
    for i in range(n):
        graph.addNode(1)
    for i in(range(n)):
        if(i == 0):
            continue
        graph.adddirectedEdge(graph.nodes[i-1],graph.nodes[i],1)
    return graph
print('\nWeighted Linked list graph with 5 nodes\n')
temp = createWeightedLinkedList(5)
temp.printGraph()

class GraphSearch():
    def DFSiter(self,start,stop):
        visited = []
        search = [start]
        while (len(search) > 0):
            temp = search.pop()
            if(temp in visited):
                continue
            visited.append(temp)
            if (temp == stop):
                return visited
            for i in temp.edges:
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
    def BFSrec(self,start,stop):
        ret = []
        queue = []
        def BFSrecsearch(self,start,stop):
            if(start == stop):
                ret.append(start)
                return
            if(start in ret):
                if(len(queue) > 0):
                    BFSrecsearch(self,queue.pop(0),stop)
                    return
                return
            ret.append(start)
            for i in start.edges:
                queue.append(i[0])
            BFSrecsearch(self,queue.pop(0),stop)
        BFSrecsearch(self,start,stop)
        if(len(ret)>0):
            return ret
        return None
    def BFSiter(self,start,stop):
        visited = []
        search = [start]
        while (len(search) > 0):
            temp = search.pop(0)
            if(temp in visited):
                continue
            visited.append(temp)
            if(temp == stop):
                return visited
            for i in temp.edges:
                search.append(i[0])
        return None
    
class TopSort():
    def Khans(self,DirectedGraph):
        graph = DirectedGraph
        ret =[]
        visited = 0
        indegree=[0]*len(graph.nodes)
        for i in graph.nodes:
            for j in i.edges:
                indegree[graph.nodes.index(j[0])] +=1
        queue = []
        for i in range(len(indegree)):
            if (indegree[i] == 0):
                queue.append(graph.nodes[i])
        while(len(queue) > 0):
            temp = queue.pop(0)
            ret.append(graph.nodes.index(temp))
            for i in temp.edges:
                indegree[graph.nodes.index(i[0])] -=1
                if(indegree[graph.nodes.index(i[0])] == 0):
                    queue.append(i[0])
            visited+=1
        return(ret)
    def mDFS(self,DirectedGraph):
        def mDFSort(self,index,visit,stack):
            visit[index] = True
            for i in graph.nodes[index].edges:
                if(not visit[graph.nodes.index(i[0])]):
                    mDFSort(self,graph.nodes.index(i[0]),visit,stack)
            stack.insert(0,index)
        graph = DirectedGraph
        stack = []
        visit=[False]*len(graph.nodes)
        for i in range(len(visit)):
            if(not visit[i]):
                mDFSort(self,i,visit,stack)
        return stack
class TreadmillMazeSolver():
    #assuming node zero as start
    #prints a path to each node
    #followed by a distance list
    def dijsktras(self,WeightedGraph):
        graph = WeightedGraph
        path = [[]]*len(graph.nodes)
        distance = [math.inf]*len(graph.nodes)
        distance[0] = 0
        visit = [False]*len(graph.nodes)
        for i in range(len(graph.nodes)):
            min = math.inf
            for j in range(len(distance)):
                if(distance[j]<min and visit[j] == False):
                    min = distance[j]
                    next = j         
            visit[next] = True
            for k in graph.nodes[next].edges:
                index = graph.nodes.index(k[0])
                new = distance[next] + k[1]
                if (new < distance[index]):
                    distance[index] = new
                    path[index].append(graph.nodes[next])
        path.append(distance)
        return path           
    def astar(self,WeightedGraph):
        graph = WeightedGraph
        path = [[]]*len(graph.nodes)
        distance = [math.inf]*len(graph.nodes)
        estdist = [math.inf]*len(graph.nodes)
        estdist[0] = 1
        distance[0] = 0
        visit = [False]*len(graph.nodes)
        for i in range(len(graph.nodes)):
            min = math.inf
            for j in range(len(estdist)):
                if(estdist[j]<min  and visit[j] == False):
                    min = distance[j]
                    next = j         
            visit[next] = True
            for k in graph.nodes[next].edges:
                index = graph.nodes.index(k[0])
                new = distance[next] + k[1]
                if (new < distance[index]):
                    distance[index] = new
                    estdist[j] = new+1
                    path[index].append(graph.nodes[next])
        path.append(distance)
        return path 
        
        
search = GraphSearch()
topsearch = TopSort()
maze = TreadmillMazeSolver()
temp = createLinkedList(10)
print('\nRecursive BFT search on linked list')
print(search.BFSrec(temp.nodes[0],temp.nodes[-1]))
temp = createLinkedList(10)
print('\nIterative BFT search on lined list')
print(search.BFSiter(temp.nodes[0],temp.nodes[-1]))
print('\nRandom Graph for topological sorts')
temp =createRandomDAGIter(5)
temp.printGraph()
print('\nKhans top sort on randomDAG Graph\n')
print(topsearch.Khans(temp))
print('\nmDFS on the same randomDAG Graph')
print(topsearch.mDFS(temp))
temp =createRandomCompleteWeightedGraphIter(5)
temp.printGraph()
print(maze.dijsktras(temp))
print(maze.astar(temp))
start = time.time()
temp =createRandomCompleteWeightedGraphIter(5000)
print("--- %s seconds ---" % (time.time() - start))
start = time.time()
maze.dijsktras(temp)
print("--- %s seconds ---" % (time.time() - start))
start = time.time()
maze.astar(temp)
print("--- %s seconds ---" % (time.time() - start))
