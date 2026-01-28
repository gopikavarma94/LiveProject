from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
#from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait


class WaitUtility:
    EXPLICIT_WAIT = 5  # Duration in seconds for explicit waits

    def wait_until_clickable(self, driver, element):
        WebDriverWait(driver, self.EXPLICIT_WAIT).until(expected_conditions.element_to_be_clickable(element))

    def wait_until_alert_displayed(self, driver):
        WebDriverWait(driver, self.EXPLICIT_WAIT).until(expected_conditions.alert_is_present())

    def wait_until_cancel_link_is_displayed(self, driver):
        WebDriverWait(driver, self.EXPLICIT_WAIT).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='Cancel']"))
        )

    def wait_until_logout_is_displayed(self, driver):
        WebDriverWait(driver, self.EXPLICIT_WAIT).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a i.fa-power-off"))
        )

    def wait_until_text_is_displayed(self, driver, element, text):
        WebDriverWait(driver, self.EXPLICIT_WAIT).until(
            expected_conditions.text_to_be_present_in_element(element, text)
        )

    def wait_until_element_is_selected(self, driver, element):
        WebDriverWait(driver, self.EXPLICIT_WAIT).until(expected_conditions.element_to_be_selected(element))

    def wait_until_element_is_visible(self, driver, element):
        WebDriverWait(driver, self.EXPLICIT_WAIT).until(expected_conditions.visibility_of(element))

    def wait_until_element_to_be_visible(self, element, timeout=10):
        WebDriverWait(element, timeout).until(expected_conditions.visibility_of_element_located(element))