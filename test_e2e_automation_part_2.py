import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_e2e_automation():
    """
    Test E2E automation website with selenium
    """
    path = '/Users/ran/Desktop/chromedriver'  # The Path of the ChromeDriver
    driver = webdriver.Chrome(path)  # The initialization of the driver
    driver.maximize_window()  # Maximize the web window
    driver.implicitly_wait(3)
    driver.get('https://stephenchou1017.github.io/scheduler/#/')  # Entering the URL
    time.sleep(5)
    infinite_scroll = driver.find_element(by=By.CSS_SELECTOR,
                                          value='#root > div > div:nth-child(1) > ul > li:nth-child(19) > a > span')
    infinite_scroll.click()  # Click on the button of 'infinite scroll'
    time.sleep(5)
    month = driver.find_element(by=By.CSS_SELECTOR,
                                value='#RBS-Scheduler-root > thead > tr > td > div > div:nth-child(2) > div > '
                                      'label:nth-child(2) '
                                      '> span:nth-child(2) > span')
    month.click() # Click on the button of 'month'
    time.sleep(5)
    list_of_events = (driver.find_elements(By.CLASS_NAME, "timeline-event")) # Handles the list of events in the current month

    new_event1 = driver.find_element(by=By.CSS_SELECTOR,
                                     value='#RBS-Scheduler-root > tbody > tr > td:nth-child(2) > div > div:nth-child(2) > '
                                           'div > div.scheduler-content > table > tbody > tr:nth-child(2) > td > div > '
                                           'a:nth-child(2)') # Adding a new event to the current month

    new_event2 = driver.find_element(by=By.CSS_SELECTOR,
                                     value='#RBS-Scheduler-root > tbody > tr > td:nth-child(2) > div > div:nth-child(2) > '
                                           'div > div.scheduler-content > table > tbody > tr:nth-child(2) > td > div > '
                                           'a:nth-child(2)')  # Adding another event to the current month

    new_list_of_events = [new_event1, new_event2]  # Handles the new list of events with the ones added
    assert (len(new_list_of_events) + len(list_of_events)) > len(list_of_events), f'The num of new events expected to be bigger then the events before adding new events'

    one_month_later = driver.find_element(by=By.CSS_SELECTOR,
                                          value='#RBS-Scheduler-root > thead > tr > td > div > div:nth-child(1) > div > '
                                                'i.anticon.anticon-right.icon-nav > svg')
    one_month_later.click()  # Click on the button of next month

    time.sleep(5)

    list_of_events_month_later = (driver.find_elements(By.CLASS_NAME, "timeline-event"))   # Handles the list of events month later
    assert len(list_of_events_month_later) < (len(new_list_of_events) + len(list_of_events)), f'The num of events in the next month expected to be smaller than the events in the past month '

    original_date = driver.find_element(by=By.CSS_SELECTOR,
                                        value='#RBS-Scheduler-root > thead > tr > td > div > div:nth-child(1) > div > '
                                              'i.anticon.anticon-left.icon-nav > svg')
    original_date.click()  # Click on the button of previous month

    list_of_events_original_date = (driver.find_elements(By.CLASS_NAME, "timeline-event"))  # Handles the list of events from the original date
    assert (len(list_of_events_original_date)) == (len(new_list_of_events) + len(list_of_events)), f'The events that were created expected be exist, Instead the new events created were not saved'
