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
    print(val.toString())
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
    pass
