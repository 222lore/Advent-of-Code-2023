def part1(file):
    line = file.readline()#[:-1]

    while line != "":


        line = file.readline()

    return 0 


def part2(file):
    line = file.readline()

    while line != "":


        line = file.readline()

    return 0 


def main():
    print("Part 1: " + str(part1(open("../input/Day01.txt", "r"))))
    print("Part 2: " + str(part2(open("../input/Day01.txt", "r"))))


if __name__ == "__main__": main()