# Randomly select a restaurant for cankaya 100. yil above 9 points. 
# Randomly pick a desginated amount of items
# Add to basket

# Yemeksepeti 100. Yil https://www.yemeksepeti.com/ankara/cankaya-isci-bloklari-mah-100-yil
# Above 8.5 Points https://www.yemeksepeti.com/ankara/cankaya-isci-bloklari-mah-100-yil#tp:8.5
# https://www.yemeksepeti.com/ankara/cankaya-isci-bloklari-mah-100-yil#tp:9|mbt:10

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os 
import random
from tkinter import *
import tkinter
import tkinter.messagebox

def choose_restaurant():
    wd = webdriver.Firefox()
    # build the google query
    restaurant_url = 'https://www.yemeksepeti.com/ankara/cankaya-isci-bloklari-mah-100-yil#tp:{}'

    # load the page
    wd.get(restaurant_url.format(Entry.get(point)))
    urls = []
    restaurants = wd.find_elements_by_css_selector('a.restaurantName')
    for span in restaurants:
        urls = urls + [span.get_attribute('href')]
    choose_meal(random.choice(urls),Entry.get(meals),wd)

def choose_meal(link,num_of_meals,wd): 
    wd.get(link)
    meals = wd.find_elements_by_css_selector('a.getProductDetail')    
    to_click = []
    i = 0
    while(i < int(num_of_meals)):
        to_click = to_click + [random.choice(meals)]
        i += 1
    for meal in to_click:
        time.sleep(5)
        meal.location_once_scrolled_into_view
        wd.maximize_window()
        # time.sleep(10)
        element = wd.find_element_by_xpath("//div[@class='row']")
        wd.execute_script("arguments[0].style.visibility='hidden'", element)
        element2 = wd.find_element_by_xpath("//div[@class='container']")
        wd.execute_script("arguments[0].style.visibility='hidden'", element2)
        element3 = wd.find_element_by_xpath("//div[@class='inner']")
        wd.execute_script("arguments[0].style.visibility='hidden'", element3)
        meal.click()
        time.sleep(5)   
        button = wd.find_element_by_xpath("//button[@class ='ys-btn ys-btn-primary ys-btn-lg pull-right add-to-basket']")
        button.location_once_scrolled_into_view
        button.click()

top = tkinter.Tk()
L1 = Label(top, text = "Restaurant Picker",).grid(row=0, column=1)
L2 = Label(top, text="Points: ",).grid(row=1,column=0)
Label(top, text="Meals: ",).grid(row=2,column=0)
point = Entry(top, bd =5)
point.grid(row=1,column=1)
meals = Entry(top,bd=5)
meals.grid(row=2,column=1)
B=Button(top, text="FOOD",command = choose_restaurant).grid(row=5,column=1,)

top.mainloop()
