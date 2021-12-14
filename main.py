import random
import time

import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

TFR = []
for _i in range(random.randint(20, 30)):
    TFR.append(True)
for _i in range(random.randint(5, 7)):
    TFR.append(False)

version = 1.0
print("Nitro by TacoError, Version " + str(version))
print("Opening driver")
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--profile-directory=Default")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)


def Class_Exists(name):
    try:
        if driver.find_element(By.CLASS_NAME, name):
            return True
    except (Exception, NoSuchElementException):
        return False


driver.delete_all_cookies()
driver.get("https://nitrotype.com/race")
print("Driver opened, getting NitroType")
while True:
    if keyboard.is_pressed("0"):
        def Run_Bot():
            print("Running")
            if not Class_Exists("dash-letter"):
                wait = WebDriverWait(driver, 10)
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".is-retracting")))
                time.sleep(3)
            filtered_string = []
            words = driver.find_elements(By.CLASS_NAME, "dash-letter")
            words.pop()
            for letter in words:
                letter = letter.get_attribute("textContent")
                if "\xa0" in letter:
                    letter = str(letter).replace("\xa0", " ")
                filtered_string.append(letter)
            filtered_string = "".join(filtered_string)
            if Class_Exists(".is-retracting"):
                wait = WebDriverWait(driver, 10)
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".is-retracting")))
                time.sleep(3)
            for i in range(len(filtered_string)):
                letter = filtered_string[i]
                if random.choice(TFR):
                    keyboard.write(letter)
                else:
                    if letter == "o":
                        keyboard.write("e")
                    else:
                        keyboard.write("o")
                    time.sleep(0.06)
                    keyboard.write(letter)
                time.sleep(0.06)
            print("Done")
            time.sleep(5)
            keyboard.press_and_release("ENTER")
            time.sleep(3)
            Run_Bot()


        time.sleep(3)
        Run_Bot()
