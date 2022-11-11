# https://xlsxwriter.readthedocs.io/tutorial01.html

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import xlsxwriter
workbook=xlsxwriter.Workbook('Top_250_movies_data.xlsx')
worksheet=workbook.add_worksheet()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
# worksheet.write(raw, col, data)
worksheet.write(0,0, "Rank")
worksheet.write(0,1, "Name")
worksheet.write(0,2, "Year")
worksheet.write(0,3, "Rating")
for i in range(1, 251):
    Rank = i
    Name = driver.find_element(By.XPATH, f"//tbody[@class='lister-list']/tr[{i}]/td[2]/a").text
    Year = driver.find_element(By.XPATH, f"//tbody[@class='lister-list']/tr[{i}]/td[2]/span").text.strip('( )')
    Rating = driver.find_element(By.XPATH, f"//tbody[@class='lister-list']/tr[{i}]/td[3]/strong").text
    worksheet.write(i, 0, Rank)
    worksheet.write(i, 1, Name)
    worksheet.write(i, 2, Year)
    worksheet.write(i, 3, Rating)
    print(Rank, Name, Year, Rating)
workbook.close()