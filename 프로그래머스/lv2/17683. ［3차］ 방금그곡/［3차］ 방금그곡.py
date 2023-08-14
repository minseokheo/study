# 최초의 문제해결을 위해서는 musicinfos의 리스트안의 문자열을 나눠서 뜯어야겠다고 생각했습니다.
# 시가의 흐름을 기준으로 악보를 재구성 한 후(딕셔너리로 재구성하여 해당하는 악보에 대한 제목을 바로 알 수 있도록)
# m에 맞는 음악을 출력하는 방식으로 코딩 해 보겠습니다.
def solution(m, musicinfos):
    answer = ''
    music_dict = {}
    for musicinfo in musicinfos:
        # 한 곡의 정보를 정리하기 위해 나누기
        start_time, finish_time, title, music = musicinfo.split(',')
        
        # 시간을 계산해서 얼마동안 음악이 흘러나왔는지 계산
        if start_time[:2] == finish_time[:2]:
            running_time = int(finish_time[-2:]) - int(start_time[-2:])
        elif start_time[:2] < finish_time[:2]:
            running_time = int(finish_time[-2:]) + (int(finish_time[:2]) - int(start_time[:2])) * 60 - int(start_time[-2:])
        else:
            running_time = int(finish_time[-2:]) + (int(finish_time[:2]) + 24 - int(start_time[:2])) * 60 - int(start_time[-2:])
        
        # 흘러나온 시간에 따라 악보 재구성
        music_sheet = ""
        l = len(music)
        time = 0
        index = 0
        ## 최초에 제출 했을 때 80%만 통과하였고 다른 사람들 질문을 참고하니 제 코드로 돌리면
        ## 테케 4번에 추가된 것과 같이 악보에 추가해줄때 마지막 #은 처리하지 못하여서 개선하였습니다.
        ## 다른 답안을 참고하니 그냥 C#과 같은 음계를 c로 치환하였고 다음부터는 이런 방법도 생각해내야겠습니다.
        while time != running_time:
            music_sheet += music[index%l]
            if music[(index+1)%l] == '#':
                music_sheet += '#'
                index += 1
            time += 1
            index += 1
            """
            if music[index%l] == '#':
                music_sheet += music[index%l]
            else:
                music_sheet += music[index%l]
                time += 1
            index += 1
            """
        music_dict[music_sheet] = [title, running_time]
        
    # 악보에 따른 딕셔너리로 제목을 맞추어 주었고 들은 멜로디로 악보에서 찾아줍니다.
    max_time = -1
    m_l = len(m)
    for k, v in music_dict.items():
        # 이런 식으로 찾으면 C#과 같은 #을 해결 못함(테스트 케이스 3번) -> 이중 for문을 돌려서 찾을 생각
        """
        if m in k:
            if len(answer) == 0:
                answer = v[0]
                max_time = v[1]
            else:
                if max_time < v[1]:
                    answer = v[0]
                    max_time = v[1]
        """
        k_l = len(k)
        for i in range(k_l):
            # 시간복잡도를 줄이기 위해 찾는 멜로디의 수가 더 길게 되면 더 이상 안 찾아도 되기 때문에 for문을 탈출
            if m_l > len(k[i:]):
                break
            
            if k[i] == m[0]:
                for m_index in range(1, m_l):
                    i += 1
                    if k[i] != m[m_index]:
                        break
                    if m_index == m_l-1:
                        if i+1 < k_l:
                            if k[i+1] != "#":
                                if len(answer) == 0:
                                    answer = v[0]
                                    max_time = v[1]
                                else:
                                    if max_time < v[1]:
                                        answer = v[0]
                                        max_time = v[1]
                        ## 이 부분 추가 해 주었습니다.
                        elif i+1 == k_l:
                            if len(answer) == 0:
                                answer = v[0]
                                max_time = v[1]
                            else:
                                if max_time < v[1]:
                                    answer = v[0]
                                    max_time = v[1]
    if len(answer) == 0:
        answer = "(None)"
    return answer