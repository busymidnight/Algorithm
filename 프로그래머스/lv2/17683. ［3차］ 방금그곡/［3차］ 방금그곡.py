def solution(m, musicinfos):
    m = m.replace("D#","d").replace("C#","c").replace("F#","f").replace("A#","a").replace("G#","g")
    answer = (0,'')
    for info in musicinfos:
        splitted = info.split(",")
        start_time, end_time = splitted[0], splitted[1]
        times = int(end_time[-2:]) - int(start_time[-2:])
        if start_time[:2] != end_time[:2]:
            times += 60*(int(end_time[:2])-int(start_time[:2]))
        raw_melody = splitted[3].replace("D#","d").replace("C#","c").replace("F#","f").replace("A#","a").replace("G#","g")
        
        melody = (raw_melody * (times // len(raw_melody) + 1))[:times]
        if m in melody and answer[0] < times:
            answer = (times, splitted[2])
                

    if answer[0] == 0:
        return '(None)'
    else:
        return answer[1]