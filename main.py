# from Servers import *
# from src.deku import *
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as req

#ip = 'http://132.73.201.223'
def main():
    # download_path = 'D:\_Guy\d9anime\downloaded'
    # download('kyoukai no kanata', [12])
    # print(find('steins gate'))
    # print(find('nanatsu no taizai imashime no fukkatsu'))
    # print(find('yuru camp'))
    # print(fetch_url('http://httpbin.org/headers').replace('\\n', '\n'))
    # deku.download_episodes(anime_name='A Place Further Than The Universe', path='.', server=RapidVideo)
    # deku.download_episodes(anime_name='A Place Further Than The Universe', path='.', server=MyCloud)
    # get_video_links_by_name('A Place Further Than The Universe')
    opts = Options()
    opts.set_headless()
    browser = Chrome(options=opts)
    #test1(browser)
    test2(browser)
    return

def test1(driver):
    driver.get("http://132.73.201.223:12345/pick_aq/")
    driver.find_element_by_id('finish_pick_aq').click()
    if(driver.current_url=='http://132.73.201.223:12345/attractions/'):
        print('test passed!')
    else:
        print('test failed!')

    return

def test2(driver):
    driver.get('http://132.73.201.223:12345/attractions/')
    # points_arr = driver.find_element_by_id('points_arr_for_test').get_attribute('value')
    # print(points_arr)
    driver.execute_script("shitToDeleteFast()")
    #myscript = settings.shitToDeleteFast()
    # driver = webdriver.PhantomJS()
    # driver.get('http://132.73.201.223:12345/attractions/')
    # result = driver.execute_script(myscript)
    print(driver.current_url)
    # driver.quit()
    #resp = req.get('http://132.73.201.223:12344/managementsystem/attraction/?format=json')

    # driver.find_element_by_id('finish_pick_aq').click()
    # if (driver.current_url == 'http://132.73.201.223:12345/attractions/'):
    #     print('test passed!')
    # else:
    #     print('test failed!')

    return

if __name__ == '__main__':
    main()
