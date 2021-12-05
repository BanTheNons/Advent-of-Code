import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r").readlines()

def main():
    last = 0
    count = -1
    for data in input:
        if last < int(data):
            count += 1
        last = int(data)
    print(count)

if __name__ == "__main__": main()