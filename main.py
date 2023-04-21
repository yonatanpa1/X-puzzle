from puzzle import *
from algorithems import *

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

    if algorithem == 'IDA-STAR':
        path = IDAStar(root)
    
    if algorithem == 'DFS':
        path = DFS(root)

    save_to_output(path)
    print(f'Done. Results will be showed in {OUTPUT_FILE_LOCATION}')

if __name__ == "__main__":
    main()
