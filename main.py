import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv', header=0)

# Extract the 'Content' column
content_column = df['Content']

# Configure Chrome options for muting audio
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")

# Loop through each video ID in the 'Content' column
for i, video_id in enumerate(content_column[1:], start=1):
    try:
        print(f"Processing video {i} out of {len(content_column) - 1}")
        
        # Construct the YouTube URL
        url = f'https://www.youtube.com/watch/{video_id}'
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            # Open the YouTube video URL
            driver.get(url)
            
            # Wait for the 'Play' button to become clickable and click it
            play_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play']"))
            )
            play_button.click()
            
            # Wait for 10 minutes or until the 'Replay' button becomes clickable
            WebDriverWait(driver, 10 * 60).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@title='Replay']"))
            )
        except Exception as e:
            print(f"Error processing video {i}: {str(e)}")
        finally:
            driver.quit()  # Close the browser window
        
    except Exception as e:
        print(f"Error processing video {i}: {str(e)}")
