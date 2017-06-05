class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
         
  
    # function to add an adjacency list to graph
    def addEdge(self,w1,w2,w3,w4,w5):
        self.graph.append([w1,w2,w3,w4,w5])
 
    # A utility function to find set of an element i
    # (uses path compression technique)

    def findmin(self,key,mst):
        
        mini=999999
        min_index=-1
        for i in range(self.V):
            if((mst[i]==False) and key[i]<mini):
                mini=key[i]
                min_index=i
        return min_index
 
    # The main function to construct MST using Kruskal's algorithm
    def printMST(self,parent,n,graph):
    
        print("Edge   Weight");
        for i in range(1,self.V):
            print (str(parent[i])+" - "+ str(i)+"    "+str(graph[i][parent[i]]));
    
    def primmst(self):
        parent=[-1,-1,-1,-1,-1]
        key=[]
        mst=[]
        u=-1
        result =[] #This will store the resultant MST
 
        for i in range(self.V):
            key.append(999999)
            mst.append(False)

       
        key[0]=0
        
        

        for i in range(self.V):

            u=self.findmin(key,mst)
            #print u
            mst[u]=True
            #print mst
            for j in range(self.V):
                #print j
                if(mst[j] == False):
                    if(u!=j):
                        if(self.graph[u][j]!=0):
                            #print "yes"
                            #print u
                            #print j
                            #print "---"
                            if(self.graph[u][j]<key[j]):
                                parent[j]=u
                                key[j]=self.graph[u][j]
                            else:
                                continue
                                
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

           
            
        # print the contents of result[] to display the built MST
        print "Following are the edges in the constructed MST"
       
        self.printMST(parent,self.V,self.graph) 
 
g = Graph(5)
g.addEdge(0, 2, 0, 6, 0)
g.addEdge(2, 0, 3, 8, 5)
g.addEdge(0, 3, 0, 0, 7)
g.addEdge(6, 8, 0, 0, 9)
g.addEdge(0, 5, 7, 9, 0)
 
g.primmst()
