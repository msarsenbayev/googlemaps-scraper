# import requests
# from bs4 import BeautifulSoup

# # URL of the page to scrape
# url = "https://www.google.com/maps/place/Holiday+Inn+Aktau+-+Seaside/@43.6634168,51.1261527,14z/data=!4m11!3m10!1s0x41b433aaa618c2eb:0xb5a98c39cf81d915!5m2!4m1!1i2!8m2!3d43.6726733!4d51.1291512!9m1!1b1!16s%2Fg%2F11fb30xrl0?authuser=0&entry=ttu"

# # Fetch the HTML content from the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find the element containing the rating
#     rating_element = soup.find(text="Located at the 17 district, one of the most premium locations in Aktau city, this beautifully located hotel offers a range of entertainment options - swimming pools, waterslides, hamam. Options also include breakfast, lunch and dinner.")

#     # Get the parent element's class
#     if rating_element:
#         parent_element = rating_element.find_parent()
#         class_of_rating = parent_element.get('class')
#         print(class_of_rating)
#     else:
#         print("Element not found.")
# else:
#     print("Failed to fetch the URL.")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize a Chrome WebDriver
driver = webdriver.Chrome()

# URL of the page to scrape
url = "https://www.google.com/maps/place/Holiday+Inn+Aktau+-+Seaside/@43.6634168,51.1261527,14z/data=!4m11!3m10!1s0x41b433aaa618c2eb:0xb5a98c39cf81d915!5m2!4m1!1i2!8m2!3d43.6726733!4d51.1291512!9m1!1b1!16s%2Fg%2F11fb30xrl0?authuser=0&entry=ttu"

# Open the URL
driver.get(url)

# Wait for an element with the specified text to appear on the page
element = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '   AY NEO2 reviews · 3 photos5/5a month ago on GoogleRooms: 5Service: 4Location: 5Like Share')]"))
    #EC.presence_of_element_located((By.XPATH, "//div[contains(@data-ved, '2/5')]"))  
)

# Get the class of the element
class_of_rating = element.get_attribute("class")
print(class_of_rating)

# Close the browser
driver.quit()
