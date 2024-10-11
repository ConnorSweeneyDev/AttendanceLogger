import os
import time

import getpass

from button import click_button

def resend_code(page):
    os.system("cls")
    print("You took too long! Sending another code in 10 seconds...")
    time.sleep(10)
    page.click("xpath=//*[@id=\"idA_SAASTO_Resend\"]")
    page.wait_for_load_state()
    print("Please verify your login with the following code: " + page.locator("xpath=//*[@id=\"idRichContext_DisplaySign\"]").inner_text())

def wait_for_verification(page):
    print("Please verify your login with the following code: " + page.locator("xpath=//*[@id=\"idRichContext_DisplaySign\"]").inner_text())
    while True:
        if page.locator("//*[@id=\"idA_SAASTO_Resend\"]").is_visible():
            resend_code(page)
        elif click_button(page, "//*[@id=\"idBtn_Back\"]") == 1:
            break
        time.sleep(0.5)
    page.wait_for_load_state()
    os.system("cls")

def goto_login_page(page):
    page.goto("https://generalssb-prod.ec.royalholloway.ac.uk/BannerExtensibility/customPage/page/RHUL_Attendance_Student")
    page.wait_for_load_state()

def enter_credentials(page, username, password):
    print("Logging in...")
    page.fill("xpath=//*[@id=\"i0116\"]", username + "@live.rhul.ac.uk")
    page.click("xpath=//*[@id=\"idSIButton9\"]")
    page.wait_for_load_state()
    page.fill("xpath=//*[@id=\"i0118\"]", password)
    page.click("xpath=//*[@id=\"idSIButton9\"]")
    page.wait_for_load_state()
    os.system("cls")

    try:
        page.locator("xpath=//*[@id=\"idRichContext_DisplaySign\"]").inner_text() 
        return True
    except:
        print("Login failed! Please check your credentials and try again.")
        return False

def get_credentials():
    username = input("Enter your username (xxxxyyy): ")
    password = getpass.getpass(prompt = "Enter your password: ")
    save_credentials = input("Would you like to save your credentials for next time? (Y/n): ").lower()
    if save_credentials == "n":
        return username, password

    credentials = open("credentials.txt", "w")
    credentials.write(username + "\n" + password)
    credentials.close()
    return username, password

def check_existing_credentials():
    if os.path.exists("credentials.txt"):
        use_credentials = input("Do you want to use saved credentials? (Y/n): ").lower()
        if use_credentials != "n":
            credentials = open("credentials.txt", "r")
            username = credentials.readline().strip()
            password = credentials.readline().strip()
            credentials.close()
            return username, password
    return None, None

def retrieve_credentials():
    username, password = check_existing_credentials()
    if username is not None and password is not None:
        return username, password
    return get_credentials()
