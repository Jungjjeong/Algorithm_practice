menu = 0  # 선택메뉴
number = 0  # 주문수량
price = 0  # 상품단가
total = 0  # 금액합계

print("="*50)
print("주문을 끝내려면 [0]을 입력하세요.")
print("="*50)

while True:
    menu = int(input('선택 메뉴: '))
    if menu == 0:
        print("-" * 50)
        print("금액 합계는", total)
        break

    number = int(input('주문 수량: '))

    if menu == 1:
        price = 5000 * number
        total += price
    elif menu == 2:
        price = 4000 * number
        total += price
    elif menu == 3:
        price = 3500 * number
        total += price
    elif menu == 4:
        price = 2000 * number
        total += price
    else:
        print('잘못된 메뉴 번호입니다. 다시 입력해주세요.')
