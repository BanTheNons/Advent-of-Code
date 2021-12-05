import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r").readlines()

def main():
    horizontal = 0
    depth = 0
    aim = 0
    for data in input:
        if data.startswith("forward"):
            horizontal += int(data.split(" ")[1])
            depth += int(data.split(" ")[1]) * aim
        elif data.startswith("up"):
            aim -= int(data.split(" ")[1])
        elif data.startswith("down"):
            aim += int(data.split(" ")[1])
    print(horizontal * depth)

if __name__ == "__main__": main()