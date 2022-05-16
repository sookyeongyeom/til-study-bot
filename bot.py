import time, win32con, win32api, win32gui, schedule


def kakao_sendtext(kakao_opentalk_name, text):
    # # 핸들
    hwndMain = win32gui.FindWindow(None, kakao_opentalk_name)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)
    # hwndListControl = win32gui.FindWindowEx(
    #     hwndMain, None, "EVA_VH_ListControl_Dblclk", None
    # )
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)


# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# # 채팅방 열기
def open_chatroom(chatroom_name):
    # # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx(
        hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None
    )
    hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit2_2, None, "Edit", None)

    # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1)  # 안정성 위해 필요
    SendReturn(hwndkakao_edit3)
    time.sleep(1)


def main():
    # # # 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
    kakao_opentalk_name = "TIL STUDY"

    open_chatroom(kakao_opentalk_name)

    # # 스케줄
    schedule.every().day.at("07:49").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("07:50").do(
        kakao_sendtext,
        kakao_opentalk_name,
        "[🤖STUDY안내봇]\n곧 1부가 시작됩니다! 오늘도 좋은 하루 되세요! 🌼",
    )

    schedule.every().day.at("11:59").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("12:00").do(
        kakao_sendtext, kakao_opentalk_name, "[🤖STUDY안내봇]\n1부가 종료되었습니다. 점심 드시고 만나요! 🍚"
    )

    schedule.every().day.at("12:49").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("12:50").do(
        kakao_sendtext, kakao_opentalk_name, "[🤖STUDY안내봇]\n곧 2부가 시작됩니다!"
    )

    schedule.every().day.at("16:59").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("17:00").do(
        kakao_sendtext, kakao_opentalk_name, "[🤖STUDY안내봇]\n2부가 종료되었습니다. 저녁 드시고 만나요! 🥘"
    )

    schedule.every().day.at("17:49").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("17:50").do(
        kakao_sendtext, kakao_opentalk_name, "[🤖STUDY안내봇]\n곧 3부가 시작됩니다!"
    )

    schedule.every().day.at("21:59").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("22:00").do(
        kakao_sendtext, kakao_opentalk_name, "[🤖STUDY안내봇]\n3부가 종료되었습니다. 고생하셨습니다! 💪"
    )

    schedule.every().day.at("22:49").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("22:50").do(
        kakao_sendtext, kakao_opentalk_name, "[🤖STUDY안내봇]\n곧 4부가 시작됩니다!"
    )

    schedule.every().day.at("02:59").do(open_chatroom, kakao_opentalk_name)
    schedule.every().day.at("03:00").do(
        kakao_sendtext, kakao_opentalk_name, "[🤖STUDY안내봇]\n4부가 종료되었습니다. 내일 또 만나요! 🌙"
    )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    print("[🤖STUDY안내봇] 일하는 중 ...")
    main()
