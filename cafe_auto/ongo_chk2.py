import threading
import time
import sys
import os

import pyautogui as pg
import pywinauto
import pygetwindow as gw
from openpyxl import load_workbook

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from ppadb.client import Client as AdbClient

import keyboard
from tkinter import *


import requests


def goScript(num,id):


    pg.alert(text=f"현재 위치는? : {pg.position()}")

    # os.startfile('whale.exe')

    # os.startfile('chrome.exe')

    win = gw.getWindowsWithTitle('Chrome')[0]  # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
    print(win)
    # if win.isActive == False:
    #     pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
    win.activate()  # 윈도우 활성화
    pg.click(win.left + 100, win.top + 150)

    pg.alert(text="asdljilasjdf")


    print(os.system('taskkill /f /im whale.exe'))

    pg.alert(text="asdljilasjdf")

    time.sleep(3)
    keyboard.write('The quick 브라운폭스 jumps over the 화난개.', 0.2)
    time.sleep(3)
    keyboard.write('한글은 어떻게 빨리 써지는거겠지???', 0.2)


    # 아이피 변경 체크 부분
    # if num == 1:
    #     oldIp = ""
    #     while True:
    #         newIp = changeIp()
    #         if newIp != oldIp or oldIp == "":
    #             break
    # else:
    #     pg.alert(title="아이피 수동 변경", text="아이피를 변경 해주세요!")

    pg.alert(text='시작합니다!')




    options = Options()
    user_agent = "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A325N/KSU1AUH2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
    options.add_argument('user-agent=' + user_agent)
    global driver
    driver = webdriver.Chrome(chrome_options=options)

    print(id)
    driver.get(url='https://www.naver.com')
    print('아니 씨발 왜 안되냐고!!!')
    time.sleep(3)


    # searchElement("#query")

    searchBar = searchElement("#MM_SEARCH_FAKE")
    searchBar[0].click()
    time.sleep(3)


    pg.alert(text='대기요!')

    print('----------- 엘리먼트 출력 부분 -----------')
    # print(element)
    print('----------- 엘리먼트 출력 끝 -----------')

    time.sleep(3)

    driver.find_element(by=By.CSS_SELECTOR, value='#query').send_keys('python')
    time.sleep(3)
    driver.find_element(by=By.CSS_SELECTOR, value='#query').send_keys(Keys.ENTER)
    time.sleep(3)
    driver.get(url='https://www.naver.com')
    driver.find_element(by=By.CSS_SELECTOR, value='#query').send_keys('python')
    time.sleep(3)
    driver.find_element(by=By.CSS_SELECTOR, value='#query').send_keys(Keys.ENTER)
    time.sleep(3)

    print('끝~~~~~~~~~~~~~~~~~~~~~')

def exitApp():
    pg.alert(text='프로그램을 종료합니다.', title='제목입니다.', button='OK')
    try:
        driver.quit()
    except:
        pass
    sys.exit(0)


def searchElement(ele):
    print('함수 진입!')
    re_count = 0
    while True:
        if re_count % 3 == 0:
            driver.refresh()
        elif element != "":
            break
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ele)))
        re_count += 1

    selected_element = driver.find_elements(by=By.CSS_SELECTOR, value=ele)
    print(len(selected_element))
    pg.alert(text=f"있어??")
    return selected_element


def changeIp():
    try:
        os.system('adb server start')
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.devices()  # 디바이스 1개
        ondevice = device[0]
        ondevice.shell("input keyevent KEYCODE_POWER")
        ondevice.shell("svc data disable")
        ondevice.shell("settings put global airplane_mode_on 1")
        ondevice.shell("am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")

        ondevice.shell("svc data enable")
        ondevice.shell("settings put global airplane_mode_on 0")
        ondevice.shell("am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")
        time.sleep(5)
        getIp = requests.get("http://ip.jsontest.com").json()['ip']
        pg.alert(text=f"현재 아이피는 {getIp} 입니다.")
    except:
        time.sleep(5)
        getIp = requests.get("http://ip.jsontest.com").json()['ip']
        pg.alert(text=f"현재 아이피는 {getIp} 입니다.")
    return getIp