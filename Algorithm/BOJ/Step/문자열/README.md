*(11654_아스키코드 문제 中)*

🗸 `ord(문자열)` = 아스키코드

🗸 `chr(아스키코드)` = 문자열


**# 알파벳 a-z를 원소로 가지는 리스트 생성하기**
```
alphabet = [chr(c) for c in range(ord('a'),ord('z')+1)]
```
**# 리스트 원소를 띄어쓰기로 구분하여 출력하기**

```
result = [1, 2, 3, 4, 5]
print(' '.join(map(str, result)))
```
1. 각 원소를 string으로 mapping
2. 각 원소를 `join`을 이용하여space bar로 이어붙임

---
*(2675_문자열반복 문제 中)*

**# 문자를 반복하고 싶을 땐 곱셈 연산자 사용**
```
print('a'*3)
=> aaa
```
**# join으로 문자열 연결 시 인자의 앞뒤를 바꾸면 연결되는 방향이 바뀐다**

abc를 각 원소 3회씩 반복하여 aaabbbccc를 출력할 때
1. 뒤로 붙이며 반복
```
string='abc'
result = ''
for char in string:
    result=''.join([result, char*int(repeat_num)])
```
출력 결과
```
aaabbbccc
```
2. 앞으로 붙이며 반복
```
string='abc'
result = ''
for char in string:
    result=''.join([char*int(repeat_num),result])
```
출력 결과
```
cccbbbaaa
```