from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / "drivers" / "chromedriver.ext"

chrome_options = webdriver.ChromeOptions()
chrome_service = Service()
chrome_browser = webdriver.Chrome(
    chrome_options,
    chrome_service,
)


TIME_TO_WAIT = 5

chrome_browser.get("https://www.google.com.br/")

# Espere para encontrar o input
search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located(
        (By.NAME, "q")
    )
)
search_input.send_keys("Hello, world!!!")
search_input.send_keys(Keys.ENTER)

# Pegar elementos
results = chrome_browser.find_element(By.ID, "search")
links = results.find_elements(By.TAG_NAME, "a")

links[0].click()

# Dorme por 10 segundos
sleep(TIME_TO_WAIT)
