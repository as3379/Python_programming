from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#open the first window
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://www.facebook.com")

#get the window handle after the window has opened
window_before = driver.window_handles[0]

window_before_title = driver.title
print(window_before_title)

#open a new window
driver.execute_script("window.open('http://www.twitter.com', 'new window')")

#get the window handle after a new window has opened
window_after = driver.window_handles[1]

#switch on to new child window
driver.switch_to.window(window_after)
time.sleep(10)

window_after_title = driver.title
print(window_after_title)

#Compare and verify that main window and child window title don't match
if window_before_title != window_after_title:
 print('Context switched to Twitter, so the title did not match')
else:
 print('Control did not switch to new window')

#switch back to original window
driver.switch_to.window(window_before)

#Verify that the title now match
if window_before_title == driver.title:
 print('Context returned to parent window. Title now match')

print(driver.title)
driver.quit()