from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
try:
    driver.get("https://www.example.com/")
    driver.maximize_window()
    # Wait for the "Login" button to become clickable
    login_button = WebDriverWait(driver, 10).until(
        # EC.element_to_be_clickable((By.XPATH, "//span[text(@'Login']"))
        EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ant-btn-text']"))
    )
    login_button.click()

    # Wait for the login form to load and then fill in the login credentials
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "normal_login_username"))
    )
    password_input = driver.find_element(By.ID, "normal_login_password")

    # Fill in the username and password
    username_input.send_keys("example@gmail.com")
    password_input.send_keys("kdjdjdjdj")

    # Click the login button
    login_submit_button = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block']")
    login_submit_button.click()
    time.sleep(10)
    
  
    try:
            # Wait for the "Go To Link" link to become clickable
        link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='nav__left_actions_btn']"))
        )
        link.click()
        print("Linked Successfully Clicked")
    except NoSuchElementException:
        print("link not found")

    time.sleep(10)

    # Hover over and click the element
    element_to_hover = driver.find_element(By.XPATH, "//div[@class='ibriDR']")
    
    hover = ActionChains(driver)
    hover.move_to_element(element_to_hover)
    hover.perform()

    element_to_click = driver.find_element(By.XPATH, "//a[@href='/route']")
    time.sleep(2)
    element_to_click.click()
    time.sleep(3)

    #hover
    element_to_hover = driver.find_element(By.XPATH, "//div[@class='sc-fzsDOv ibriDR']")
    
    hover = ActionChains(driver)
    hover.move_to_element(element_to_hover)
    hover.perform()

    time.sleep(3)
    key = driver.find_element(By.XPATH, "//div[text()='key']")
    driver.execute_script("arguments[0].click();", key)
    print("Clicked key Link")
    driver.execute_script("window.history.go(-1)")
    time.sleep(5)
    value = driver.find_element(By.XPATH, "//div[text()='value']")
    driver.execute_script("arguments[0].click();", value)
    time.sleep(2)

    #Now We are Creating a value in the form
    driver.find_element(By.XPATH, "//input[@placeholder='fname']").send_keys("fname")
    print("Done")

    #For back
    driver.back()
    print("Current Page title after back: " + driver.title)
    time.sleep(5)

    #select attribute from src
    driver.find_element(By.XPATH, "//svg[@src ='/static/media/paper.8f4e95eb.svg']").click()
    time.sleep(5)

   #For Two attributes
    Media_Library_Image = driver.find_element(By.XPATH,"//button[@class='ant-btn rounded ant-btn-lg'][span='Upload Image']")
    driver.execute_script("arguments[0].click();", Media_Library_Image)
    time.sleep(15)

    Icon = driver.find_element(By.XPATH, "//div[contains(text(),'Icon Size')]")
    driver.execute_script("arguments[0].click();", Icon)
    time.sleep(3)

    # Wait for the input element to be present
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "react-select-2-input"))
    )

    # Type 'testing' into the input element 
    input_element.send_keys("testing")

    time.sleep(3)
    input_element.send_keys(Keys.DOWN)
    input_element.send_keys(Keys.RETURN)

    driver.find_element(By.ID, "value").send_keys("ok")

     # Wait for the input element to be present
    input_email = driver.find_element(By.XPATH, "//input[@id='host_emails']")
    input_email.send_keys("exmaple@gmail.com")
    input_email.send_keys(Keys.RETURN)
    time.sleep(3)

    element = driver.find_element(By.CSS_SELECTOR, "input#ant-calendar-picker-input ant-input")
    driver.execute_script("arguments[0].removeAttribute('readonly')", element)
    driver.execute_script("arguments[0].setAttribute('value', '2023/01/31')", element)

    date=driver.find_element(By.XPATH, "//input[@placeholder='Start Date']")
    date.send_keys("18-10-2023")
    date.send_keys(Keys.RETURN)

    Page_Background_button = driver.find_element(By.XPATH, "//div[starts-with(@class,'ant-row')]/following::input[1]")
    driver.execute_script("arguments[0].click();", Page_Background_button)
    time.sleep(10)

except Exception as e:
    print("An exception occurred:", str(e))

finally:
    # Close the WebDriver when done or in case of an exception
    input('Press anything to quit') 
    driver.quit() 
