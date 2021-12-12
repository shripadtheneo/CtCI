def solution(string):
    result = ''
    for char in string:
        if char == ' ':
            result += '%20' 
        else:
            result += char

    return result


if __name__ == '__main__':
    string = str(input()).rstrip()
    print(solution(string))
