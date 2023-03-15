def page(a, b, c):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR, a)
    password = driver.find_element(By.CSS_SELECTOR, b)
    submit = driver.find_element(By.CSS_SELECTOR, c)

    if a is None and b is None and c is None:
        return 'Не найдены'
    else:
        return 'Элементы найдены'

print(page('#user-name', '#password', '#login-button'))

