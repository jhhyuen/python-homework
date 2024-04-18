#   사용자 정의 함수부

def read_single_digit(number):
    digits_korean = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return digits_korean[number]

def read_number(number):
    if number == 0:
        return "영"

    digit_100 = number // 100
    digit_10 = (number % 100) // 10
    digit_1 = number % 10

    result = ''

    if digit_100 > 0:
        result += read_single_digit(digit_100) + ' '
    if digit_10 > 0:
        result += read_single_digit(digit_10) + ' '
    if digit_1 > 0:
        result += read_single_digit(digit_1)

    return result

#   주 프로그램부
def show_message():
    try:
        number = int(input("세 자리수  정수 입력: "))
        if 0 <= number <= 999:
            print(read_number(number))
        else:
            print("잘못된 입력입니다. 세 자리수 이하의 정수를 입력하세요.")
    except ValueError:
        print("잘못된 입력입니다. 세 자리수 이하의 정수를 입력하세요.")

if __name__ == "__main__":
    show_message()
