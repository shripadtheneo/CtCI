from collections import Counter

def solution(string1, string2):
    if len(string1) != len(string2):
        return False
    
    counter = Counter()

    for char in string1:
        counter[char] += 1

    for char in string2:
        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    print(solution(string1, string2))