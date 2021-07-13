#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[2]:


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

exepath = "/Users/alexreynolds/Desktop/important/research/coding/geckodriver"
firefoxpath = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"

print("Welcome, Charlotte!")


# In[3]:


binary = FirefoxBinary(firefoxpath)
driver = webdriver.Firefox(firefox_binary=binary,executable_path=exepath)
driver.get('https://app.pivotinteractives.com/login')

print("Now running Selenium :)")


# In[4]:



username = "phys121z@uw.edu"
password = "p121LAB!"
w = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
login = driver.find_element_by_id('email').send_keys(username)
password = driver.find_element_by_id('password').send_keys(password)
submit = driver.find_element_by_class_name('form-button').click()
w2 = WebDriverWait(driver, 5).until(EC.url_contains("dashboard"))
print("Logged in successfully!")


# In[18]:


# edit: get to archived classes
# currently broken
archive = driver.find_element_by_id('button-dropdown-321').click()


# In[20]:


# 
# myclasses = driver.find_element_by_xpath("//a[@class='nav-link'][1]").click()
# w3 = driver.implicitly_wait(5)
labsection = driver.find_element_by_partial_link_text("TA -"[1]).click()
labs = driver.find_elements_by_partial_link_text("SPR21")
lab_parent = driver.find_element_by_partial_link_text("SPR21").click()


# In[6]:


numlabs = driver.find_elements_by_class_name("student-name-link")
print(len(numlabs))
# tells how many students, could be useful for how many times to hit the next button


# In[7]:


w3
firststudent = driver.find_element_by_class_name("student-name-link").click()


# In[8]:


# this worked but im unsure about labs name
labs = labs[:len(numlabs) - 1]
for lab in labs:
    w3
    responses = driver.find_element_by_class_name("next-button").click()


# In[50]:


w3 = driver.implicitly_wait(5)
labsection = driver.find_element_by_partial_link_text("Michael Clancy").click()
labs = driver.find_elements_by_partial_link_text("SUM21")
lab_parent = driver.find_element_by_partial_link_text("SUM21").click()


# In[51]:


numlabs = driver.find_elements_by_class_name("student-name-link")
print(len(numlabs))


# In[53]:


firststudent = driver.find_element_by_class_name("student-name-link").click()
labs = labs[:30]
i = 0
for lab in labs:
    print(i)
    i = i + 1
    # w5 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "heading-title")))
    url = driver.current_url
    print(url)
    responses = driver.find_element_by_class_name("next-button").click()
    


# In[ ]:


driver.quit()


# In[ ]:




