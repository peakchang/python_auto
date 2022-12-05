from ongo import *



def th():
    getDict = {}
    onth = threading.Thread(target=lambda: goScript(getDict))
    onth.daemon = True
    onth.start()

def th1():
    print('닝러니ㅏ어리머인러미ㅏㅇㄴ러ㅣ멀')
    getDict = {}
    onth = threading.Thread(target= imageReduceCapa())
    onth.daemon = True
    onth.start()


# 윈도우 창 생성 및 버튼 화면 조절
root = Tk()
root.title("카페 자동화")
root.geometry("300x360+500+300")
root.resizable(False, FALSE)

frame1 = LabelFrame(root, text='이미지다운', padx=40, pady=10)  # padx / pady 내부여백
frame1.pack(padx=10, pady=5)  # padx / pady 외부여백

frame2 = LabelFrame(root, text='이미지용량', padx=60, pady=10)  # padx / pady 내부여백
frame2.pack(padx=10, pady=5)  # padx / pady 외부여백



# 시작 버튼 생성
f_btn1 = Button(frame1, text='이미지 다운', command=th, padx=50)
f_btn1.pack()

# 시작 버튼 생성
f_btn2 = Button(frame2, text='이미지 용량 줄이기', command=th1, padx=50)
f_btn2.pack()


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
