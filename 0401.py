## 3-1

1.
False
True
False
True
True
False

2. 3

3. 1(a)
   2(o)
   3(a)

4.
int
int

a > b
format(a, b)
a < b
format(a, b)


## 3-2

1. 12  5  12

2. if 10 < x < 20:

3.
int(str_input) % 12
birth_year == 0:
birth_year == 1:
birth_year == 2:
birth_year == 3:
birth_year == 4:
birth_year == 5:
birth_year == 6:
birth_year == 7:
birth_year == 8:
birth_year == 9:
birth_year == 10:
birth_year == 11:

## 3장 도전문제

1.
import datetime

str_input = input("입력> ")

if "안녕" in str_input:
	print("안녕하세요.")
elif "몇 시" in str_input:
	now = datetime.datetime.now()
	print(f"지금은 {now.hour}시 입니다.")
else:
	print(str_input)
2.
str_input = input("정수를 입력해주세요> ")
num= int(str_input)

if num % 2 != 0 :
    print(f"{num}은(는) 2로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print(f"{num}은(는) 2로 나누어 떨어지는 숫자입니다.")

if num % 3 !=0 :
    print(f"{num}은(는) 3로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print(f"{num}은(는) 3로 나누어 떨어지는 숫자입니다.")
if num % 4 !=0 :
    print(f"{num}은(는) 4로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print(f"{num}은(는) 4로 나누어 떨어지는 숫자입니다.")
if num % 5 != 0 :
    print(f"{num}은(는) 5로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print(f"{num}은(는) 5로 나누어 떨어지는 숫자입니다.")

##4-1 확인문제

1.
[0, 1, 2, 3, 4, 5, 6, 7] [0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 10]
[0, 1, 2, 0, 4, 5, 6, 7]
[0, 1, 2, 4, 5, 6, 7]
[0, 1, 3, 4, 5, 6, 7]
[]

2. number >= 100:

3. 
for number in numbers:
    if number % 2 == 0:
        print(number, "는 짝수입니다.")
    else:
        print(number, "는 홀수입니다.")
for number in numbers:
    digit_count = len(str(number))
    print(number, "는", digit_count, "자릿수입니다.")

4. (number+2) % 3

5. i * 2 + 1

##4-2 확인문제

1.
dict_a = {}

dict_a['name'] = '구름'

print(dict_a)

2.
for pet in pets:
    print(pet["name"], str(pet["age"]) + "살")

3.
# 딕셔너리에 해당 숫자가 이미 있는지 확인하고, 있으면 값을 1 증가시킵니다.
    if number in counter:
        counter[number] += 1
    else:
        # 해당 숫자가 처음 등장하면 새로운 키로 추가하고 값을 1로 설정합니다.
        counter[number] = 1

4.
for key in character:
    if isinstance(character[key], dict):
        for item_key, item_value in character[key].items():
            print(f"{item_key} : {item_value}")
    elif isinstance(character[key], list):
        for item in character[key]:
            print(f"{key} : {item}")
    else:
        print(f"{key} : {character[key]}")

## 4-3 확인문제

1. [4, 5] [7, 6, 5, 4, 3, 2, 1] range(3, 10, 3)

2. for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

3.
sum_value = 0

while True:
    sum_value += i
    if sum_value > limit:
        break
    i += 1

4.
range(1, 101):
if i * j > max_value:
        max_value = i * j
        a = i
        b = j

##4-4 확인문제

1. 2, 4

2. []
range(1, 101):

## 4장 도전문제

1.
numbers = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

number_counts = {}

for number in numbers:
    if number in number_counts:
        number_counts[number] += 1
    else:
        number_counts[number] = 1


print("사용된 숫자의 종류는 {}개입니다.".format(len(number_counts)))

print(number_counts)
2.
# 염기 서열을 입력받습니다.
sequence = input("염기 서열을 입력해주세요: ")

# 각 염기의 개수를 저장할 딕셔너리를 초기화합니다.
counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

# 반복문을 사용하여 염기의 개수를 세고 딕셔너리에 저장합니다.
for base in sequence:
    if base in counts:
        counts[base] += 1

# 결과를 출력합니다.
for base, count in counts.items():
    print("{}의 개수: {}".format(base, count))
3.
# 염기 서열을 입력받습니다.
sequence = input("염기 서열을 입력해주세요: ")

# 코돈의 개수를 저장할 딕셔너리를 초기화합니다.
codon_counts = {}

# 반복문을 사용하여 코돈의 개수를 세고 딕셔너리에 저장합니다.
for i in range(len(sequence) - 2):
    codon = sequence[i:i+3]
    if codon in codon_counts:
        codon_counts[codon] += 1
    else:
        codon_counts[codon] = 1

# 결과를 출력합니다.
print(codon_counts)
4.
def flatten(lst):
    result = []  # 평탄화된 결과를 저장할 리스트
    
    # 리스트의 각 요소에 대해 반복하며 처리합니다.
    for item in lst:
        # 요소가 리스트인 경우 재귀적으로 평탄화 작업을 수행합니다.
        if isinstance(item, list):
            result.extend(flatten(item))
        # 그렇지 않은 경우 요소를 결과 리스트에 추가합니다.
        else:
            result.append(item)
    
    return result

# 주어진 리스트
nested_list = [1, 2, [3, 4], 5, [6, 7], [8, 9]]

# 리스트를 평탄화합니다.
flattened_list = flatten(nested_list)

# 결과 출력
print(flattened_list)