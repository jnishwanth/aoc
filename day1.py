from os.path import basename
infile = './input/' + basename(__file__).replace('.py', '')

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9n"
}

def solve(line):
    num1=None
    num2=None
    for i in range(len(line)):
        if line[i].isdigit():
            num1=line[i]
            break
    for i in range(len(line)-1,-1,-1):
        if line[i].isdigit():
            num2=line[i]
            break
    return(num1+num2)

def replace(line):
    for k, v in str2num.items():
        line = line.replace(k, v)
    return line

inp = open(infile).read().split()
ans1 = sum([int(solve(line)) for line in inp])
ans2 = sum([int(solve(replace(line))) for line in inp])
print(ans1, ans2)