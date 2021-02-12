#combinations 이용 풀이. permutations + set 으로 풀려 하였으나 시간초과.

from itertools import combinations

l, c = map(int, input().split())
arr = list(input().split()) #후보 알파벳들.
newarr = list(combinations(arr, l)) #후보 알파벳 이용 조합.
vowel = ['a', 'e', 'i', 'o', 'u'] #모음들.

result = []
for str_val in newarr:
    check_val = set(str_val) - set(vowel) #check_val = 후보 단어 set - 모음 단어 set
    if len(check_val) == len(str_val) or len(check_val) < 2: #check_val의 길이가 str_val과 같으면 모음이 없다는것.
                                                             #2보다 작으면 자음이 2개보다 적다는것. 이 두경우는 후보에서 제외.
        continue
    #답에 넣을 놈들.
    str_val = sorted(list(str_val)) #combinations은 투플이므로 list로 변경후 정렬해줌.
    str_val = "".join(str_val) #문자열로 변경하여 답에 삽입.
    result.append(str_val)

result.sort() #답 순서 정렬

for i in result:
    print(i)