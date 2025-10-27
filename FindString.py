def count_substring(string, sub_string):
    count1 = 0
    for i in range(len(string)):
        if sub_string[0] == string[i]:
            if sub_string == string[i:len(sub_string)+i]:
                count1 += 1

    return count1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)