from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
#import common

from time import sleep
import os


def validate(MacList=[],reminder=False,conf=None,ap=None,tim=None):
        Present_mac=[]
        res = True
        driver = None
        try:
                #Opening Firefox browser
                try: 
                        driver = webdriver.Firefox()
                        driver.get("http://192.168.100.166/")
                except Exception as e:
                        print e
                sleep(5) # sleep so as to give time to open the page

                frame = driver.find_element_by_xpath('//frame[@name="master"]')
                driver.switch_to_frame(frame)
                action = webdriver.ActionChains(driver)
                action.move_to_element(driver.find_element_by_class_name('spacer25Percent'))
                action.perform()
                #login to GUI 
                inputElement = driver.find_element_by_name("username") 
                inputElement.send_keys('%s'%"admin")
                inputElement = driver.find_element_by_id("password")
                inputElement.send_keys('%s'%"password")
                 
                action.move_to_element(driver.find_element_by_xpath('//input[@onclick="doLogin(event);"]'))
                action.perform()

                inputElement = driver.find_element_by_xpath('//input[@onclick="doLogin(event);"]')
                inputElement.click() #login done
                sleep(4)

                #navigate to wireless page
                frame1 = driver.find_element_by_xpath('//frame[@name="thirdmenu"]')
                frame2 = driver.find_element_by_xpath('//frame[@name="master"]')
                frame = driver.find_element_by_xpath('//frame[@name="header"]')
                frameaction = driver.find_element_by_xpath('//frame[@name="action"]')
                driver.switch_to_frame(frame)
                inputElement = driver.find_element_by_link_text('Wireless').click()
                sleep(2)

                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to_frame(frame2)
                inputElement = driver.find_element_by_xpath('//li[@currentid="1"]').click()
                inputElement = driver.find_element_by_css_selector("input[type='radio'][value='2']").click()
                if not driver.find_element_by_css_selector("input[type='checkbox'][value='1']").is_selected():
                        inputElement = driver.find_element_by_css_selector("input[type='checkbox'][value='1']").click()
                
                #Filling configuration details
                inputElement = driver.find_element_by_id('wirelessSSID0')
                inputElement.clear()
                inputElement.send_keys('%s'%"admin")
                inputElement = driver.find_element_by_css_selector("input[type='radio'][id='idbroadcastSSID1']").click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'channel\']"]/option[text()="1/2.412GHz"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'mcsRate\']"]/option[text()="0 / 7.2 Mbps"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'channelWidth\']"]/option[text()="Dynamic 20/40 MHz"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'guardInterval\']"]/option[text()="Long - 800 ns"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'txPower\']"]/option[text()="Quarter"]').click()
                

                inputElement = driver.find_element_by_xpath('//li[@currentid="2"]').click()
                inputElement = driver.find_element_by_css_selector("input[type='radio'][value='4']").click()
                if not driver.find_element_by_id("cb_chkRadio1").is_selected():
                        inputElement = driver.find_element_by_id("cb_chkRadio1").click()
                inputElement = driver.find_element_by_id('wirelessSSID1')
                inputElement.clear()
                inputElement.send_keys('%s'%"NETGEAR_11na")
                action = webdriver.ActionChains(driver)
                action.move_to_element(driver.find_element_by_class_name('spacer5Percent'))
                action.context_click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'channel\']"]/option[text()="Auto"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'mcsRate\']"]/option[text()="Best"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'channelWidth\']"]/option[text()="20 MHz"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'guardInterval\']"]/option[text()="Auto"]').click()
                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'txPower\']"]/option[text()="Half"]').click()

                #configuration done
                #searching for apply button
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to_frame(frameaction)
                inputElement=driver.find_element_by_id('applyButton').click()
                #apply button clicked 

                #logout the page
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to_frame(frame)
                inputElement=driver.find_element_by_xpath('//img[@onclick="processLogout();"]').click()
                #close firefox
                driver.close()
        except Exception as e:
                print e
if __name__ =='__main__':
        validate()

