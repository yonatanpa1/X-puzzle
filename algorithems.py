from puzzle import *
from queue import LifoQueue, PriorityQueue


#IDS algorithm implementation using DFS_
def IDS(root: puzzle_state,max_depth = 1000):
    #Loop over all possible depth limits until found a solution or limit is max_depth
    for d_limit in range(max_depth):
        visited=set()
        # Apply DFS with the current depth limit
        p=DFS_(root, d_limit, visited)
        if p is not None:
            return p
    return None

def DFS_(root:puzzle_state,limit:int,seen:set=set()):
    if root.id in seen:
        return None
    seen.add(root.id)

    if root.isGoal():
        return []

    #If the current depth limit is reached so stop and return None
    if limit==0:
        return None
    #iterates over moves from the current state and performs a depth limit DFS 
    for son in root.get_possible_moves():
        son[0].parent=root
        son[0].moveFromParent=son[1]
        result=DFS_(son[0],limit-1,seen)
        if result is not None:
            return [son[1]]+result

    return None

def DFS(root: puzzle_state):
    
    def dive(node: puzzle_state, seen: list):
        #for the seen moves
        seen.append(node.id)
        if node.isGoal():
            return node #return the goal sate 
        #Aplay the DFS algorithm
        for state_son in node.get_possible_moves():
            if not (state_son[0].id in seen):
                state_son[0].parent = node
                state_son[0].moveFromParent = state_son[1]
                #recursive for depth
                val = dive(state_son[0], seen)
                if val:
                    return val

    root.parent = None
    seen = []
    try:
        val = dive(root, seen)    
    except:
        print(f'too hard... scanned {len(seen)} diffrent states without success')
        return ['failed']
    # val is the goal, now let's get the path
    path = []
    while val.parent is not None:
        path.append(val.moveFromParent)
        val = val.parent
    path.reverse()
    return path
    


def BFS(root: puzzle_state):
    q = []
    seen = []
    seen.append(root.id)
    root.parent = None
    root.moveFromParent = None
    q.append(root)
    while q:
        val = q.pop(0)
        if val.isGoal():
            print(val.toString())
            break
        for state_son in val.get_possible_moves():
            if not (state_son[0].id in seen):
                seen.append(state_son[0].id)
                state_son[0].parent = val
                state_son[0].moveFromParent = state_son[1]
                q.append(state_son[0])
    
    # val is the goal, now let's get the path
    path = []
    while val.parent is not None:
        path.append(val.moveFromParent)
        val = val.parent
    path.reverse()
    return path



def AStar(root: puzzle_state):
    open_list=PriorityQueue() 
    closed_list=list()
    root.g=0
    root.h=manhattan_dis(root.current_state,root.goal_state,root.n)
    root.f=root.h
    #insert root with priority root.f
    open_list.put((root.f,root))  
    
    while not open_list.empty():
        #get the node with the lowest priority in the open list-priority Queue
        current=open_list.get()[1]
        
        if current.isGoal():
            #found the goal 
            path=[]
            #calculate the path for the goal
            while current.parent is not None:
                path.append(current.moveFromParent)
                current=current.parent
            #the correct order    
            return path[::-1] 
        
        closed_list.append(current.id)
        
        for child,move in current.get_possible_moves():
            if child.id in closed_list:
                #child is in closed list so continue
                continue
            
            if any(child.id==item[1].id for item in open_list.queue):
                open_list.queue=[(f, node) for (f,node) in open_list.queue if node.id !=child.id]
            #calculate f and h function for the child
            child.g=current.g+1#manhattan_dis(current.current_state, child.current_state)
            child.h=manhattan_dis(child.current_state, child.goal_state,root.n)
            child.f=child.g+child.h
            child.parent=current
            child.moveFromParent=move
            
            #add child to open list with priority f
            open_list.put((child.f, child))
         
    #no path found so return None           
    return None  

def manhattan_dis(s1,s2,n):
    #Calculates the Manhattan distance 
    dis = 0
    for i in range(len(s1)):
        if s1[i]!=0:#Is not the empty tile
            row1=i//n
            col1=i%n
            #Find the index of s1 in s2
            index=s2.index(s1[i])
            row2=index//n
            col2=index%n
            # Calculate the Manhattan distance of the current tile
            dis+=abs(row1-row2)+abs(col1-col2)
    return dis





