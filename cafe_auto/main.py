from ongo import *



def th():
    getDict = {}
    onth = threading.Thread(target=lambda: goScript(getDict))
    onth.daemon = True
    onth.start()

# def th2():
#     onth = threading.Thread(ongo_searchItem())
#     onth.daemon = True
#     onth.start()


# 윈도우 창 생성 및 버튼 화면 조절
root = Tk()
root.title("카페 자동화")
root.geometry("300x360+500+300")
root.resizable(False, FALSE)

frame1 = LabelFrame(root, text='버튼', padx=40, pady=20)  # padx / pady 내부여백
frame1.pack(padx=10, pady=5)  # padx / pady 외부여백

frame2 = LabelFrame(root, text='아이피 변경', padx=60, pady=0)  # padx / pady 내부여백
frame2.pack(padx=10, pady=5)  # padx / pady 외부여백

frame3 = LabelFrame(root, text='아이피 변경', padx=60, pady=0)  # padx / pady 내부여백
frame3.pack(padx=10, pady=5)  # padx / pady 외부여백

# 시작 버튼 생성
btn1 = Button(frame1, text='카페 ALL 자동화', command=th, padx=50)
btn1.pack()

# btn2 = Button(frame1, text='쇼핑 순위 체크', command=th2, padx=50)
# btn2.pack()

btn3 = Button(frame1, text="종료하기", command=exitApp, padx=50)
btn3.pack()


# ipVal = IntVar()
# ipChk1 = Radiobutton(frame2, text="아이피 변경", value=1, variable=ipVal)
# ipChk1.select()
# ipChk2 = Radiobutton(frame2, text="아이피 미변경", value=0, variable=ipVal)
# ipChk1.pack()
# ipChk2.pack()


# loginVal = IntVar()
# loginChk1 = Radiobutton(frame3, text="랜덤 로그인", value=1, variable=loginVal)
# loginChk1.select()
# loginChk2 = Radiobutton(frame3, text="로그인 안함", value=0, variable=loginVal)
# loginChk1.pack()
# loginChk2.pack()





# ********************************

# 윈도우창 계속 띄우기
root.mainloop()
