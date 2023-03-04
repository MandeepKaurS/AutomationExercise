from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 1. launching browser
edge_path = r"C:\Edge Browser Driver\msedgedriver.exe"
service = Service(executable_path=edge_path)
driver = webdriver.Edge(service=service)

# 2. Navigating to the URL
driver.get('https://automationexercise.com/')
driver.implicitly_wait(10)

# 3. Verifying that home page is visible successfully
assert "Automation Exercise" in driver.title

# 4. Adding products to cart

driver.find_element(By.CSS_SELECTOR, 'a[data-product-id="1"].add-to-cart').click()
time.sleep(2)

# 5. Click Cart Button
driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a').click()

# 6. Verify that cart page is displayed
assert "Automation Exercise - Checkout" in driver.title

# 7. Click Proceed To Checkout
driver.find_element(By.XPATH, "//*[@id='do_action']/div[1]/div/div/a").click()
time.sleep(1)

# 8. Click 'Register / Login' button
driver.find_element(By.XPATH, '//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a/u').click()
time.sleep(1)

# 9. Fill all details in Signup and create account
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys('Brenda Kaya')
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys('BKaya@gmail.com')
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
time.sleep(1)

#Enter Account Information
driver.find_element(By.ID, 'id_gender1').send_keys(Keys.LEFT)
driver.find_element(By.ID, 'password').send_keys('JoeChrist123')
driver.find_element(By.ID, 'days').send_keys('28')
driver.find_element(By.ID, 'months').send_keys('February')
driver.find_element(By.ID,'years').send_keys('1993')
driver.find_element(By.ID, 'first_name').send_keys('Brenda')
driver.find_element(By.ID, 'last_name').send_keys('Kaya')
driver.find_element(By.ID, 'address1').send_keys('3')
driver.find_element(By.ID, 'address2').send_keys('Penstock Street')
driver.find_element(By.ID, 'country').send_keys('Canada')
driver.find_element(By.ID, 'state').send_keys('Ontario')
driver.find_element(By.ID, 'city').send_keys('Brampton')
driver.find_element(By.ID, 'zipcode').send_keys('L6P2J5')
driver.find_element(By.NAME, 'mobile_number').send_keys('9876500126')
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button').click()
time.sleep(2)

# 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
assert 'Automation Exercise - Account Created'
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(12)

# 11. Verify ' Logged in as username' at top
username_element = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a/b')


# Get the text of the username element
username_text = username_element.text

# Check that the username matches the expected value
assert username_text == 'Brenda Kaya', f"Expected username 'Brenda Kaya', but found '{username_text}'"

# If the assertion passes, the following code will execute
print('Successfully logged in as Brenda Kaya')
time.sleep(3)

# 12. Clicking Cart Button
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a').click()
time.sleep(2)

# 13. Proceeding to Checkout
driver.find_element(By.XPATH, "//*[@id='do_action']/div[1]/div/div/a").click()
time.sleep(1)

# 14. Verify Address Details and Review Your Order
expected_address_text = """
Mrs. Brenda Kaya
3
Penstock Street
Brampton Ontario L6P2J5
Canada
9876500126
"""
# Locate the address section
address_section = driver.find_element(By.ID, "address_delivery")

# Extract the address information
firstname_lastname = address_section.find_element(By.CLASS_NAME, "address_firstname").text
address2 = address_section.find_elements(By.CLASS_NAME,"address_address2")[1].text
city_state_postcode = address_section.find_element(By.CLASS_NAME,"address_city").text
country = address_section.find_element(By.CLASS_NAME,"address_country_name").text
phone = address_section.find_element(By.CLASS_NAME,"address_phone").text

# Print the extracted information
assert firstname_lastname=='Mrs. Brenda Kaya', f"Full Name: {firstname_lastname}"
assert address2 == '3', f"Address Line 2: {address2}"
assert city_state_postcode=='Brampton Ontario L6P2J5', f"City, State, and Postcode: {city_state_postcode}"
assert country=='Canada', f"Country: {country}"
assert phone =='9876500126', f"Phone Number: {phone}"



#15. Enter description in comment text area and click 'Place Order'
driver.find_element(By.NAME, "message").send_keys("Is there a return or exchange policy available in case the product does not meet my expectations?")
driver.find_element(By.XPATH,"//*[@id='cart_items']/div/div[7]/a").click()
time.sleep(10)

#16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
driver.find_element(By.NAME, 'name_on_card').send_keys('Mandeep Kaur')
driver.find_element(By.NAME,'card_number').send_keys('987654321')
driver.find_element(By.NAME,'cvc').send_keys('214')
driver.find_element(By.NAME,'expiry_month').send_keys(10)
driver.find_element(By.NAME,'expiry_year').send_keys(2025)

#17. Click 'Pay and Confirm Order' button
driver.find_element(By.XPATH, '//*[@id="submit"]').click()
time.sleep(5)

# 18. Verify success message 'Your order has been placed successfully!'
assert driver.find_element(By.CSS_SELECTOR, "h2[data-qa='order-placed']").text == 'ORDER PLACED!'

# 19. Click 'Delete Account' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()

# 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
assert driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2').text == 'ACCOUNT DELETED!'
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(3)





