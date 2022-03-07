# coding=utf-8
import os
from selenium import webdriver
import datetime
import time
from os import path
import tkinter as tk
from tkinter import filedialog

#先来一次清屏操作
os.system("cls")
print("请选择你的chromedriever文件")
#拉起文件选择窗口，用来设定chromedriever的位置
root = tk.Tk()
root.withdraw()

#选择文件路径
local_way_path = filedialog.askdirectory()
local_way = filedialog.askopenfilename()

#设置好Chromedriver的路径
driver = webdriver.Chrome(local_way)
#让浏览器窗口最大化
driver.maximize_window()

#由于商城需要登录
def login(url1,url2):
    #打开网络商城的页面，并扫码登录
    driver.get(url1)
    time.sleep(1)
    if driver.find_element_by_link_text("登录"):
        driver.find_element_by_link_text("登录").click()
        print("请在15s内完成扫码")
        time.sleep(15)
        #打开商品详情页
        driver.get(url2)
        time.sleep(1)
    now=datetime.datetime.now()
    print("login success:",now.strftime("%Y-%m-%d %H:%M:%S"))

#定义购买函数
def buy(times):
    #创建死循环
    while True:
        #记录当前时间
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(times)
        print(now)
        if now == times:
            try:
                if driver.find_element_by_link_text("立即购买"):
                    driver.find_element_by_link_text("立即购买").click
                    driver.find_element_by_link_text("提交订单").click()
                    print('抢购成功，请尽快付款')
            except:
                print('请再次尝试提交订单')
        print(now)
        time.sleep(1)

#运行主程序
if __name__ == "__main__":
    #先来清屏一下
    os.system('cls')
    #抢购网站的主页面
    url1 = input('抢购网站的主页面的连接：')
    #商品详情页
    url2 = input('商品详情页的连接：')
    #抢购时间
    times = input("请输入抢购时间（格式为：2022-03-08 10:00:00）：")
    #给login函数传入参数
    login(url1,url2)
    #给buy函数传入参数
    buy(times)