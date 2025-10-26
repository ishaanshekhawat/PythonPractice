def wrap(string, max_width):
    lines = []

    for i in range(0, len(string), max_width):
        lines.append(string[i:i+max_width])
    
    return '\n'.join(lines)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)