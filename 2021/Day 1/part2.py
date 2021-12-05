import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r").readlines()

def main():
    last = 0
    lastThree = []
    count = -1
    for i, data in enumerate(input):
        lastThree.append(int(data))
        if i in [0, 1]:
            continue
        sum = lastThree[-1] + lastThree[-2] + lastThree[-3]
        if last < sum:
            count += 1
        last = sum
    print(count)

if __name__ == "__main__": main()