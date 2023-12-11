from os.path import basename
infile = './input/' + basename(__file__).replace('.py', '')

inp = open(infile).read().split('\n')

# pros = [[game[0], game[1:].split(';')] for game in line.split(':') for line in inp]
print(pros)