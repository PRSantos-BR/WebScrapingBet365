from selenium import webdriver as wd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (StaleElementReferenceException,
                                        TimeoutException,
                                        ElementClickInterceptedException,
                                        NoSuchElementException)


def objeto_existe(wdw: WebDriverWait, locator: tuple):
    return wdw.until(EC.presence_of_element_located(locator))


def objeto_visivel(wdw: WebDriverWait, locator: tuple):
    return wdw.until(EC.visibility_of_element_located(locator))


def objeto_clicavel(wdw: WebDriverWait, locator: tuple):
    return wdw.until(EC.element_to_be_clickable(locator))


def objeto_interativo(wdw: WebDriverWait, locator: tuple):
    return wdw.until(EC.presence_of_element_located(locator))


def valida_objeto(wdw: WebDriverWait, locator: tuple):
    objeto_retorno = bool

    try:
        if objeto_existe(wdw, locator) and \
                objeto_visivel(wdw, locator) and \
                objeto_clicavel(wdw, locator):
            objeto_retorno = True
    except (StaleElementReferenceException,
            TimeoutException,
            ElementClickInterceptedException,
            NoSuchElementException):
        objeto_retorno = False
    finally:
        return objeto_retorno


def clica_objeto(wdd: wd, wdw: WebDriverWait, locator: tuple):
    # Clica no objeto
    valida_objeto(wdw, locator)
    wdd.find_element(locator[0], locator[1]).click()
