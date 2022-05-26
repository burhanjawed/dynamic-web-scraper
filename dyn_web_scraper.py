from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = 'https://www.youtube.com/channel/UCoOjH8D2XAgjzQlneM2W0EQ/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome()
driver.get(url)

videos = driver.find_elements_by_class_name(
    'style-scope ytd-grid-video-renderer')

video_list = []

for video in videos:
    title = video.find_element(
        by=By.XPATH, value='.//*[@id="video-title"]').text
    views = video.find_element(
        by=By.XPATH, value='.//*[@id="metadata-line"]/span[1]').text
    date = video.find_element(
        by=By.XPATH, value='.//*[@id="metadata-line"]/span[2]').text
    vid_item = {
        'title': title,
        'views': views,
        'date_added': date
    }

    video_list.append(vid_item)

df = pd.DataFrame(video_list)

print(df)
