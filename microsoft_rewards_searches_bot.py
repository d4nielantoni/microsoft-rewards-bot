import time
import random
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class MicrosoftRewardsBot:
    def __init__(self, headless=False):
        self.headless = headless
        self.setup_driver()
        self.search_terms = self.generate_search_terms()
        
    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        if self.headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
    def generate_search_terms(self):
        base_terms = [
            "news", "weather", "sports", "technology", "movies", "music",
            "food", "travel", "health", "science", "art", "books",
            "fashion", "cars", "nature", "history", "games", "education"
        ]
        search_terms = []
        for term in base_terms:
            search_terms.append(term)
            search_terms.append(f"{term} today")
            search_terms.append(f"best {term}")
            search_terms.append(f"{term} 2024")
        random.shuffle(search_terms)
        return search_terms

    def login(self, email, password):
        try:
            self.driver.get("https://login.live.com/")
            
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "loginfmt"))
            )
            email_field.send_keys(email)
            email_field.send_keys(Keys.RETURN)
            
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "passwd"))
            )
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            
            try:
                stay_signed_in = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "idSIButton9"))
                )
                stay_signed_in.click()
            except TimeoutException:
                pass
                
            print("Login successful!")
            
        except Exception as e:
            print(f"Error during login: {str(e)}")
            raise

    def perform_searches(self, num_searches=30):
        print(f"Starting {num_searches} searches...")
        
        for i, search_term in enumerate(self.search_terms[:num_searches], 1):
            try:
                self.driver.get("https://www.bing.com")
                
                search_box = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )
                
                search_box.clear()
                search_box.send_keys(search_term)
                search_box.send_keys(Keys.RETURN)
                
                delay = random.uniform(3, 7)
                print(f"Search {i}/{num_searches}: '{search_term}'")
                time.sleep(delay)
                
            except Exception as e:
                print(f"Error during search '{search_term}': {str(e)}")
                continue

    def close(self):
        self.driver.quit()

def main():
    load_dotenv()
    
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    
    if not email or not password:
        print("Error: Please set EMAIL and PASSWORD in .env file")
        return
    
    headless_mode = True
    
    bot = MicrosoftRewardsBot(headless=headless_mode)
    try:
        bot.login(email, password)
        time.sleep(3)
        
        bot.perform_searches()
        
        print("All searches completed!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        bot.close()

if __name__ == "__main__":
    main()
