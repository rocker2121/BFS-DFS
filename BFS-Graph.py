#!/usr/bin/env python
# coding: utf-8

# In[1]:


class graph:
    def __init__(self):
        self.bigl=[]
    def addvertex (self,vert):
        self.bigl.append([vert,{}])
    def addedge (self,vertfro,vertto,weight=0):
        for i in range(len(self.bigl)):
            if self.bigl[i][0] ==vertfro:
                self.bigl[i][1][vertto]=weight
            elif self.bigl[i][0] ==vertto:
                self.bigl[i][1][vertfro]=weight
    def getgraph(self):
        return self.bigl
        
    def __iter__(self):
        return iter(self.bigl)
        


# In[ ]:





# In[29]:


class graph1:
    def __init__(self):
        self.bigl={}
    def addvertex (self,vert):
        self.bigl[vert]={}
    def addedge (self,vertfro,vertto,weight=0):
        for i in range(len(self.bigl)):
            self.bigl[vertfro][vertto]=weight
            self.bigl[vertto][vertfro]=weight
           
    def getgraph(self):
        return self.bigl
        
    def __iter__(self):
        return iter(self.bigl)


# In[ ]:





# In[30]:


g=graph1()


# In[31]:


for i in range(8):
    g.addvertex(i)


# In[32]:


g.addedge(2,3,9)


# In[33]:


g.addedge(4,3,90)


# In[34]:


g.addedge(1,2,10)


# In[35]:


g.addedge(4,5,8)


# In[36]:


g.addedge(5,6,70)


# In[37]:


g.addedge(6,7,5)


# In[38]:


g.addedge(0,1,4)


# In[39]:


g.addedge(1,7,5)


# In[43]:


g.getgraph()


# In[45]:


for gus in g:
    print (gus)


# In[26]:


import random

random.randint(0,10)


# In[54]:


a=[9,8,7]


# In[55]:


a.pop(0)


# In[56]:


a


# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:


g.getgraph()[3]


# In[48]:


d={"a":3,"b":4}
for i in d.keys():
    print(i)


# In[ ]:





# In[46]:


len(g.getgraph())


# In[75]:


def n_bfs(graphs):
    x=random.randint(0,len(graphs.getgraph())-1)
    q=[]
    q.append(x)
    visited=[]
    while len(visited)<len(graphs.getgraph()):
     
        tovis=q[0]
        if tovis not in visited:
            dtc=graphs.getgraph()[tovis]
            for i in dtc.keys():
                if i not in q:
                    q.append(i)


            visited.append(tovis)
            q.pop(0)
        else:
            q.pop(0)
            
        
    
    return visited
        
        
            
            
    


# In[76]:


n_bfs(g)


# In[61]:


g.getgraph()[1]


# In[66]:


g.getgraph()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


def bfs (graphs):
    queue=[]
    for item in graphs:
        if item[0] not in queue:
            queue.append(item[0])
        for kitem in item[1]:
            if kitem not in queue:
                queue.append(kitem)
    return (queue)
    
            
        
        
        
        
        


# In[ ]:


def dfs (graphs):
    queue=[]
    for item in graphs:
        if item[0] not in queue:
            queue.append(item[0])
        for kitem in item[1]:
            if kitem not in queue:
                queue.append(kitem)
    return (queue)
    
            
        
        
        
        
        


# In[15]:


bfs(g)


# In[60]:


import difflib

case_a = 'h'
case_b = 'hat'

output_list = [li for li in difflib.ndiff(case_a, case_b) if li[0] != ' ']


# In[61]:


output_list


# In[55]:


difflib.ndiff(case_a, case_b)


# In[62]:


from itertools import combinations


# In[ ]:


list(combinations(arr, r))


# In[ ]:





# In[67]:


def Word_ladder(beginword,endword,wordlist):
    f=graph()
    for word in wordlist:
        f.addvertex(word)
    l2=list(combinations(wordlist, 2))
    for l in l2:
        output_list = [li for li in difflib.ndiff(l[0], l[1]) if li[0] != ' ']
        if len(output_list)==2:
            f.addedge(l[0],l[1],1)
    print (f.getgraph())
    return (bfs(f))
        


# In[70]:


beginWord = "hit",
endWord = "cog",
wordList = ["hit","hot","dot","dog","lll","lot","log","cog","ooo","ppp"]


# In[71]:


Word_ladder(beginWord,endWord,wordList)


# In[ ]:




