import random
import threading
import time
from datetime import datetime, timedelta
import sys
import os
from pathlib import Path
from typing import Optional
from pyparsing import And
import requests
from bs4 import BeautifulSoup as bs
import json
import re
import pyautogui as pg
import pyperclip
import pywinauto
import pygetwindow as gw
import clipboard as cb
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ppadb.client import Client as AdbClient
import keyboard
from tkinter import *
from tkinter import ttk
import requests
import winsound as ws
import glob
import aiohttp
import asyncio


# chrome://version/ 에서 '프로필경로' 복사, 난 왜 디폴트만 되지?? 뭔... 딴건 필요 없쓰....


def goScript(getDict):
    
    # folder = 'id_1'
    # with open(f'./etc/content/{folder}/content.txt', 'r') as f:
    #     getLines = f.readlines()
        
        
    
    # print(getLines)
    # pg.alert('대기~~~')

    # path_dir = './etc/content'
    # file_list = os.listdir(path_dir)
    # print(file_list)
    # pg.alert('대기~~~')
    
    exLineNum = getDict['nlist']
    wb = load_workbook('./etc/nid.xlsx')
    ex = wb.active
    
    
    preIp = ''
    while True:
        getIP = changeIp()
        print(getIP)
        if not preIp == getIP:
            preIp = getIP
            break
        
    global driver
    
    
    options = Options()
    user_data = 'C:\\Users\\pcy\\AppData\\Local\\Google\\Chrome\\User Data\\default'
    service = Service(ChromeDriverManager().install())
    options.add_argument(f"user-data-dir={user_data}")
    # options.add_argument('--profile-directory=Profile 3')
    pg.alert('프로필을 선택해주세요!')
    driver = webdriver.Chrome(service=service, chrome_options=options)
    
    driver.get('https://www.naver.com')
    loginBtn = searchElement('.sc_login')
    loginBtn[0].click()
    
    cb.copy(ex.cell(exLineNum, 1).value)
    pg.alert('아이디가 복사되었습니다. 붙여넣기 해주세요')
    
    cb.copy(ex.cell(exLineNum, 2).value)
    pg.alert('비밀번호가 복사되었습니다. 로그인 후 블로그 작성 준비가 되면 엔터를 클릭해주세요!')
    
    
    path_dir = './etc/content'
    folder_list = os.listdir(path_dir)
    for folder in folder_list:
        print(driver.window_handles)
        # driver.to_switch()
        driver.switch_to.window(driver.window_handles[1])
        
        driver.switch_to.frame('mainFrame')
        
        writeArea = searchElement('.se-component-content')
        pg.alert(writeArea)
        
        with open(f'./etc/content/{folder}/content.txt', 'r') as f:
            getLines = f.readlines()
            
        for i, getline in enumerate(getLines):
            getline = getline.replace('\n', '')
            
            if getline == 'img_line':
                pg.alert('이미지를 첨부 해주세요 첨부 후 확인 버튼을 클릭 해주세요')
                continue
            
            if i == 0:
                writeArea[0].click()
                keyboard.write(text=getline, delay=0.05)
                wait_float(1.2,2.8)
            elif i == 1:
                writeArea[1].click()
                keyboard.write(text=getline, delay=0.05)
                wait_float(0.5,0.9)
                pg.press('enter')
                wait_float(0.5,0.9)
            else:
                keyboard.write(text=getline, delay=0.05)
                wait_float(0.5,0.9)
                pg.press('enter')
                wait_float(0.5,0.9)
        
        pg.alert('글 작성 완료!! 반드시 예약으로 발행 해주세요!! 다음글이 있을경우 글쓰기 준비를 해주세요!')
    
    
    
    
    # options = Options()
    # service = Service(ChromeDriverManager().install())
    # # options.add_argument("--headless")
    # options.add_argument('--no-sandbox')
    # options.add_argument("--disable-dev-shm-usage")
    
    # user_data = r'C:\Users\pcy\AppData\Local\Google\Chrome\User Data'
    # options.add_argument(f"user-data-dir={user_data}")
    
    # # default => 1 / 2 => 2 / 3 => 4 / 4 => 5
    # options.add_argument('--profile-directory=Profile 3')
    
    # pg.alert('대기1111')
    # driver = webdriver.Chrome(options=options)
    
    # pg.alert('대기2222')
    # driver.get('https://www.naver.com/')
    
    # pg.alert(text='로그인 대기~~~~')
    
def makeBlogContent():
    
    
    a = random.sample(range(1,101),10) # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
    print(a)
    subjectArr = ['창동','더큐브','오피스텔','아레나','분양','정보']
    firstPage = requests.get('https://m.blog.naver.com/wpthdud0/222906496708')
    fisrtContent = makeContentArr(firstPage)

    
    seconPage = requests.get('https://m.blog.naver.com/meirand/222713232416')
    secondContent = makeContentArr(seconPage)
    
    if len(fisrtContent) > len(secondContent):
        contentLength = len(secondContent)
    else:
        contentLength = len(fisrtContent)
        
    with open('./etc/text.txt', 'a') as f:
        for i in range(0, contentLength):
            getLastSentence_first = fisrtContent[i].pop(len(fisrtContent[i]) - 1)
            getLastSentence_second = secondContent[i].pop(len(secondContent[i]) - 1)

            
            if random.randrange(1,3) == 1:
                lastSentence = getLastSentence_first
                allArr = secondContent[i] + fisrtContent[i]
            else:
                lastSentence = getLastSentence_second
                allArr = fisrtContent[i] + secondContent[i]
                
            
            sampleRandom = random.sample(range(0, len(allArr)), len(allArr) // 3 * 2)
            resultSentence = ''
            
            for k in sampleRandom:
                resultSentence = resultSentence + allArr[k] + ' '
            # for k in range(1, len(sampleRandom)):
            #     resultSentence = resultSentence + allArr[sampleRandom[]] + ' '
            resultSentence = resultSentence + lastSentence + '.'
            
            f.write(f'{resultSentence}\n')
    pg.alert('대기요~~~~~~~~~~~~')















# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>함수 시작염

# 상품 들어가서 스크롤 내리고 나오기


def makeContentArr(page):
    soup = bs(page.text, "html.parser")
    elements = soup.select('.se-module.se-module-text')
    sentenceEndArr = ['요','죠','다','용']
    
    allStr = []
    for ele in elements:
        p = re.compile('[\uAC00-\uD7A30-9a-zA-Z\s]+')
        chkResult = p.findall(str(ele))
        allStr = allStr + chkResult

    p_str = re.compile(r'[a-zA-Z0-9,|\n]+')
    for i in range(1, len(allStr)):
        for j, strin in enumerate(allStr):
            getStr = p_str.search(strin)
            if getStr is not None:
                allStr.pop(j)
                break

            
    allStr = "".join(allStr)
    allStr = allStr.replace('   ', ' ')
    allStr = allStr.replace('   ', ' ')
    allStr = allStr.replace('   ', ' ')
    allStr = allStr.replace('  ', ' ')
    allStr = allStr.replace('  ', ' ')
    allStr = allStr.replace('  ', ' ')
    
    resetStrArr = allStr.split(' ')
    tempArr = []
    for i in range(0, len(resetStrArr)):
        for j, strin in enumerate(resetStrArr):
            if(strin != ''):
                if strin[-1] in sentenceEndArr:
                    chkArr = resetStrArr[0:j + 1]
                    tempArr.append(chkArr)
                    del resetStrArr[0:j + 1]
                    break
    
    return tempArr

def changeIp():
    try:
        os.system('adb server start')
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.devices()  # 디바이스 1개
        ondevice = device[0]
        ondevice.shell("input keyevent KEYCODE_POWER")
        ondevice.shell("svc data disable")
        ondevice.shell("settings put global airplane_mode_on 1")
        ondevice.shell(
            "am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")

        ondevice.shell("svc data enable")
        ondevice.shell("settings put global airplane_mode_on 0")
        ondevice.shell(
            "am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")
        time.sleep(3)
        while True:
            try:
                wait_float(0.5, 0.9)
                getIp = requests.get("http://ip.jsontest.com").json()['ip']
                if getIp is not None:
                    break
            except:
                continue
    except:

        while True:
            try:
                wait_float(0.5, 0.9)
                getIp = requests.get("http://ip.jsontest.com").json()['ip']
                if getIp is not None:
                    break
            except:
                continue
    return getIp



def searchElement(ele):
    wait_float(0.3, 0.7)
    re_count = 0
    element = ""
    while True:
        re_count += 1
        if re_count % 5 == 0:
            print(ele)
            print("새로고침!!!!")
            driver.refresh()
            focus_window('chrome')
            pg.press('F5')
        elif element != "":
            break
        try:
            element = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, ele)))
        except:
            pass
        

    selected_element = driver.find_elements(by=By.CSS_SELECTOR, value=ele)
    wait_float(0.3, 0.7)
    return selected_element



def untilEleShow(clickEle, searchEle):
    while True:
        try:
            clickEle.click()
            time.sleep(1)
        except:
            pass
        try:
            btnEle = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, searchEle)))
            if btnEle is not None:
                return
        except:
            continue


def untilEleGone(clickEle, searchEle):
    while True:
        try:
            clickEle.click()
            time.sleep(1)
        except:
            pass
        
        try:
            btnEle = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, searchEle)))
            if btnEle is None:
                return
        except:
            return


def wait_float(start, end):
    wait_ran = random.uniform(start, end)
    time.sleep(wait_ran)


def exitApp():
    pg.alert(text='프로그램을 종료합니다.', title='제목입니다.', button='OK')
    try:
        driver.quit()
    except:
        pass
    sys.exit(0)


def focus_window(winName):
    if winName == 'chkname':
        win_list = gw.getAllTitles()
        pg.alert(text=f"{win_list}")
    # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
    win = gw.getWindowsWithTitle(winName)[0]
    win.activate()  # 윈도우 활성화


BASE_DIR = Path(__file__).resolve().parent




async def getEmptyArr(setNum, exName):
    getArr = []
    asyncio.gather(*[busyFunc(i, getArr, exName) for i in range(1, setNum)])
    return getArr


async def busyFunc(i, getArr, exName):
    getTime = exName.cell(i, 4).value

    try:
        if getTime is None:
            getTime = datetime.now().date()
        if isinstance(getTime, datetime):
            getTime = getTime.date()
        compareTime = datetime.now() - timedelta(days=3)
        if exName.cell(i, 4).value is None or getTime <= compareTime.date():
            getArr.append(i)
    except:
        pass


def getExLength(exName):
    ExLength = 0
    while True:
        ExLength += 1
        if exName.cell(ExLength, 2).value is None:
            break
    return ExLength


def getUaNum():
    with open("./etc/useragent/useragent_all.txt", "r") as f:
        fArr = f.readlines()
        fCount = len(fArr)
        uaSet = random.randrange(0, fCount)
    return uaSet

def mainToCafe():
    shs_item = searchElement('.shs_item')
    for item in shs_item:
        chkCafe = item.find_element(
            by=By.CSS_SELECTOR, value='a').get_attribute('href')
        if 'cafe' in chkCafe:
            untilEleGone(item, '.shs_list')
            break
    
    myCafeGo = searchElement('.mycafe .btn_cafe_more')
    untilEleGone(myCafeGo[0], '.mycafe')



    myCafeList = searchElement('.list_cafe__favorites li')
    with open("./etc/cafe_info.txt", "r") as f:
        getCafeNameList = f.readlines()
        getCafeName = getCafeNameList[0]
        getCafeName = getCafeName.replace(" ", "")
    
    for onCafe in myCafeList:
        chkCafeTitle = onCafe.find_element(by=By.CSS_SELECTOR, value='.title').text
        chkCafeTitle = chkCafeTitle.replace(" ", "")

        if chkCafeTitle in getCafeName:
            untilEleGone(onCafe, '.list_cafe__favorites')
            break
        
    # 카페 진입 끝

def getBlogContent(subjectArr):
    # 블로그 글따기 시작

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://section.blog.naver.com/BlogHome.naver')

    try:
        popup = driver.find_element(
            by=By.CSS_SELECTOR, value='#floatingda_home')
        popupClostBtn = popup.find_elements(by=By.CSS_SELECTOR, value='button')
        popupClostBtn[-1].click()
    except:
        pass

    while True:
        
        
        try:
            nCategoryList = driver.find_elements(by=By.CSS_SELECTOR, value='.navigator_category a')
            categoryRanVal = random.randrange(0, len(nCategoryList) - 1)
            nCategoryList[categoryRanVal].click()

            wait_float(0.5, 0.9)

            paginationNum = driver.find_elements(by=By.CSS_SELECTOR, value='.pagination span')
            driver.execute_script("arguments[0].scrollIntoView();", paginationNum[0])
            paginationRanVal = random.randrange(0, len(paginationNum) -1)
            getClickPage = paginationNum[paginationRanVal].find_element(by=By.CSS_SELECTOR, value='a')
            getClickPage.click()
            wait_float(0.5, 0.9)

            infoPostList = driver.find_elements(by=By.CSS_SELECTOR, value='.info_post')
            infoPostRanVal = random.randrange(0, len(infoPostList) - 1)
            getInfoPostTag_a = infoPostList[infoPostRanVal].find_element(by=By.CSS_SELECTOR, value='.desc a')
            getInfoPostLink = getInfoPostTag_a.get_attribute('href')
            getInfoPostLink = getInfoPostLink.replace('//', '//m.')
        except:
            driver.refresh()
            focus_window('chrome')
            pg.press('F5')
            wait_float(2.5,3.5)
            continue

        page = requests.get(getInfoPostLink)
        soup = bs(page.text, "html.parser")
        elements = soup.select('.se-module.se-module-text')

        allStr = []
        for ele in elements:
            p = re.compile('[\uAC00-\uD7A30-9a-zA-Z\s]+')
            chkResult = p.findall(str(ele))
            allStr = allStr + chkResult

        p_str = re.compile(r'[a-zA-Z0-9,|\n]+')
        p_space = re.compile('\s\s')

        for i in range(1, len(allStr)):
            for j, strin in enumerate(allStr):
                getStr = p_str.search(strin)
                if getStr is not None:
                    allStr.pop(j)
                    break
                getSpace = p_space.search(strin)
                if getSpace is not None:
                    allStr.pop(j)
                    break
                if strin == " ":
                    allStr.pop(j)
                    break
        allStr = "".join(allStr)
        if len(allStr) < 600:
            continue
        if len(allStr) > 1200:
            sliceRanNum = random.randrange(1050, 1150)
            allStr = allStr[0:sliceRanNum]
        break

    resetStrArr = allStr.split(' ')

    resetListArr = list_chunk(resetStrArr, 12)
    for resetList in resetListArr:
        setRan = random.randrange(2, 5)
        resetOn = random.sample(range(1, 13), setRan)

        if resetList == "":
            continue

        for inon in resetOn:
            changeRanCount = random.randrange(0, len(subjectArr))
            chkChangeRan = random.randrange(1, 6)
            if chkChangeRan == 1:
                try:
                    resetList[inon - 1] = subjectArr[changeRanCount]
                except:
                    pass
            else:
                try:
                    resetList[inon - 1] = ''
                except:
                    pass

    imgLineCountBasic = divmod(len(resetListArr), 2)
    imgLineCount = random.randrange(
        int(imgLineCountBasic[0]) - 4, int(imgLineCountBasic[0]) + 4)

    allContent = ''
    for i, setList in enumerate(resetListArr):
        if imgLineCount == i:
            allContent = allContent + 'img_line|randomimg\n'
        for setStr in setList:
            if setStr == '':
                continue
            elif len(setStr) > 20:
                continue
            allContent = allContent + setStr
            allContent = allContent + ' '
        allContent = allContent + '\n'

    driver.close()
    return allContent


# subjectArr
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
