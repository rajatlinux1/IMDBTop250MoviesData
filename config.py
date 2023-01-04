from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_option=Options()
chrome_option.add_argument("--headless")

BASE_DIR = Path(__file__).resolve().parent
driver = webdriver.Chrome(executable_path=f"{BASE_DIR}/chromedriver", options=chrome_option)
# driver = webdriver.Chrome(executable_path=f"{BASE_DIR}/chromedriver")
