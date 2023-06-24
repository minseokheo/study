def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계
    print(new_id)
    
    i = 0
    while i < len(new_id): # 2단계
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            i += 1
        else:
            if i+1 == len(new_id):
                new_id = new_id[:i]
            else:
                new_id = new_id[:i] + new_id[i+1:]
    print(new_id)
    
    if len(new_id) >= 2: # 3단계
        i = 1
        while i < len(new_id):
            if new_id[i-1] == '.' and new_id[i] == '.':
                if i+1 == len(new_id):
                    new_id = new_id[:i]
                else:
                    new_id = new_id[:i] + new_id[i+1:]
            else:
                i += 1
    print(new_id)
    
    if len(new_id) >= 2: # 4단계
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:len(new_id)-1]
    elif len(new_id) == 1:
        if new_id[0] == '.':
            new_id = ''
    print(new_id)
    
    if len(new_id) == 0: # 5단계
        new_id = 'a'
    print(new_id)
    
    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:len(new_id)-1]
    print(new_id)
    
    if len(new_id) <= 2: # 7단계
        while len(new_id) < 3:
            new_id += new_id[-1]
    print(new_id)
    
    answer = new_id       
            
    return answer