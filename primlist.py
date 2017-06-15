class Graph:
 
    def __init__(self,vertices,edges):
        self.V= vertices #No. of vertices
        self.E= edges
        self.graph = [] # default dictionary to store graph
         
  
    # function to add an adjacency list to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
 
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
    def printMST(self,parent,n,graph,key):
    
        print("Edge   Weight");
        for i in range(1,self.V):
            print (str(parent[i])+" - "+ str(i)+"    "+str(key[i]));
    
    def primmst(self):
        parent=[]
        key=[]
        mst=[]
        u=-1
        result =[] #This will store the resultant MST

        self.graph=sorted(self.graph, key=lambda item:item[0])
 
        for i in range(self.V):
            key.append(999999)
            mst.append(False)
            parent.append(-1)
       
        key[0]=0 
        
        
        
        mini=999999
        mini_index=-1
        for i in range(self.V):
            u=self.findmin(key,mst)
            #print u
            mst[u]=True
            minw=999999
            min_w=-1
            for j in range(self.E):
                if(self.graph[j][0]==u):
                    if(mst[(self.graph[j][1])]==False):
                        if(self.graph[j][2]<key[self.graph[j][1]]):
                            key[self.graph[j][1]]=self.graph[j][2]
                            min_w=j
                            #print minw,min_w
                            parent[self.graph[min_w][1]]=u
                            key[self.graph[min_w][1]]=self.graph[min_w][2]
            
                            #print parent,key
                if(self.graph[j][1]==u):
                    if(mst[(self.graph[j][0])]==False):
                        if(self.graph[j][2]<key[self.graph[j][0]]):
                            key[self.graph[j][0]]=self.graph[j][2]
                            min_w=j
                            #print minw,min_w
                            parent[self.graph[min_w][0]]=u
                            key[self.graph[min_w][0]]=self.graph[min_w][2]
            
                            #print parent,key
                       

           
            
        # print the contents of result[] to display the built MST
        print "Following are the edges in the constructed MST"
       
        self.printMST(parent,self.V,self.graph,key) 
 
#g = Graph(9,14)
#g.addEdge(0,1,4);
#g.addEdge(0,7,8);
#g.addEdge(1,2,8);
#g.addEdge(1,7,11);
#g.addEdge(2,3,7);
#g.addEdge(2,8,2);
#g.addEdge(2,5,4);
#g.addEdge(3,4,9);
#g.addEdge(3,5,14);
#g.addEdge(4,5,10);
#g.addEdge(5,6,2);
#g.addEdge(6,7,1);
#g.addEdge(6,8,6);
#g.addEdge(7,8,7);


g = Graph(6,9)
g.addEdge(0,1,7);
g.addEdge(0,5,8);
g.addEdge(1,5,3);
g.addEdge(1,2,6);
g.addEdge(2,5,4);
g.addEdge(2,4,2);
g.addEdge(2,3,5);
g.addEdge(3,4,2);
g.addEdge(4,5,3);

 
g.primmst()
