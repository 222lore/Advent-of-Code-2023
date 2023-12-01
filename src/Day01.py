def part1(file):
    line = file.readline()

    sum = 0
    while line != "":
        num = ""

        for c in line:
            if c.isdigit():
                num += c 
                break 
        
        for c in line[::-1]:
            if c.isdigit():
                num += c 
                break 
        
        sum = sum + int(num)

        line = file.readline()

    return sum


def part2(file):
    line = file.readline()

    forward = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    reverses = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]

    sum = 0
    while line != "":
        first = ""
        last = ""
        curs = []

        for c in line:
            if first != "":
                break 

            if c.isdigit():
                first = str(c) 
                break

            for i in range(len(curs)):
                curs[i] += c.strip()
            curs.append(c.strip())
            
            for x in curs:
                i = 1
                for y in forward:
                    if x == y:
                        first = str(i)
                    i += 1     

        curs = []

        for c in line[::-1]:
            if last != "":
                break 

            if c.isdigit():
                last = str(c) 
                break

            for i in range(len(curs)):
                curs[i] += c.strip()
            curs.append(c.strip())

            for x in curs:
                i = 1
                for y in reverses:
                    if x == y:
                        last = str(i)
                        break  
                    i += 1

        sum += int(first + last)

        line = file.readline()

    return sum


def main():
    f1 = open("../input/Day01.txt", "r")
    f2 = open("../input/Day01.txt", "r")
    print("Part 1: " + str(part1(f1)))
    print("Part 2: " + str(part2(f2)))


if __name__ == "__main__": main()