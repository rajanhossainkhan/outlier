import sys

sys.setrecursionlimit(5000)

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
    
    tower_of_hanoi(n - 1, source, auxiliary, destination)

    print(f"Mode disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, destination, source)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')