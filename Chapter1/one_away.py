def one_edit_replace(string1, string2):
    edited = False
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(string1, string2):
    edited = False
    i, j = 0, 0

    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if edited:
                return False
            edited = True
            if len(string1) < len(string2):
                j += 1
            elif len(string1) > len(string2):
                i += 1
        else:
            i += 1
            j += 1
    print(i,j)
    

    return True

def solution(string1, string2):
    if len(string1) == len(string2):
        return one_edit_replace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return one_edit_insert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return one_edit_insert(string1, string2)
    return False



if __name__ == '__main__':
    string1 = str(input()).rstrip()
    string2 = str(input()).rstrip()
    print(solution(string1, string2))