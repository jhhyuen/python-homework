def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("정수를 입력해주세요.")

def exchange(amount):
    coins = [500, 100, 50, 10]
    coin_counts = {}

    for coin in coins:
        count = amount // coin
        amount -= count * coin
        coin_counts[coin] = count

    return coin_counts

def main():
    try:
        amount = get_integer("동전으로 교환하고자 하는 금액은?: ")
    
        coin_counts = exchange(amount)
        
        print("동전 교환 결과:")
        for coin, count in coin_counts.items():
            print(f"{coin}원 짜리 동전 {count}개")

    except ValueError as ve:
        print("오류 발생:", ve)

if __name__ == "__main__":
    main()
