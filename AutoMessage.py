import time
import os
import pyperclip as pc
import webbrowser as web
import pyautogui as pg
from colorama import Fore

def sendwhatmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 10,
                         tab_close: bool = False, close_time: int = 3 ) -> None:
    
    if time_hour not in range(25) or time_min not in range(60):
        print("Invalid time format")

    timehr = time_hour

    if time_hour == 0:
        time_hour = 24
    call_second = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_second - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    if left_time < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.shad.ir takes some time to load")

    date = "%s:%s:%s" % (current_time.tm_mday, current_time.tm_mon, current_time.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("whatGP_history.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nGroup_id: %s\nMessage: %s" %
                   (date, time_write, group_id, message))
        file.write("\n--------------------\n")
    sleep_time = left_time - wait_time
    print(f"\nIn {sleep_time} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleep_time)
    web.open('https://web.whatsapp.com/accept?code=' + group_id)
    pc.copy(message)
    time.sleep(20)
    width, height = pg.size()
    pg.click(width / 2, height - height / 10)
    time.sleep(2)
    pg.hotkey('ctrl', 'v')
    time.sleep(2)
    pg.press('enter')
    print("\n" + Fore.GREEN + "Message sent successfully!")
    if tab_close:
        close_tab(wait_time=close_time)

def sendshadmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 10,
                         tab_close: bool = False, close_time: int = 3 ) -> None:

    if time_hour not in range(25) or time_min not in range(60):
        print("Invalid time format")

    timehr = time_hour

    if time_hour == 0:
        time_hour = 24
    call_second = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_second - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    if left_time < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.shad.ir takes some time to load")

    date = "%s:%s:%s" % (current_time.tm_mday, current_time.tm_mon, current_time.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("ShadGP&NUM_history.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nGroup_id: %s\nMessage: %s" %
                   (date, time_write, group_id, message))
        file.write("\n--------------------\n")
    sleep_time = left_time - wait_time
    print(f"\nIn {sleep_time} seconds web.shad.ir will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleep_time)
    web.open('https://web.shad.ir/#c=' + group_id)
    pc.copy(message)
    time.sleep(20)
    width, height = pg.size()
    pg.click(width / 2, height - height / 6)
    time.sleep(2)
    pg.hotkey('ctrl', 'v')
    time.sleep(2)
    pg.press('enter')
    print("\n" + Fore.GREEN + "Message sent successfully!")
    if tab_close:
        close_tab(wait_time=close_time)

def sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 10,
                tab_close: bool = False, close_time: int = 3) -> None:

    global sleep_time
    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format")

    timehr = time_hour

    if time_hour == 0:
        time_hour = 24
    call_sec = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_sec - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    if left_time < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s" % (current_time.tm_mday, current_time.tm_mon, current_time.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("WhatNUM_history.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s" %
                   (date, time_write, phone_no, message))
        file.write("\n--------------------\n")
    sleep_time = left_time - wait_time
    print(
        f"In {sleep_time} seconds web.whatsapp.com will open and after {wait_time} seconds message will "
        f"be delivered")
    time.sleep(sleep_time)
    web.open('https://web.whatsapp.com/send?phone=' + phone_no)
    pc.copy(message)
    time.sleep(20)
    width, height = pg.size()
    pg.click(width / 2, height - height / 10)
    time.sleep(2)
    pg.hotkey('ctrl', 'v')
    time.sleep(2)
    pg.press('enter')
    print("\n" + Fore.GREEN + "Message sent successfully!")
    if tab_close:
        close_tab(wait_time=close_time)

def Function():
    command_input = input(Fore.LIGHTGREEN_EX + "Enter the desired number to continue >> ")

    if(command_input == "1"):

        os.system("cls")
        Group_ID = input(Fore.LIGHTRED_EX + "Enter The Phone Number      : ")
        if(Group_ID == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Message_Text = input("Enter Your Message          : ")
        if(Message_Text == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Time_hr = int(input("Enter The Hour              : "))
        if(Time_hr == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Time_Min = int(input("Enter The Minute            : "))
        if(Time_Min == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()


        sendwhatmsg(Group_ID,Message_Text,Time_hr,Time_Min)

    elif(command_input == "2"):
        os.system("cls")
        Group_ID = input(Fore.LIGHTRED_EX + "Enter The Group ID      : ")
        if(Group_ID == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Message_Text = input("Enter Your Message      : ")
        if(Message_Text == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Time_hr = int(input("Enter The Hour          : "))
        if(Time_hr == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Time_Min = int(input("Enter The Minute        : "))
        if(Time_Min == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()

        sendwhatmsg_to_group(Group_ID,Message_Text,Time_hr,Time_Min)

    elif(command_input == "3"):
        os.system("cls")
        Group_ID = input(Fore.LIGHTRED_EX + "Enter The Group ID      : ")
        if(Group_ID == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Message_Text = input("Enter Your Message      : ")
        if(Message_Text == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Time_hr = int(input("Enter The Hour          : "))
        if(Time_hr == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()
        Time_Min = int(input("Enter The Minute        : "))
        if(Time_Min == ""):
            print("Field is mandatory")
            print(Fore.WHITE)
            exit()

        sendshadmsg_to_group(Group_ID,Message_Text,Time_hr,Time_Min)

    elif(command_input == "0"):
        os.system("cls")
        print(Fore.WHITE)
        exit()

    else:
        print(Fore.RED + "Incorrect number")
        print(Fore.WHITE)

os.system('cls')
print(Fore.LIGHTBLUE_EX + "<<  To send an automatic message to a WhatsApp number ..... select 1  >>")
print("<<  To send an automatic message to a WhatsApp group ...... select 2  >>")
print("<<  To send an automatic message to a Shad number or group  select 3  >>")
print("<<  To close the program .................................. select 0  >>")
print("\n")
print("             --*        Author   :   Amirh_Krg        *--")
print("             --* GitHub : Https://Github.com/AmirHKrg *--")
print("\n")

Function()

print(Fore.WHITE)
