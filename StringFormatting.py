def octal(n):
    octal = ""
    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n = n // 8
    return octal

def hexa(n):
    hexa = ""
    while n > 0:
        rem = n % 16
        if rem == 10:
            hexa = 'A' + hexa
        elif rem == 11:
            hexa = 'B' + hexa
        elif rem == 12:
            hexa = 'C' + hexa
        elif rem == 13:
            hexa = 'D' + hexa
        elif rem == 14:
            hexa = 'E' + hexa
        elif rem == 15:
            hexa = 'F' + hexa
        else:
            hexa = str(rem) + hexa
        n = n // 16
    return hexa

def binary(n):
    binary = ""
    while n > 0:
        rem = n % 2
        binary = str(rem) + binary
        n = n // 2
    return binary

def print_formatted(number):
    width = len(binary(number))  # width of the largest binary number
    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            octal(i).rjust(width),
            hexa(i).rjust(width),
            binary(i).rjust(width)
        )
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)