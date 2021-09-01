from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
print("哔哩哔哩已经打开")