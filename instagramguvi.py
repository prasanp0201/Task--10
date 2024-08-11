from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Instagram credentials - Actual credentials have been given and tested the code whereas its not mentioned here 
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Set up the WebDriver
driver = webdriver.Chrome()

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the login elements to be present
wait = WebDriverWait(driver, 50)

# Locate and enter username
username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_input.send_keys(USERNAME)

# Locate and enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(PASSWORD)

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the home page to load and handle the "Save Info" and "Turn on Notifications" prompts
try:
    # Handle "Save Info" prompt
    save_info_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    save_info_prompt.click()
except Exception as e:
    print("Save Info prompt not found or already handled")

try:
    # Handle "Turn on Notifications" prompt
    notifications_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
    notifications_prompt.click()
except Exception as e:
    print("Notifications prompt not found or already handled")

# Wait for the home page to fully load
time.sleep(5)

# Navigate to the specified Instagram profile
profile_url = "https://www.instagram.com/guviofficial/"
driver.get(profile_url)

# Wait for the profile page to load
time.sleep(5)

# Define XPaths for followers and following elements
followers_xpath = "(//a[contains(@href,'/followers')]/span)[1]"
following_xpath = "(//a[contains(@href,'/following')]/span)[1]"

# Locate the elements and extract their text
followers_element = wait.until(EC.presence_of_element_located((By.XPATH, followers_xpath)))
following_element = wait.until(EC.presence_of_element_located((By.XPATH, following_xpath)))

# Extract the number of followers and following
followers = followers_element.get_property('title')
following = following_element.text

# Print the results
print(f"Followers: {followers}")
print(f"Following: {following}")

# Close the browser
# driver.quit()
