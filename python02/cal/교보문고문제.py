sticker_price = 1000
book_price = 2500

sticker = int(input("스티커 매수 입력>>> "))
book = int(input("북마크 매수 입력>>> "))
vip = int(input("vip: 1, 일반회원: 2>>> "))

total = sticker_price * sticker + book_price * book;
if vip == 1:
    print("당신이 내야할 금액은 ", total - total * 0.1)
else:
    print("당신이 내야할 금액은 ", total)
    