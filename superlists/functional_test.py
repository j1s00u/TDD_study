from selenium import webdriver

binary = 'C:\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
