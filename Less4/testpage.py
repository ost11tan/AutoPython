import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml


class TestLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)

    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])

    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])


class OperationsHelper(BasePage, TestLocators):
    with open('./testdata.yaml') as f:
        data = yaml.safe_load(f)

    def enter_login(self, word):
        logging.debug('Enter login')
        login_field = self.find_element(self.ids["LOCATOR_LOGIN_FIELD"])
        login_field.clear()
        if login_field:
            login_field.send_keys(word)
        else:
            logging.error('Поле для ввода логина не найдено')

    def enter_pass(self, word):
        logging.debug('Enter passwd')
        login_field = self.find_element(self.ids["LOCATOR_PASS_FIELD"])
        login_field.clear()
        if login_field:
            login_field.send_keys(word)
        else:
            logging.error('Поле для ввода пароля не найдено')

    def click_login_button(self):
        logging.debug('Click login button')
        btn = self.find_element(self.ids['LOCATOR_LOGIN_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')

    def click_contact_button(self):
        logging.debug('Click contact button')
        btn = self.find_element(self.ids['LOCATOR_CONTACT_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')

    def click_contact_send_button(self):
        logging.debug('Click contact button')
        btn = self.find_element(self.ids['LOCATOR_CONTACT_SEND_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')

    def get_error_text(self):
        logging.debug('Error')
        error_field = self.find_element(self.ids["LOCATOR_ERROR_FIELD"])
        if error_field:
            text = error_field.text
            return text
        else:
            logging.error('Окно ошибки не обнаружено')

    def get_login_text(self):
        logging.debug('Enter passwd')
        element_successful_login = self.find_element(self.ids["LOCATOR_HELLO_LOGIN"])
        if element_successful_login:
            return element_successful_login.text
        else:
            logging.error('Текст не обнаружен')

    def click_create_post_btn(self):
        logging.debug('Click create new post button')
        btn = self.find_element(self.ids['LOCATOR_CREATE_POST_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')

    def enter_post_title(self, word):
        logging.debug('post_title')
        title_field = self.find_element(self.ids["LOCATOR_POST_TITLE"])
        if title_field:
            title_field.clear()
            title_field.send_keys(word)
        else:
            logging.error('Поле для ввода не найдено')


    def enter_post_description(self, word):
        logging.debug('post_description')
        description_field = self.find_element(self.ids["LOCATOR_POST_DESCRIPTION"])
        if description_field:
            description_field.clear()
            description_field.send_keys(word)
        else:
            logging.error('Поле для ввода не найдено')


    def enter_post_content(self, word):
        logging.debug('post_content')
        content_field = self.find_element(self.ids["LOCATOR_POST_CONTENT"])
        if content_field:
            content_field.clear()
            content_field.send_keys(word)
        else:
            logging.error('Поле для ввода не найдено')

    def click_save_btn(self):
        logging.debug('Click save button')
        btn = self.find_element(self.ids['LOCATOR_SAVE_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')

    def get_added_post_title(self):
        logging.debug('post_title')
        post_title = self.find_element(self.ids["LOCATOR_POST_ADDED"])
        if post_title:
            return post_title.text
        else:
            logging.error('Поле для ввода не найдено')

    def enter_contact_name(self, word):
        logging.debug('Enter contact name')
        login_field = self.find_element(self.ids["LOCATOR_CONTACT_NAME"])
        login_field.clear()
        if login_field:
            login_field.send_keys(word)
        else:
            logging.error('Поле для ввода не найдено')

    def enter_contact_email(self, word):
        logging.debug('Enter contact email')
        login_field = self.find_element(self.ids["LOCATOR_CONTACT_EMAIL"])
        login_field.clear()
        if login_field:
            login_field.send_keys(word)
        else:
            logging.error('Поле для ввода не найдено')

    def enter_contact_content(self, word):
        logging.debug('Enter contact content')
        login_field = self.find_element(self.ids["LOCATOR_CONTACT_CONTENT"])
        login_field.clear()
        if login_field:
            login_field.send_keys(word)
        else:
            logging.error('Поле для ввода не найдено')

    def switch_alert(self):
        logging.info("Switch alert")
        alert = self.driver.switch_to.alert
        logging.info(alert.text)
        return alert.text


    def click_home_step1_btn(self):
        logging.debug('Click home button')
        btn = self.find_element(self.ids['LOCATOR_HOME'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')

    def click_home_step2_btn(self):
        logging.debug('Click home button')
        btn = self.find_element(self.ids['LOCATOR_HOME_STEP2'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')
"""
    def  (self, word):
        logging.debug('FIND_DESCRIPTION')
        content_field = self.find_element(self.ids["LOCATOR_FIND_DESCRIPTION"])
        if content_field:
            content_field.clear()
            content_field.send_keys(word)
        else:
            logging.error('Поле для ввода не найдено')"""


