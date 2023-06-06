from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutations = list(permutations(user_id, len(banned_id)))
    ban_list = []

    for users in user_permutations:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_list:
                ban_list.append(users)

    return len(ban_list)