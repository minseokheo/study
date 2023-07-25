def solution(files):
    answer = []
    file_list = []
    
    for file in files:
        head = ""
        number = ""
        tail = ""
        for i in range(len(file)):
            if file[i].isdigit() and len(head) == 0:
                head = file[:i]
                number += file[i]
            elif file[i].isdigit() and len(tail) == 0:
                number += file[i]
            elif len(head) != 0 and len(number) != 0:
                tail += file[i]
        file_list.append([head, number, tail])
    file_list.sort(key = lambda x: (x[0].lower(), int(x[1])))
    
    for f in file_list:
        a = ""
        for i in range(3):
            a += f[i]
        answer.append(a)
    return answer