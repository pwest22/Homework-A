from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import *
import time

home_page = None
found_page = None
@given(u'that we have gone to {site}')
def step_impl(context, site):
    context.site = site
    context.browser = webdriver.Chrome()
    if not site.startswith("http"):
        site = "https://" + site
    context.browser.get(site)
    home_page = site
    time.sleep(5)

@when(u'we click on the {logo}')
def step_impl(context, logo):
    web_page = context.browser.find_element(By.PARTIAL_LINK_TEXT, '/')
    found_page = web_page
    #web_page.clear()
    time.sleep(5)

@then(u'we return to {homepage}')
def step_impl(context, homepage):
    link1 = home_page.split('/')
    link2 = found_page.split('/')
    assert link1[2] == link2[2]
