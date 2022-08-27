import time
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait as Wdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (StaleElementReferenceException,
                                        TimeoutException,
                                        ElementClickInterceptedException,
                                        NoSuchElementException)
from bs4 import BeautifulSoup as Bs
from selenium.webdriver.support.wait import WebDriverWait

def bet365_online(url_principal):
    # Opções para o Driver
    options = Options()
    options.page_load_strategy = 'none'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user_agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36')

    # Infoca browse
    print('Iniciando driver ...')
    with wd.Chrome() as WdChrome:
        # with wd.Chrome(options=options) as WdChrome:

        # Requisitando página ...
        print('Requisitando página {} ...'.format(url_principal))
        WdChrome.get(url_principal + '/#/IP/B1')

        # Aguardando renderização da página ...
        print('Aguardando renderização da página ...')
        wdw = Wdw(WdChrome, 30)

        # Aguardando receber título da página ...
        print('Aguardando receber título da página ...')
        wdw.until(EC.title_is('bet365 - Apostas Desportivas Online'))

        # Maximizando drive
        print('Maximizando drive ...')
        WdChrome.maximize_window()

        time.sleep(30)
