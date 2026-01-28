import base64
#import datetime
import os
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from pytest_html import extras as html_extras

@pytest.fixture
def browserinstance():
    driver = webdriver.Chrome()  # or Firefox(), Edge(), etc.
    driver.implicitly_wait(10)
    yield driver
@pytest.fixture(params=["chrome", "firefox", "edge"])
def crossbrowser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    yield driver

REPORT_FOLDER = None

def pytest_configure(config):
    global REPORT_FOLDER
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    REPORT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'reports', timestamp))
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    # Override the HTML report output path dynamically
    config.option.htmlpath = os.path.join(REPORT_FOLDER, "report.html")
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
        outcome = yield
        rep = outcome.get_result()

        if rep.when == "call" and rep.failed:
            try:
                driver = item.funcargs.get("browserinstance")  # your driver fixture
                if driver:
                    # 1️⃣ Save screenshot on disk
                    safe_name = rep.nodeid.replace("::", "_").replace("/", "_")
                    screenshot_path = os.path.join(REPORT_FOLDER, f"{safe_name}.png")
                    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
                    driver.save_screenshot(screenshot_path)  # Stores png in reports/

                    # 2️⃣ Attach screenshot to Allure report
                    allure.attach.file(
                        screenshot_path,
                        name="Failure Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )

                    # 3️⃣ Attach screenshot to pytest-html report
                    screenshot_base64 = base64.b64encode(driver.get_screenshot_as_png()).decode("utf-8")
                    extra = getattr(rep, "extra", [])
                    extra.append(html_extras.png(screenshot_base64))  # Attach to pytest-html
                    rep.extra = extra

            except Exception as e:
                print(f"Could not take screenshot: {e}")