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
---
*(5622_다이얼 문제 中)*

🗸 `enumerate`
* 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때
* 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
```
alphabet = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

for i, alpha in enumerate(alphabet):
    print(i, alpha)
```
출력 결과
```
0 abc
1 def
2 ghi
3 jkl
4 mno
5 pqrs
6 tuv
7 wxyz
```
---
*(2941_크로아티아 알파벳 문제 中)*

**# `map(함수, 리스트)`을 사용하여 반복문 한 줄로 줄이기**

Ex) 리스트의 모든 요소를 정수로 변환할 때
```
a = [1.2, 2.5, 3.7, 4.6]

# 1. for문 이용
for i in range(len(a)):
     a[i] = int(a[i])

# 2. map이용
a = list(map(int, a))
```
문제에 적용
```
term = 'ddz=z='
map(term.count,['-','=','lj','nj','dz='])

# 결과 : [0, 2, 0, 0, 1]
```
* 입력받은 단어에서 list속의 요소를 카운트 한다.
* term.count('-'), term.count('='), ... 수행하여 list로 반환
