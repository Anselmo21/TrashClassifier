#------------------------------------------------------------------------------#
#                                                                              #
#  Purpose :  Extract images from google to form dataset                       #
#  AUTHOR :  Rafael Dolores                                                    #
#  ACKNOWLEDGMENT: This work was done without looking at any external sources  #
#------------------------------------------------------------------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import urllib.request

#Acknowledgement: This code was not taken from any sources. Solely produced by Rafael Dolores
def scrape_images(query, num_images=10, output_folder='images'):
    # Set up the WebDriver
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in your PATH

    try:
        # Navigate to Google Images
        driver.get("https://www.google.com/imghp")

        # Find the search box using its name attribute value
        search_box = driver.find_element("name", "q")

        # Send the query to the search box
        search_box.send_keys(query)

        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)

        # Scroll down to load more images (you may need to adjust this based on the website's behavior)
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # Find all image elements on the page using By.XPATH
        img_elements = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')

        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Download the images
        for i, img_element in enumerate(img_elements[:num_images]):
            img_url = img_element.get_attribute("src")
            img_path = os.path.join(output_folder, f"{query}_{i + 1}.jpg")
            urllib.request.urlretrieve(img_url, img_path)
            print(f"Downloaded image {i + 1}/{num_images}")

    finally:
        # Close the browser in a 'finally' block to ensure it happens even if an exception occurs
        driver.quit()

if __name__ == "__main__":
    query = "plastic garbadge"
    num_images = 10
    scrape_images(query, num_images)
