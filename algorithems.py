from puzzle import *

def IDS(root: puzzle_state):
    pass

def BFS(root: puzzle_state):
    q = []
    seen = []
    seen.append(root.id)
    root.parent = 'root'
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
    while val.parent != 'root':
        path.append(val.moveFromParent)
        val = val.parent
    path.reverse()
    return path

def AStar(root: puzzle_state):
    pass

def IDAStar(root: puzzle_state):
    pass

def DFS(root: puzzle_state):
    
    def dive(node: puzzle_state, seen: list):
        seen.append(node.id)
        if node.isGoal():
            return node
        for state_son in node.get_possible_moves():
            if not (state_son[0].id in seen):
                state_son[0].parent = node
                state_son[0].moveFromParent = state_son[1]
                val = dive(state_son[0], seen)
                if val:
                    return val

    root.parent = 'root'
    seen = []
    try:
        val = dive(root, seen)    
    except:
        print(f'too hard... scanned {len(seen)} diffrent states without success')
        return ['failed']
    # val is the goal, now let's get the path
    path = []
    while val.parent != 'root':
        path.append(val.moveFromParent)
        val = val.parent
    path.reverse()
    return path
    
