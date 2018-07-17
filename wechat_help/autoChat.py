#!/usr/bin/env python3
#  _*_ coding: utf-8 _*_
# coding=utf-8
import itchat
import random
import string
import os
import smtplib
from email.mime.text import MIMEText
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.blocking import BlockingScheduler


def show_login():
    sent_type = input("***************************\n"
                      "*                         *\n"
                      "*                         *\n"
                      "*                         *\n"
                      "*                         *\n"
                      "*   欢迎使用微信群发小助手！  *\n"
                      "*                         *\n"
                      "*                         *\n"
                      "*     普通用户请按1         *\n"
                      "*     高级用户请按2         *\n"
                      "*     退出请按3            *\n"
                      "*                         *\n"
                      "*                         *\n"
                      "*                         *\n"
                      "***************************\n")
    return int(sent_type)

def login_normal():
    result = False
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    msg_from = '280497626@qq.com'  # 发送方邮箱
    passwd = 'juvnryrhksgkcbbb'  # 填入发送方邮箱的授权码
    msg_to = '939892295@qq.com'  # 收件人邮箱
    subject = "普通用户登陆验证码"  # 主题
    content = salt
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("验证码已发送至邮箱，请输入验证码")
    except Exception:
        print("发送失败")
    finally:
        s.quit()
    pwd = input("请输入验证码：")
    if pwd == salt:
        result = True
    return result

def login_vip():
    result = False
    name = input("请输入用户名:")
    pwd = input("请输入密码：")
    if name == "LL" and pwd == "guidong":
        result = True
    return result


def sendmsg_onegroup():
    gname = input("请输入你想发送的的群的名字：")
    msg = input("请输入你想发送的话：")
    room = itchat.search_chatrooms(gname)
    if room is not None:
        username = room[0]['UserName']
        itchat.send_msg(msg, username)
        print("发送成功！")
    else:
        print("未找到该群！")

def sendmsg_allgroup():
    msg = input("请输入你想发送的话：")
    rooms = itchat.get_chatrooms(update=True)
    if rooms is not None:
        for i in rooms:
            uname = i['UserName']
            nname = i['NickName']
            itchat.send_msg(msg, uname)
            print("已发送成功到群：%s！" % nname)
    else:
        print("没有任何群！")

def sendimage_onegroup():
    gname = input("请输入你想发送的的群的名字：")
    image = input("请输入你想发送的图片的路径如'E:/hello/桂东.png'(记得加引号！！！)：")
    room = itchat.search_chatrooms(gname)
    if room is not None:
        username = room[0]['UserName']
        itchat.send_image(image, username)
        print("发送成功！")
    else:
        print("未找到该群！")

def sendimage_allgroup():
    image = input("请输入你想发送的图片的路径如'E:/hello/桂东.png'(记得加引号！！！)：")
    rooms = itchat.get_chatrooms(update=True)
    if rooms is not None:
        for i in rooms:
            uname = i['UserName']
            nname = i['Nickname']
            itchat.send_image(image, uname)
            print("已发送成功到群：%s！" % nname)
    else:
        print("没有任何群！")

def sendfile_onegroup():
    gname = input("请输入你想发送的的群的名字：")
    file = input("请输入你想发送的文件的路径如'E:/hello/桂东.html'(记得加引号！！！)：")
    room = itchat.search_chatrooms(gname)
    if room is not None:
        username = room[0]['UserName']
        itchat.send_image(file, username)
        print("发送成功！")
    else:
        print("未找到该群！")

def sendfile_allgroup():
    file = input("请输入你想发送的文件的路径如'E:/hello/桂东.html'(记得加引号！！！)：")
    rooms = itchat.get_chatrooms(update=True)
    if rooms is not None:
        for i in rooms:
            uname = i['UserName']
            nname = i['NickName']
            itchat.send_image(file, uname)
            print("已发送成功到群：%s！" % nname)
    else:
        print("没有任何群！")

def show_time():
    send_type = input("*********************************\n"
                           "请输入你想什么时候发的数字：\n"
                           "1.设置一个时间间隔，每隔一段时间发送\n"
                           "2.设置一个确定时间发送\n"
                           "3.现在就开始发送\n"
                           "4.退出\n"
                           "*********************************\n")
    return int(send_type)

def show():
    send_type = input("*********************************\n"
                      "请输入你想发送的类型的数字：\n"
                      "1.文字\n"
                      "2.图片\n"
                      "3.文件\n"
                      "4.退出\n"
                      "*********************************\n")
    return int(send_type)

def show_type():
    send_type = input("*********************************\n"
                      "请输入你想如何发的数字：\n"
                      "1.发送到指定的一个群\n"
                      "2.所有群直接群发\n"
                      "3.退出\n"
                      "*********************************\n")
    return int(send_type)

def run():
    while True:
        send_type = show()
        if send_type == 1:
            getshow = show_type()
            if getshow == 1:
                sendmsg_onegroup()
            elif getshow == 2:
                print("你确定要发送到以下这些群吗？")
                rooms = itchat.get_chatrooms(update=True)
                for i in rooms:
                    print(i['NickName'])
                ans = input("yes/no?")
                if ans == "yes":
                    sendmsg_allgroup()
                else:
                    run()
            elif getshow == 3:
                break
            else:
                print("您输入的数字不在范围内！请重新输入1-3内的数字：")
                show_type()

        elif send_type == 2:
            getshow = show_type()
            if getshow == 1:
                sendimage_onegroup()
            elif getshow == 2:
                print("你确定要发送到以下这些群吗？")
                rooms = itchat.get_chatrooms(update=True)
                for i in rooms:
                    print(i['NickName'])
                ans = input("yes/no?")
                if ans == "yes":
                    sendimage_allgroup()
                else:
                    run()
            elif getshow == 3:
                break
            else:
                print("您输入的数字不在范围内！请重新输入1-3内的数字：")
                show_type()

        elif send_type == 3:
            getshow = show_type()
            if getshow == 1:
                sendfile_onegroup()
            elif getshow == 2:
                print("你确定要发送到以下这些群吗？")
                rooms = itchat.get_chatrooms(update=True)
                for i in rooms:
                    print(i['NickName'])
                ans = input("yes/no?")
                if ans == "yes":
                    sendfile_allgroup()
                else:
                    run()
            elif getshow == 3:
                break
            else:
                print("您输入的数字不在范围内！请重新输入1-3内的数字：")
                show_type()

        elif send_type == 4:
            break

        else:
            print("您输入的数字不在范围内！请重新输入1-4内的数字：")
            show()


def setmsg(msg):
    rooms = itchat.get_chatrooms(update=True)
    if rooms is not None:
        for i in rooms:
            uname = i['UserName']
            nname = i['NickName']
            itchat.send_msg(msg, uname)
            print("已发送成功到群：%s！" % nname)
    else:
        print("没有任何群！")

def setimg(img):
    image = img
    rooms = itchat.get_chatrooms(update=True)
    if rooms is not None:
        for i in rooms:
            uname = i['UserName']
            nname = i['Nickname']
            itchat.send_image(image, uname)
            print("已发送成功到群：%s！" % nname)
    else:
        print("没有任何群！")

def setfile(file):
    rooms = itchat.get_chatrooms(update=True)
    if rooms is not None:
        for i in rooms:
            uname = i['UserName']
            nname = i['NickName']
            itchat.send_image(file, uname)
            print("已发送成功到群：%s！" % nname)
    else:
        print("没有任何群！")


def run_all():
    while True:
        global MSG
        global IMG
        global FILE
        sendtype = show_login()
        result = False
        if sendtype == 1:
            result = login_normal()
        elif sendtype == 2:
            result = login_vip()
        else:
            break
        if result == True:
            print("登陆成功！")
            print("请准备扫描登陆微信")
            itchat.auto_login(hotReload=True)
            print("登陆微信成功！您有以下这些群:")
            rooms = itchat.get_chatrooms(update=True)
            for i in rooms:
                print(i['NickName'])
            getans = show_time()
            if getans == 1:
                time_set = input("请输入一个间隔时间:如3即从先在开始每3小时自动发送")
                get_type = show()
                if get_type == 1:

                    MSG = input("请输入您要发送的文字:")
                    print("准备发送中。。。")
                    def msgset():
                        setmsg(MSG)

                    sched = BlockingScheduler()
                    int_trigger = IntervalTrigger(hour=int(time_set), id="my_job")
                    sched.add_job(msgset, int_trigger, id="my_job")

                    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
                    try:
                        sched.start()
                    except (KeyboardInterrupt, SystemExit):
                        sched.remove_job('my_job')
                    run_all()
                elif get_type == 2:

                    IMG = input("请输入您要发送的图片路径:")
                    print("准备发送中。。。")
                    def imgset():

                        setimg(IMG)

                    sched = BlockingScheduler()
                    int_trigger = IntervalTrigger(hour=int(time_set), id="my_job")
                    sched.add_job(imgset, int_trigger, id="my_job")
                    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
                    try:
                        sched.start()
                    except (KeyboardInterrupt, SystemExit):
                        sched.remove_job('my_job')
                    run_all()
                elif get_type == 3:

                    FILE = input("请输入您要发送的文件路径:")
                    print("准备发送中。。。")
                    def fileset():

                        setfile(FILE)

                    sched = BlockingScheduler()
                    int_trigger = IntervalTrigger(hour=int(time_set))
                    sched.add_job(fileset, int_trigger, id="my_job")
                    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
                    try:
                        sched.start()
                    except (KeyboardInterrupt, SystemExit):
                        sched.remove_job('my_job')
                    run_all()
                else:
                    break

            elif getans == 2:
                time_set = input("请输入一个准确的时间:如2018.7.10.8.20即2018年7月10日8点20分:\n")
                year, month, day, hour, minute = time_set.split('.')[0], time_set.split('.')[1], time_set.split('.')[2], time_set.split('.')[3], time_set.split('.')[4]
                get_type = show()
                if get_type == 1:
                    MSG = input("请输入您要发送的文字:")
                    print("准备发送中。。。")
                    def msgset():

                        setmsg(MSG)

                    sched = BlockingScheduler()
                    cron_trigger = CronTrigger(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute), second=0)
                    sched.add_job(msgset, cron_trigger, id="my_job")
                    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
                    try:
                        sched.start()
                    except (KeyboardInterrupt, SystemExit):
                        sched.remove_job('my_job')
                    run_all()
                elif get_type == 2:

                    IMG = input("请输入您要发送的图片路径:")
                    print("准备发送中。。。")
                    def imgset():

                        setimg(IMG)

                    sched = BlockingScheduler()
                    cron_trigger = CronTrigger(year=int(year), month=int(month), day=int(day), hour=int(hour),
                                               minute=int(minute), second=0)
                    sched.add_job(imgset, cron_trigger, id="my_job")
                    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
                    try:
                        sched.start()
                    except (KeyboardInterrupt, SystemExit):
                        sched.remove_job('my_job')
                    run_all()
                elif get_type == 3:

                    FILE = input("请输入您要发送的文件路径:")
                    print("准备发送中。。。")
                    def fileset():

                        setfile(FILE)

                    sched = BlockingScheduler()
                    cron_trigger = CronTrigger(year=int(year), month=int(month), day=int(day), hour=int(hour),
                                               minute=int(minute), second=0)
                    sched.add_job(fileset, cron_trigger, id="my_job")
                    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
                    try:
                        sched.start()
                    except (KeyboardInterrupt, SystemExit):
                        sched.remove_job('my_job')
                    run_all()
                else:
                    break

            elif getans == 3:
                run()
            else:
                break
        else:
            print("登陆失败！用户名不存在或密码错误！请重新登陆!")
            run_all()


if __name__ == '__main__':
    MSG = ''
    IMG = ''
    FILE = ''
    run_all()