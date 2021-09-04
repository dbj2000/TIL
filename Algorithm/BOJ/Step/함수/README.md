*(155962_정수N개의합 문제 中)*

**# 1차원 list 원소의 합은 for문보다 sum()이 빠르다**

난수를 생성하여 list를 생성한 후 수행시간을 비교해 보았다.
```
import numpy as np
data=np.random.rand(100)
```
🗸 `sum()` 내장함수 이용
```
def solve(a):
    return sum(a)
```
🗸 `for문` 이용
```
result = 0
for x in data:
    result += x
```
전체 코드
```
# 1. sum()사용
start = timeit.default_timer()
result = solve(data)
stop = timeit.default_timer()
print(f"sum 수행시간 : {stop - start:0.6f}")

# 2. for문 사용
start = timeit.default_timer()
result = 0
for x in data:
    result += x
stop = timeit.default_timer()
print(f"for 수행시간 : {stop - start:0.6f}")
```
실행 결과
```
sum 수행시간 : 0.000015
for 수행시간 : 0.000046
```
주의할 점

🗸 2차원 이상의 list의 경우 `sum()`을 사용하면 TypeError가 발생한다.

---
*(4673_셀프넘버 문제 中)*

**# 각 자리수의 합을 구할 땐 문자열인 상태에서!**

정수인 상태에서 각 자리수의 합을 반환하는 함수를 작성했는데, 그것보다 str로 바꾼 후 각 자리의 char을 돌며 그때마다 int로 바꿔 더해주는 것이 코드도 깔끔하고 간결하다.

```
# int인 상태에서 자리수 합
def d(n):
    sum = 0
    while(n!=0):
        sum += n%10
        n = n//10
    return sum
```
```
# str인 상태에서 자리수 합
for n in str(num):
    num += int(n)
```
**# set vs list**
- 중복을 제거하고 싶은 경우 list보다 set자료형이 적합
- set의 `'-'` 연산자로 차집합을 구할 수 있음
- 파이썬 내장 함수 `sorted`  **vs** list객체 내의 `sort` 함수
    - sorted는 정렬된 **새로운 객체**를 생성
    - list.sort()는 해당 **리스트 자체의 순서를 바꿈**
