from ongo import *



def th():
    getDict = {'ipval': ipVal.get(),}
    getDict['nlist'] = idbox.current() + 1
    onth = threading.Thread(target=lambda: goScript(getDict))
    
    onth.daemon = True
    onth.start()

def th2():
    onth = threading.Thread(target=lambda: makeBlogContent(textbox.get()))
    onth.daemon = True
    onth.start()
    
def th3():
    
    getValList = {'nlist' : idbox.current() + 1}
    onth = threading.Thread(blogReplyReady(getValList))
    onth.daemon = True
    onth.start()


# 윈도우 창 생성 및 버튼 화면 조절
root = Tk()
root.title("블로그 자동화 테스트")
root.geometry("300x360+500+300")
root.resizable(False, FALSE)

frame0 = LabelFrame(root, text='아이피 변경', padx=60, pady=5)  # padx / pady 내부여백
frame0.pack(padx=10, pady=5)  # padx / pady 외부여백

ipVal = IntVar()
ipChk1 = Radiobutton(frame0, text="아이피 변경", value=1, variable=ipVal)
ipChk2 = Radiobutton(frame0, text="아이피 미변경", value=0, variable=ipVal)
ipChk1.select()
ipChk1.pack()
ipChk2.pack()



frame1 = LabelFrame(root, text='아이디 선택', padx=40, pady=20)  # padx / pady 내부여백
frame1.pack(padx=10, pady=5)  # padx / pady 외부여백

frame2 = LabelFrame(root, text='버튼', padx=60, pady=0)  # padx / pady 내부여백
frame2.pack(padx=10, pady=5)  # padx / pady 외부여백

frame3 = LabelFrame(root, text='아이피 변경', padx=60, pady=0)  # padx / pady 내부여백
frame3.pack(padx=10, pady=5)  # padx / pady 외부여백

# 시작 버튼 생성
btn1 = Button(frame2, text='블로그 자동화', command=th, padx=50)
btn1.pack()

btn2 = Button(frame2, text='블로그 글따기', command=th2, padx=50)
btn2.pack()

btn3 = Button(frame2, text="블로그 소셜", command=th3, padx=50)
btn3.pack()

btn4 = Button(frame2, text="종료하기", command=exitApp, padx=50)
btn4.pack()


wb = load_workbook('./etc/nid.xlsx')
ex = wb.active


nid_list = []
nlogin_list = []
i = 0
while True:
    i += 1
    id_val = ex.cell(i, 1).value
    if id_val is None:
        break
    else:
        nid_list.append(id_val)
        
idbox = ttk.Combobox(frame1, values=nid_list)
idbox.current(0)
idbox.pack()
textbox = ttk.Entry(frame1, width=20, textvariable=str)
textbox.pack()

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
