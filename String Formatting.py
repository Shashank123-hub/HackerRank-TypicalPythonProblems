def print_formatted(number):
    w = len("{0:b}".format(number))   #width defined to format numbers while printing
    for i in range(1,number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=w))       #formatting extra characters from all formats

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
