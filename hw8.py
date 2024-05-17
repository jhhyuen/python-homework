def buy(shopping_bag):
    item = input("상품명을 입력하세요 : ")
    if item == '끝':
        return False
    quantity = int(input(f"수량을 입력하세요: "))
    if item in shopping_bag:
        shopping_bag[item] += quantity
    else:
        shopping_bag[item] = quantity
    return True

def show(shopping_bag):
    print("\n현재 장바구니 품목:")
    for item, quantity in shopping_bag.items():
        print(f"{item}: {quantity}개")
    print()

def find(shopping_bag):
    item = input("확인하고자 하는 상품명을 입력하세요: ")
    if item in shopping_bag:
        print(f"{item}은(는) {shopping_bag[item]}개 있습니다.")
    else:
        print(f"{item}은(는) 장바구니에 없습니다.")

def main():
    shopping_bag = {}
    while True:
        if not buy(shopping_bag):
            break
    show(shopping_bag)
    find(shopping_bag)

if __name__ == "__main__":
    main()


