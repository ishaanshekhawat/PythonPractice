def split_and_join(line):
    ls = line.split()
    jn = '-'.join(ls)
    return jn

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)