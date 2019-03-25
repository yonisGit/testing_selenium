# from Servers import *
# from src.deku import *
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
    browser.get("http://10.0.0.4:12345/pick_aq/")
    browser.find_element_by_id('finish_pick_aq').click()


    return


if __name__ == '__main__':
    main()
