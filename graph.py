import random
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
        cost = abs(first.val-second.val)
        first.addEdge(cost,second)
        second.addEdge(cost,first)
    def removeUndirectedEdge(self,first,second):
        cost = abs(first.val-second.val)
        first.removeEdge(cost,second)
        second.removeEdge(cost,first)
    def adddirectedEdge(self,first,second):
        cost = abs(first.val-second.val)
        first.addEdge(cost,second)
    def removedirectedEdge(self,first,second):
        cost = abs(first.val-second.val)
        first.removeEdge(cost,second)
    def getAllNodes(self):
        return self.nodes
    def printGraph(self):
        print('This Graph has: ' + str(len(self.nodes)) + ' nodes.')
        print('The Connections are as follows:')
        for i in range(len(self.nodes)):
            print("\nnode: " + str(i) + ' has connections too:')
            for j in range(len(self.nodes[i].edges)):
                print('To node ' + str(self.nodes.index(self.nodes[i].edges[j][0])) + ' with a cost of '+ str(self.nodes[i].edges[j][1]))
            
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
print('Random grapth with five nodes\n')
temp = createRandomUnweightedGraphIter(5)
temp.printGraph()

def createLinkedList(n):
    graph = Graph()
    for i in range(n):
        graph.addNode(1)
    for i in(range(n)):
        if(i == 0):
            continue
        graph.adddirectedEdge(graph.nodes[i-1],graph.nodes[i])
    return graph
print('\nLinked list graph with 5 nodes\n')
temp = createLinkedList(5)
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
                    BFSrecsearch(queue.pop(0),stop)
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
search = GraphSearch()
temp = createLinkedList(10000)
print('\nRecursive BFT search on linked list')
print(search.BFSrec(temp.nodes[0],temp.nodes[-1]))
temp = createLinkedList(10000)
print('\n Iterative BFT search on lined list')
print(search.BFSiter(temp.nodes[0],temp.nodes[-1]))