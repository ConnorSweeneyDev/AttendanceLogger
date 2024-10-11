import os
import time
from datetime import datetime

from button import click_button

def click_attend(page):
    clicked = 0
    clicked += click_button(page, "//*[@id=\"pbid-buttonFoundHappeningNowButtonsOneHere\"]")
    click_button(page, "//*[@id=\"notification-center\"]/div/ul[1]/li/div[2]/button")
    clicked += click_button(page, "//*[@id=\"pbid-buttonFoundHappeningNowButtonsTwoHere\"]")
    click_button(page, "//*[@id=\"notification-center\"]/div/ul[1]/li/div[2]/button")

    return clicked

def find_lectures(page, lecture_total):
    time.sleep(1)
    os.system("cls")
    print("Checking for lectures...")

    clicked = click_attend(page)
    if clicked == 1: print("1 Lecture found!")
    elif clicked == 2: print("2 Lectures found!")
    else: print("No lectures found.")
    time.sleep(1)

    os.system("cls")
    print("Signed in as " + page.locator("xpath=//*[@id=\"username\"]/span").inner_text())
    print("Lectures attended today: " + str(lecture_total + clicked))
    time.sleep(60)
    return clicked

def get_current_minute(page):
    current_datetime = datetime.strptime(page.locator("xpath=//*[@id=\"jsTime\"]").inner_text(), "%d/%m/%Y %H:%M:%S")
    return current_datetime.strftime("%M")

def check_attendance(page, lecture_total):
    attend_target_minutes = ["02", "32"]
    refresh_target_minutes = ["01", "31"]
    current_minute = get_current_minute(page)

    clicked = 0
    if current_minute in attend_target_minutes:
        clicked += find_lectures(page, lecture_total)
    elif current_minute in refresh_target_minutes:
        page.reload()
        page.wait_for_load_state()
        time.sleep(60)

    time.sleep(0.5)
    return clicked

def check_timeout(page):
    click_button(page, "//*[@id=\"pbid-btnTimeOut\"]")
