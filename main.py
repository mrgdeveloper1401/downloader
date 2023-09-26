#python script to download instagram, facebook and twitter images and videos

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service
import os
from urllib.request import urlopen
import m3u8
import re

class Downloader():
    def __init__(self):
        # choose from chrome or firefox
        self.driver, self.service = self.get_driver('firefox')

    def get_driver(self, _type):
        if _type == 'firefox':
            service = firefox_service('./geckodriver' if os.name == 'posix' else 'geckodriver.exe')
            service.start()
            op = webdriver.FirefoxOptions()
            op.add_argument('--headless')
            op.add_argument("--no-sandbox")
            op.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Firefox(op, service)
            return driver, service
        else:
            service = chrome_service('./chromedriver' if os.name == 'posix' else 'chromedriver.exe')
            service.start()
            op = webdriver.ChromeOptions()
            op.add_argument('--headless')
            op.add_argument("--no-sandbox")
            op.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(op, service)
            return driver, service

    def download_file(self, _address, _fname, _type=0):
        if _address:
            try:
                if _type == 0:
                    r = requests.get(str(_address).replace('blob:', ''))
                    with open(_fname,'wb') as f:
                        f.write(r.content)
                    return True
                elif _type == 1:
                    reg_res = re.search('(https:\/\/.+\.com)', _address)
                    if reg_res and reg_res.group(1):
                        _domain = reg_res.group(1)
                        r = requests.get(str(_address).replace('blob:', ''))
                        r.encoding = 'utf-8'
                        m3u8_master = m3u8.loads(r.text)
                        playlist_url = m3u8_master.data['playlists'][0]['uri']
                        if str(playlist_url).startswith('/'):
                            playlist_url = _domain + playlist_url
                        play_r = requests.get(playlist_url)
                        m3u8_master_play = m3u8.loads(play_r.text)
                        m3_data=(m3u8_master_play.data)
                        m3_datas = m3_data['segments'][0]['uri']
                        with open(_fname,'wb') as fs:
                            for segments in m3_data['segments']:
                                uri = segments['uri']
                                if str(uri).startswith('/'):
                                    uri = _domain + uri
                                r = requests.get(uri)
                                fs.write(r.content)
                        return True
            except Exception as err:
                print('ERROR: ', err)
                return False
        return False

    def insta_downloader(self, link, _type=''):
        if not link:
            return None

        self.driver.get(link)
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'video.x5yr21d, img.x5yr21d')))
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            item = None

            if str(link).startswith('https://www.instagram.com/p'):
                _type = 'post'
            elif str(link).startswith('https://www.instagram.com/reel'):
                _type = 'reel'

            if _type == 'reel':
                item = soup.find('video', class_='x5yr21d')
            elif _type == 'post':
                item = soup.find('img', class_='x5yr21d')
            if item:
                img_url = item['src']
                if img_url:
                    return img_url
        except TimeoutException:
            # timeout error
            return None
        return None

    def facebook_downloader(self, link):
        if not link:
            return None
        
        # x85a59c x193iq5w x4fas0m x19kjcj4 --> photos
        # x1lliihq x5yr21d xh8yej3 --> vids

        self.driver.get(link)
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'video.x5yr21d, img.x85a59c')))
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            item = None
            item = soup.find('video', class_='x5yr21d')
            if item:
                # playScript = """
                # var _video = document.querySelector('video.x5yr21d');
                # if(_video)
                #   _video.play();
                # """
                # _ = driver.execute_script(playScript)

                networkScript = """
                var performance = window.performance || window.webkitPerformance || {};
                var network = performance.getEntries() || {};
                return network;
                """
                networkRequests = self.driver.execute_script(networkScript)
                URLs = [request['name'] for request in networkRequests if '.webm?' in request['name']]
                if not URLs:
                    URLs = [request['name'] for request in networkRequests if '.mp4?' in request['name']]
                temp_list = []
                if URLs:
                    reg_patt = '(https.+)&bytestart=\\d+&byteend=\\d+'
                    r = re.search(reg_patt, URLs[len(URLs)-1])
                    if r and r.group(1):
                        _link = r.group(1)
                        site = urlopen(_link)
                        meta = site.info()
                        temp_list.append({'link':_link, 'length':int(meta.get_all("Content-Length")[0])})
                if temp_list:
                    return max(temp_list, key=lambda x:x['length'])['link']
            if not item:
                item = soup.find('img', class_='x85a59c')
                if item:
                    img_url = item['src']
                    if img_url:
                        return img_url

        except TimeoutException:
            # timeout error
            return None
        return None

    def twitter_downloader(self, link):
        if not link:
            return None

        # css-9pa8cd

        self.driver.get(link)
        delay = 15 # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "video[aria-label='Embedded video'], div[data-testid='tweetPhoto'] img.css-9pa8cd")))
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            item = None
            item = soup.find('video', attrs={'aria-label' : 'Embedded video'})
            if item:
                networkScript = """
                var performance = window.performance || window.webkitPerformance || {};
                var network = performance.getEntries() || {};
                return network;
                """
                networkRequests = self.driver.execute_script(networkScript)
                URLs = [request['name'] for request in networkRequests if '.m3u8?variant_version' in request['name']]
                if URLs:
                    return URLs[0]

            if not item:
                temp_div = soup.find('div', attrs={'data-testid' : 'tweetPhoto'})
                item = temp_div.find('img', class_='css-9pa8cd')
                if item and item['src']:
                        return item['src']
        except TimeoutException:
            # timeout error
            return None
        return None

if __name__ == '__main__':

    downloader = Downloader()

    ## instagram test
    downloader.download_file(downloader.insta_downloader('https://www.instagram.com/p/Cxc2JJlo0dO/?igshid=MzRlODBiNWFlZA=='), 'insta_pic.png')
    downloader.download_file(downloader.insta_downloader('https://www.instagram.com/reel/Cwe9XNhs2rW/?igshid=MzRlODBiNWFlZA=='), 'insta_pic.mp4')


    ## facebook test
    # print(downloader.download_file(downloader.facebook_downloader('https://www.facebook.com/photo?fbid=290446380300668&set=a.159887996689841'), 'face_pic_0.png'))
    # print(downloader.download_file(downloader.facebook_downloader('https://www.facebook.com/photo/?fbid=298871506205788&set=ecnf.100044429349683'), 'face_pic_1.png'))
    # print(downloader.download_file(downloader.facebook_downloader('https://www.facebook.com/100091643051763/videos/1557091221454503'), 'face_pic_0.mp4'))
    # print(downloader.download_file(downloader.facebook_downloader('https://www.facebook.com/RealMadrid/videos/10151647364904953/'), 'face_pic_1.mp4'))
    # print(downloader.download_file(downloader.facebook_downloader('https://www.facebook.com/100022404092086/videos/320064193910671?idorvanity=327965031431036'), 'face_pic_2.mp4'))
    # print(downloader.download_file(downloader.facebook_downloader('https://www.facebook.com/100022283855775/videos/849794686532196'), 'face_pic_3.mp4'))
    # print(downloader.download_file(downloader.facebook_downloader('https://fb.watch/niDvk3KM4F/'), 'face_pic_4.mp4'))
    # print(downloader.download_file(downloader.facebook_downloader('https://www.facebook.com/100000599485610/videos/963642741367509?idorvanity=734349487814105'), 'face_pic_5.mp4'))


    ## twitter test
    # print(downloader.download_file(downloader.twitter_downloader('https://twitter.com/Cristiano/status/1520339985559347202'), 'twitter_pic_0.png'))
    # print(downloader.download_file(downloader.twitter_downloader('https://twitter.com/TheScarlett1/status/686295824834400256'), 'twitter_pic_1.png'))
    # print(downloader.download_file(downloader.twitter_downloader('https://twitter.com/Adele/status/1445388436773425163'), 'twitter_vid_0.mp4', 1)))
    # print(downloader.download_file(downloader.twitter_downloader('https://twitter.com/Iron_Man/status/1071027626632929280'), 'twitter_vid_1.mp4', 1))
    # print(downloader.download_file(downloader.twitter_downloader('https://twitter.com/Iron_Man/status/1266486174484295681'), 'twitter_vid_2.mp4', 1))

    print('success')
