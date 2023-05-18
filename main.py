from puzzle import *
from algorithems import *

"""
326117561 יהונתן פאשה
325427649 אביב קינן
325515401 שיר שווקה 
325427946 איתמר עצמוני 
"""

INPUT_FILE_LOCATION = "input.txt"
OUTPUT_FILE_LOCATION = "output.txt"

ALGORITHEMS = {
    1 : "IDS",
    2 : "BFS",
    3 : "A-STAR",
    4 : "IDA-STAR",
    5 : "DFS"
}

def load_from_input():
    with open(INPUT_FILE_LOCATION) as input_file:
        lines = input_file.readlines()
    algorithem = ALGORITHEMS[int(lines[0])]
    root = puzzle_state([int(x) for x in lines[2].split('-')])
    return algorithem, root

def save_to_output(path: list) -> None:
    with open(OUTPUT_FILE_LOCATION, 'w') as output_file:
        output_file.write(''.join(path))

def main():
    algorithem, root = load_from_input()    
    print(f"Welcome to AI Course Task 1\nImplemented by: Aviv, Itamar, Sheer and Yonatan")
    print(f"Chosen Algorithem: {algorithem}")
    print(f"Given state of the board:\n{root.toString()}")
    
    # Apply chosen algorithem:
    path = ['empty'] # list of moves
    if algorithem == 'IDS':
        path = IDS(root)
    
    if algorithem == 'BFS':
        path = BFS(root)

    if algorithem == 'A-STAR':
        path = AStar(root)
    
    if algorithem == 'DFS':
        path = DFS(root)
        
    if algorithem == 'IDA-STAR':
        save_to_output("we did not implement the IDA-STAR algorithm") 
        print('Done. we did not implement the IDA-STAR algorithm')
        
    if path == None or path==['failed']:
        save_to_output("it did not succeed") 
        print('Done. it did not succeed')
    else:
        save_to_output(path)
        print(f'Done. Results will be showed in {OUTPUT_FILE_LOCATION}')

if __name__ == "__main__":
    main()
