import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
from selenium import webdriver

url = "https://www.google.com/maps/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
elements_with_class = soup.find_all(class_='RfnDt')

class ReviewScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize a Chrome WebDriver

    def __scroll(self):
        # TODO: Subject to changes
        scrollable_div = self.driver.find_element_by_css_selector('div.m6QErb.DxyBCb.kA9KIf.dS8AEf')
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_reviews(self, offset):

        # scroll to load reviews
        self.__scroll()

        # wait for other reviews to load (ajax)
        time.sleep(4)

        # expand review text
        self.__expand_reviews()

        # parse reviews
        response = BeautifulSoup(self.driver.page_source, 'html.parser')
        # TODO: Subject to changes
        rblock = response.find_all('div', class_='jftiEf fontBodyMedium ')
        parsed_reviews = []
        for index, review in enumerate(rblock):
            if index >= offset:
                r = self.__parse(review)
                parsed_reviews.append(r)

                # logging to std out
                print(r)

        return parsed_reviews
        #print(parsed_reviews)


if __name__ == "__main__":
    # Create an instance of the ReviewScraper class
    scraper = ReviewScraper()

    # Call the get_reviews function and specify the desired offset
    offset_value = 0
    parsed_reviews = scraper.get_reviews(offset_value)

    # Print the extracted review data
    for review_data in parsed_reviews:
        print(review_data)