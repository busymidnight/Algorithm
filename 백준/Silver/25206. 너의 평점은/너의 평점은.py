
#과목평점
scores = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
score_sum = 0
answer = 0
#전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
for _ in range(20):
    sub, num, grade = map(str,input().split())
    if grade != "P":
        score = scores[grade] 
        answer += score*float(num)
        score_sum += float(num)
print(answer/score_sum)