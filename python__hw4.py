def welcome_message(name):
    """
    이름을 받아 환영 메시지를 출력하는 함수
    :param name: 환영할 상대방의 이름
    """
    msg1 = f"Welcome back to Korea, {name}!"
    msg2 = "We are glad to see you again!"

    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    draw_line_string(rep_char('-', nstr))

    if len(msg1) >= len(msg2):
        print(f"| {msg1} |")
        print(f"| {msg2}{' ' * (nstr - len(msg2))} |")
    else:
        print(f"| {msg1}{' ' * (nstr - len(msg1))} |")
        print(f"| {msg2} |")

    draw_line_string(rep_char('-', nstr))

# 사용자 입력 받기
name = input("Enter your friend's name: ")

# 환영 메시지 출력
welcome_message(name)


print ( " 교수님 죄송합니다. 도저히 모르겠어요ㅜㅜㅜㅜ" )
