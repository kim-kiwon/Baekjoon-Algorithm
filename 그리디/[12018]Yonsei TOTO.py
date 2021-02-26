#그리디 & 정렬
n, m = map(int, input().split()) #n : 과목수. m: 마일리지수

can_m = [] #각 과목 수강신청위한 최소점수리스트.
for i in range(n):
    p, l = map(int, input().split()) #신청수. 정원수.
    person = list(map(int, input().split())) #신청점수 리스트.
    person.sort(reverse = True) #사람들 점수 역순 정렬
    can_m.append(person[l-1] if p >= l else 1)
    #신청수 < 정원수면 1을. 신청수 > 정원수면 정원수 번째 can_m에 삽입.

can_m.sort() #최소점수 낮은순 정렬.

count = 0
for i in can_m:
    m -= i
    count += 1
    if m < 0:
        count -= 1
        break

print(count)