# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
from selenium import webdriver
import time

driver=webdriver.Chrome("chromedriver.exe")
print("Iniciando programa:")
driver.minimize_window()
driver.get("https://www.speedtest.net/pt")
driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/a[1]/span[4]").click()
x, ping, down, up=0,0,0,0
y=0
print("Coletando dados:")
for i in range(0,11):
    j=i*10
    print("Carregando: ",j,"%")
    time.sleep(6)
    
while x==0:
    try:
        ping=driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]").text
        down=driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/span[1]").text
        up=driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/span[1]").text
        x=1
    except: x=0
    y=y+1
    if y==100: x=0
driver.close()


print("Ping: ",ping,"ms")
print("Download: ",down,"mbps")
print("Upload: ",up,"mbps")




