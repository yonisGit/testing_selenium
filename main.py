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
    #test2(browser)
    test_req_one_one(browser)
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
    driver.execute_script("shitToDeleteFast()")
    print(driver.current_url)

    return


def test3(driver):
    driver.get('http://132.73.201.223:12345/attractions/')
    res = driver.execute_script("let x= funcThatReturnsOne();"
                                "return x;")
    print(res)
    return


def test_req_one_one(driver):
    driver.get("http://132.73.201.223:12345/attractions/")
    first_len = driver.execute_script("getRequestAttractions(funcForTest);"
                          "return attr_arr_for_test.length;")
    print(first_len)
    driver.find_element_by_id('add_manually_menu').click()
    driver.find_element_by_id('manual_lat').send_keys('31.2625444444')
    driver.find_element_by_id('manual_lng').send_keys('34.8019111199')
    driver.find_element_by_id('add_manually').click()
    driver.find_element_by_id('attr_name').send_keys('test attraction')
    driver.find_element_by_id('desc').send_keys('test attraction')
    driver.find_element_by_id('submit_btn_add_attr').click()
    driver.find_element_by_id('skip_game_btn').click()
    driver.find_element_by_id('finish_add_aq').click()
    driver.find_element_by_id('finish_add_hint').click()

    if driver.current_url == 'http://132.73.201.223:12345/attractions/':
        print("we are on the right page!")

    second_len = driver.execute_script("getRequestAttractions(funcForTest);"
                                      "return attr_arr_for_test.length;")
    print(second_len)

    if second_len == first_len+1:
        print("test passed!!!")
    else:
        print("test failed ! :( ")







    return


if __name__ == '__main__':
    main()
