from selenium import webdriver
from bs4 import BeautifulSoup
import os

def main():
    driver = webdriver.Chrome('D:\Python\scraping\chromedriver.exe')
    driver.get('https://www.youtube.com/feed/trending')
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', 'text-wrapper style-scope ytd-video-renderer')
    for item in items:
        try:
            title = item.find('a', id='video-title').text.strip().split('\n')[0]
            channel = item.find('a', 'yt-simple-endpoint style-scope yt-formatted-string').text
            view = item.find('span', 'style-scope ytd-video-meta-block').text
            upload = item.find('div', id='metadata-line').text.strip().split('\n')[1]
            raw = item.find('a', id='video-title')['href']
            link = 'https://www.youtube.com{}'.format(raw)

            dataSet = {}
            dataSet['Title'] = title
            dataSet['Channel'] = channel
            dataSet['View'] = view
            dataSet['Tgl_Upload'] = upload
            dataSet['Link'] = link

            print(dataSet)
        
        except AttributeError as ex:
            print('Error:', ex)

main()
