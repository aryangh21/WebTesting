from selenium import webdriver
import random
import string
import time
from time import sleep
from selenium.webdriver.common.by import By
def generate_random_name():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia', 'James', 'Sophia', 'Robert', 'Ava']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Taylor', 'Anderson']
    return random.choice(first_names) + ' ' + random.choice(last_names)

def generate_random_data(num_entries):
    data = []
    for _ in range(num_entries):
        name = generate_random_name()
        email = generate_random_email()
        number = generate_random_number()
        password = generate_random_password()
        confirm_password = password
        data.append((name, email, number, password, confirm_password))
    return data
def generate_random_email():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia', 'James', 'Sophia', 'Robert', 'Ava']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Taylor', 'Anderson']
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'example.com']
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email_name = f"{first_name.lower()}.{last_name.lower()}"
    return email_name + ''.join(random.choices(string.digits, k=2)) + '@' + random.choice(domains)

def generate_random_number():
    return ''.join(random.choices(string.digits, k=10))

def generate_random_password():
    password = "123456"
    return password

def fill_form(driver, name, email, number, password, confirm_password):
    driver.find_element(By.ID,'m_name').send_keys(name)
    driver.find_element(By.ID,'email').send_keys(email)
    driver.find_element(By.ID,'phonenum').send_keys(number)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'c_password').send_keys(confirm_password)

def main():
    num_entries = 50
    random_data = generate_random_data(num_entries)
 # Make sure chromedriver.exe is in the same directory as this script
    options = webdriver.ChromeOptions() 
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options) 

    try:

        for i, entry in enumerate(random_data, 1):
            driver.get('https://halfblack.000webhostapp.com/register_1.php')  
            time.sleep(5)
            name, email, number, password, confirm_password = entry
            fill_form(driver, name, email, number, password, confirm_password)
            driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/form/input').click()  
            sleep(5)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
