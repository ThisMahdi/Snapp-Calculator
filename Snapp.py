# A Simple Code By ThisMahdi | Telegram : @Thisismahdi

# Imports Here
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas
import time

def Snapp_Calculator():
    driver = webdriver.Firefox()
    driver.get("https://app.snapp.taxi/login/")
    phone_number = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="login-input"]')))
    phone_number.click()

    input_phone_number = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="login-input"]')))
    input_phone_number.clear()
    input_phone_number.send_keys("HERE")

    next_step = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[id="next-button"]')))
    next_step.click()

    # in this part you have to enter code manually, don't worry you have 200 secs.

    snapp = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[id="ChoiceCab"]')))
    snapp.click()

    disable_location = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[id="secondary-btn"]')))
    disable_location.click()

    main_menu = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[id="mainMenuButton"]')))
    main_menu.click()

    trips = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'li[id="rides-container"]')))
    trips.click()

    time.sleep(3)

    driver.execute_script("document.getElementById('app').style.direction='ltr';")

    time.sleep(3)

    p_tags = driver.find_elements_by_tag_name("p")

    # TO FOUND INDEXES
    # counter = 0
    # for i in p_tags:
    #     print(f"index {counter} have ====> {i.text}")
    #     counter += 1

    hours_with_snapp = p_tags[3].text
    trips_with_snapp = p_tags[5].text
    kilometers_with_snapp = p_tags[7].text

    print(f"""Hours ==> {hours_with_snapp} hr
    trips ==> {trips_with_snapp} times
    kilometers ==> {kilometers_with_snapp} km
    """)

    counter = 14
    trip_box = driver.find_elements_by_class_name("_3e91kz")
    
    for scroll in p_tags:
        try:
            # scroll down to load all components
            driver.execute_script("arguments[0].scrollIntoView(true);", trip_box[counter])
            time.sleep(5)
            trip_box = driver.find_elements_by_class_name("_3e91kz")
            counter += 15
            time.sleep(2)
        except:
            pass

    money = [*range(12,1437,4)]
    prices = []
    for i in money:
        p_tags = driver.find_elements_by_tag_name("p")
        fixed_price = int(p_tags[i].text.replace("هزینه سفر", "").replace("ریال", "").replace(" ", "").replace(",",""))
        prices.append(fixed_price)

    data = pandas.DataFrame()
    data['Price'] = prices[0:1000]
    data.to_excel('Snapp.xlsx',index=False)

    all_price = sum(prices)
    print(f"Shoma ta be hal ({all_price}) Rial hazine Snapp kardid!")

if __name__ == "__main__":
    Snapp_Calculator()
    
# A Simple Code By ThisMahdi | Telegram : @Thisismahdi
