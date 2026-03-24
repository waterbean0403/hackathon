def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다"
    return a / b


print("=== 간단한 계산기 ===")
print("1: 더하기  2: 빼기  3: 곱하기  4: 나누기")

choice = input("연산을 선택하세요: ")

a = float(input("첫 번째 숫자: "))
b = float(input("두 번째 숫자: "))

if choice == "1":
    print("결과:", add(a, b))
elif choice == "2":
    print("결과:", sub(a, b))
elif choice == "3":
    print("결과:", mul(a, b))
elif choice == "4":
    print("결과:", div(a, b))
else:
    print("잘못된 입력입니다")
