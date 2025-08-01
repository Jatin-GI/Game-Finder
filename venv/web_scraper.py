# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time
# import random

# # URL to scrape
# url = 'https://store.steampowered.com/search/?filter=topsellers'

# # Setup Chrome with a user-agent
# options = Options()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

# driver = webdriver.Chrome(options=options)
# driver.get(url)
# time.sleep(3)


# # Data containers
# game_name = []
# launch_date = []
# price = []
# pic = []
# descriptions = []

# # Get game cards
# game_cards = driver.find_elements(By.CSS_SELECTOR, ".search_result_row")
# max_games = 100  # Limit to top 50 games

# for i, game in enumerate(game_cards):
#     if i >= max_games:
#         break
#     try:
#         name = game.find_element(By.CLASS_NAME, "title").text
#         date = game.find_element(By.CLASS_NAME, "search_released").text
#         try:
#             cost = game.find_element(By.CLASS_NAME, "discount_final_price").text
#         except:
#             cost = "No price"
#         image = game.find_element(By.CSS_SELECTOR, ".search_capsule img").get_attribute("src")
#         game_url = game.get_attribute("href")

#         # Open game page in a new tab
#         driver.execute_script("window.open(arguments[0]);", game_url)
#         driver.switch_to.window(driver.window_handles[1])
#         time.sleep(random.uniform(2, 4))  # Human-like wait

#         try:
#             desc = driver.find_element(By.CLASS_NAME, "game_description_snippet").text.strip()
#         except:
#             desc = "No description found"

#         # Close game tab, return to main
#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])

#         # Save all data
#         game_name.append(name)
#         launch_date.append(date)
#         price.append(cost)
#         pic.append(image)
#         descriptions.append(desc)

#         print(f"Scraped: {name}")

#     except Exception as e:
#         print(f"Error with a game: {e}")
#         continue

# # Close browser
# driver.quit()

# # Save to CSV
# df = pd.DataFrame({
#     "Game Name": game_name,
#     "Launch Date": launch_date,
#     "Price": price,
#     "Image": pic,
#     "Description": descriptions
# })
# df.to_csv("steam_games_with_description.csv", index=False)
# print("Saved to steam_games_with_description.csv")


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

# URL to scrape
url = 'https://store.steampowered.com/search/?filter=topsellers'

# Setup Chrome with a user-agent
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
# options.add_argument('--headless')  # Uncomment for headless mode

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(3)

# Scroll to load more results
scroll_pause_time = 2
max_games = 100

while True:
    game_cards = driver.find_elements(By.CSS_SELECTOR, ".search_result_row")
    if len(game_cards) >= max_games:
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

# Data containers
game_name = []
launch_date = []
price = []
pic = []
descriptions = []

# Parse each game card
for i, game in enumerate(driver.find_elements(By.CSS_SELECTOR, ".search_result_row")):
    if i >= max_games:
        break
    try:
        name = game.find_element(By.CLASS_NAME, "title").text
        date = game.find_element(By.CLASS_NAME, "search_released").text
        try:
            cost = game.find_element(By.CLASS_NAME, "discount_final_price").text
        except:
            cost = "No price"
        image = game.find_element(By.CSS_SELECTOR, ".search_capsule img").get_attribute("src")
        game_url = game.get_attribute("href")

        # Open game page in a new tab
        driver.execute_script("window.open(arguments[0]);", game_url)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(random.uniform(2, 4))  # Random delay to mimic human behavior

        try:
            desc = driver.find_element(By.CLASS_NAME, "game_description_snippet").text.strip()
        except:
            desc = "No description found"

        # Close game tab, return to main
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        # Save all data
        game_name.append(name)
        launch_date.append(date)
        price.append(cost)
        pic.append(image)
        descriptions.append(desc)

        print(f"Scraped: {name}")

    except Exception as e:
        print(f"Error with a game: {e}")
        continue

# Close browser
driver.quit()

# Save to CSV
df = pd.DataFrame({
    "Game Name": game_name,
    "Launch Date": launch_date,
    "Price": price,
    "Image": pic,
    "Description": descriptions
})
df.to_csv("steam_games.csv", index=False)
print("Saved to steam_games.csv")
