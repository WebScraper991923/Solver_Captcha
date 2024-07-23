from selenium_recaptcha_solver import RecaptchaSolver, StandardDelayConfig
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep


# test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
# chrome_driver_path = "chromedriver/chromedriver.exe"
# options = Options()
# service = Service(chrome_driver_path)

# options.add_argument("--window-size=1920,1000")

# options.add_argument(f'--user-agent={test_ua}')

# options.add_argument('--no-sandbox')
# options.add_argument("--disable-extensions")

# test_driver = webdriver.Chrome(service=service, options=options)
test_driver = webdriver.Chrome()
solver = RecaptchaSolver(driver=test_driver, delay_config=StandardDelayConfig())
print('sucess')


test_driver.get('https://www.google.com/recaptcha/api2/demo')
sleep(3)

recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

solver.click_recaptcha_v2(iframe=recaptcha_iframe)

test_driver.execute_script("document.getElementById('recaptcha-demo-submit').click()")

test_driver.find_element(By.CSS_SELECTOR, '.recaptcha-success')
print('sucess')





def __init__():
    try:
        test_driver.get('https://www.google.com/recaptcha/api2/demo')
        sleep(3)

        recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

        solver.click_recaptcha_v2(iframe=recaptcha_iframe)

        test_driver.execute_script("document.getElementById('recaptcha-demo-submit').click()")

        test_driver.find_element(By.CSS_SELECTOR, '.recaptcha-success')
        print('sucess')

    except Exception:
        pytest.fail('Failed to automatically resolve ReCAPTCHA.')
