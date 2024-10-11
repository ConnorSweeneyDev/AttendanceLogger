import os

from playwright.sync_api import sync_playwright

from login import goto_login_page, retrieve_credentials, enter_credentials, wait_for_verification
from attend import find_lectures, check_timeout, check_attendance

def attend_lectures(page):
    lecture_total = find_lectures(page, 0)
    while True:
        check_timeout(page)
        lecture_total += check_attendance(page, lecture_total)

def microsoft_login(page):
    successful_login = False
    while not successful_login:
        goto_login_page(page)
        username, password = retrieve_credentials()
        successful_login = enter_credentials(page, username, password)
    wait_for_verification(page)

def initialize_browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    return context

def main():
    os.system("cls")
    with sync_playwright() as playwright:
        context = initialize_browser(playwright)
        context.set_default_timeout(3000)
        page = context.new_page()

        try:
            microsoft_login(page)
            attend_lectures(page)
        except KeyboardInterrupt:
            os.system("cls")

if __name__ == "__main__":
    main()
