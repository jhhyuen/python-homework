shopping_bag = [ ] 

while True:
    item = input("상품명? ")  
    if not item:  
        break
    shopping_bag.append(item)  
    print(f"장바구니에 {item}가(이) 담겼습니다.")

print(">>> 장바구니 보기:")


while True:
    count = input("수량? ")  
    if not count:  
        break
    shopping_bag.append(item)  
    print(f"장바구니에 {item}가(이) {count}개가 담겼습니다.")
