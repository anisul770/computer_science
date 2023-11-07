from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Replace the below with the contact name or phone number of the person you want to send the message to
recipient = "John Doe"

# Replace with your message
message = "Hello, this is an automated message."

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Scan the QR code
print("Scan the QR code and then press Enter")
input()

# Search for the contact
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys(recipient)
wait.until(EC.presence_of_element_located((By.XPATH, '//span[@title = "{}"]'.format(recipient))))

# Click on the contact
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(recipient))
user.click()

# Type the message
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
msg_box.send_keys(message + Keys.ENTER)

print("Message sent successfully!")
driver.close()
