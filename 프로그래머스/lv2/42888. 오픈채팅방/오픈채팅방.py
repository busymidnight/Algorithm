def solution(record):
    answer = []
    enter_stack = []
    uid_stack = dict()

    for rec in record:
        rec_split = rec.split(" ")
        command = rec_split[0]
        uid = rec_split[1]
        if command == "Enter":
            username = rec_split[2]
            enter_stack.append(rec)
            uid_stack[uid] = username
        elif command == "Change":
            username = rec_split[2]
            uid_stack[uid] = username
        else:
            enter_stack.append(rec)

    for enter in enter_stack:
        enter_split = enter.split(" ")
        command = enter_split[0]
        uid = enter_split[1]
        username = uid_stack[uid]
        if command == "Enter":
            answer.append(username+"님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(username+"님이 나갔습니다.")
    return answer