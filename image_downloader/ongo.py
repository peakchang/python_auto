
import random
import threading
import time
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *
import sys
import os
from pathlib import Path

import re
import pyautogui as pg
import pyperclip
import pywinauto
import clipboard as cb

import keyboard
from tkinter import *
from tkinter import ttk
import requests
import winsound as ws
import glob
import aiohttp
import asyncio
from PIL import Image



###


def goScript(getDict):
    pass

def imageReduceCapa():
    # 1. 이미지 파일 기본 정보 읽기 #
    print('시작~~~~~~~~~~~~~')
    print(os.getcwd())
    original_path = f'{os.getcwd()}/pre_image/'
    change_path = f'{os.getcwd()}/result_image/'
    
    if not os.path.isdir(change_path):
        os.makedirs(change_path)
        
    change_img_qualty(original_path, change_path)

    

def change_img_qualty(original_path, change_path, qualty=85):
        """
        Change Image Qualty
        :param original_path: 원본 경로
        :param change_path: 변경 후 새롭게 저장될 경로
        :param qualty: Qualty(품질) 퍼센트(기본 : 85%)
        :return:
        """
        if not os.path.exists(change_path):
            os.mkdir(change_path)
        try:
            ims_list = os.listdir(original_path)
            ims_list.sort()
        except FileNotFoundError as e:
            print("이미지 원본 디렉터리가 존재하지 않습니다...")
            sys.exit(0)
        success_cnt = 0
        fail_cnt = 0
        for filename in ims_list:
            file = original_path + filename
            try:
                # im = Image.open(file)
                # im.save(os.path.join(change_path, filename), qualty=qualty)
                # print(filename)
                fileNmaeSplit = filename.split('.')
                im1 = Image.open(f"{original_path}/{filename}").convert('RGB')
                im1.save(f"{change_path}/{fileNmaeSplit[0]}.webp", 'webp')
                # os.remove(os.path.join(change_path, filename))
                # print("+ 성공 : {success}\n  "
                #     "- {success_path}"
                #     .format(success=file, success_path=os.path.join(change_path, filename))
                #     )
                
                success_cnt += 1
            except Exception as e:
                print("+ 실패 : {fail}".format(fail=file))
                fail_cnt += 1
        print("\n성공 : {success_cnt} 건 / 실패 : {fail_cnt} 건".format(success_cnt=success_cnt, fail_cnt=fail_cnt))
        sys.exit(0)