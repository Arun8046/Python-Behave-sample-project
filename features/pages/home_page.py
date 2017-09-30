from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class HomePage(BasePage):
    project_url = "https://www.trivago.ie/"

    local_directories = {
        "slogan": (
            By.CLASS_NAME, 'hero__line'),
        "searching_bar": (
            By.ID, 'horus-querytext'),
        "searching_button": (
            By.CLASS_NAME, 'horus-btn-search'),
        "filter_on_search_page": (
            By.ID, 'js_filterlist')

    }