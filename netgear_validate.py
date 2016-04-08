from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tomlpython
from time import sleep

f=lambda param,testSuitName,defaultValue:testSuitName[param] if param in testSuitName.keys() else defaultValue

def read_config(config_path="./conf.ini"):
        try:
            with open(config_path) as datafile:
                return tomlpython.parse(datafile)
        except Exception as file_missing:
            print str(file_missing)
            return 0

def validate(conf=None,testcaseName=None,driver=None):
        try:
                sleep(4)
                #navigate to wireless page
                driver.switch_to.window(driver.window_handles[0])
                frame1 = driver.find_element_by_xpath('//frame[@name="thirdmenu"]')
                frame2 = driver.find_element_by_xpath('//frame[@name="master"]')
                frame = driver.find_element_by_xpath('//frame[@name="header"]')
                frameaction = driver.find_element_by_xpath('//frame[@name="action"]')
                driver.switch_to_frame(frame)
                inputElement = driver.find_element_by_link_text('Wireless').click()
                sleep(5)

                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to_frame(frame2)
                if 'PROTOCOL' not in conf[testcaseName].keys() or conf[testcaseName]['PROTOCOL'] == "":
                		raise Exception("PROTOCOL not given in **conf.ini** file for testcase **%s"%testcaseName)
                if 'TURN_RADIO_ON' not in conf[testcaseName].keys() or conf[testcaseName]['TURN_RADIO_ON']=="":
                                conf[testcaseName]['TURN_RADIO_ON']= "1"
                if 'WIRELESSMODE' not in conf[testcaseName].keys() or conf[testcaseName]['WIRELESSMODE'] == "":
                        if conf[testcaseName]['PROTOCOL'] == '802.11b/bg/ng':
                                conf[testcaseName]['WIRELESSMODE']= "11ng"
                        else:
                                conf[testcaseName]['WIRELESSMODE']= "11na"

                if conf[testcaseName]['PROTOCOL'] == "802.11b/bg/ng":
               		inputElement = driver.find_element_by_xpath('//li[@currentid="1"]').click()
                	if conf[testcaseName]['WIRELESSMODE'] == "11b":
                		inputElement = driver.find_element_by_css_selector("input[type='radio'][value='0']").click()
                		
                        	if conf[testcaseName]['TURN_RADIO_ON']=="1":
 		    			if not driver.find_element_by_id("cb_chkRadio0").is_selected():
                                        	inputElement = driver.find_element_by_id("cb_chkRadio0").click()
                                        	testFlag = 0
							# click on the link that opens a new window
				elif conf[testcaseName]['TURN_RADIO_ON']=='0':
					if driver.find_element_by_id("cb_chkRadio0").is_selected():
                        	                inputElement = driver.find_element_by_id("cb_chkRadio0").click()
                        	                testFlag =1
			        try:
	                                alert=driver.switch_to_alert()
				        alert.accept()
	                        except:
	                    		pass
                                sleep(5)
                                if "testFlag" not in locals().keys() or not testFlag:
		                    inputElement = driver.find_element_by_id('wirelessSSID0')
		                    inputElement.clear()
		                    inputElement.send_keys('%s'%f('SSID_NAME',conf[testcaseName],"NETGEAR_11na"))
		                    sleep(2)
	                            ##########################################################################
	                            ##HAVE TO SOLVE FOR YES NO OPTION#########################################
	                            ##########################################################################	                    
		                    #inputElement = driver.find_element_by_css_selector("input[type='radio'][id='idbroadcastSSID1']").click()
		                    ##########################################################################
		                    inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'channel\']"]/option[text()="%s"]'%f('CHANNEL',conf[testcaseName],"Auto")).click()
		                    inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'dataRate\']"]/option[text()="%s"]'%f('DATARATE',conf[testcaseName],"Best")).click()
		                    inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'txPower\']"]/option[text()="%s"]'%f('TXPOWER',conf[testcaseName],"Full")).click()

	                elif conf[testcaseName]['WIRELESSMODE'] == "11bg":
	                        inputElement = driver.find_element_by_css_selector("input[type='radio'][value='1']").click()
	                	if conf[testcaseName]['TURN_RADIO_ON']=="1":    
	 		    	        if not driver.find_element_by_id("cb_chkRadio0").is_selected():
	                                        inputElement = driver.find_element_by_id("cb_chkRadio0").click()
	                        	        testFlag=0
	                        elif conf[testcaseName]['TURN_RADIO_ON']=="0":
	                    	        if driver.find_element_by_id("cb_chkRadio0").is_selected():
	                        	        inputElement = driver.find_element_by_id("cb_chkRadio0").click()
	                        	        testFlag=1
								# click on the link that opens a new window
			    	try:
	                    	        alert=driver.switch_to_alert()
					alert.accept()
	                    	except:
	                    	        pass
                                sleep(5)
	                        if "testFlag" not in locals().keys() or not testFlag:
		                    inputElement = driver.find_element_by_id('wirelessSSID0')
		                    inputElement.clear()
		                    inputElement.send_keys('%s'%f('SSID_NAME',conf[testcaseName],"NETGEAR_11na"))
		                    sleep(2)
	                            ##########################################################################
	                            ##HAVE TO SOLVE FOR YES NO OPTION#########################################
	                            ##########################################################################	                    
		                    #inputElement = driver.find_element_by_css_selector("input[type='radio'][id='idbroadcastSSID1']").click()
		                    ##########################################################################
		                    inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'channel\']"]/option[text()="%s"]'%f('CHANNEL',conf[testcaseName],"Auto")).click()
		                    inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'dataRate\']"]/option[text()="%s"]'%f('DATARATE',conf[testcaseName],"Best")).click()
		                    inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'txPower\']"]/option[text()="%s"]'%f('TXPOWER',conf[testcaseName],"Full")).click()
	                elif conf[testcaseName]['WIRELESSMODE'] == "11ng":
			        inputElement = driver.find_element_by_css_selector("input[type='radio'][value='2']").click()
			        if conf[testcaseName]['TURN_RADIO_ON']=="1": 
			                if not driver.find_element_by_css_selector("input[type='checkbox'][value='1']").is_selected():
			                        inputElement = driver.find_element_by_css_selector("input[type='checkbox'][value='1']").click()
                                                testFlag=0
			        elif conf[testcaseName]['TURN_RADIO_ON']=="0": 
			                if driver.find_element_by_css_selector("input[type='checkbox'][value='1']").is_selected():
			                        inputElement = driver.find_element_by_css_selector("input[type='checkbox'][value='1']").click()
                                                testFlag=1
                                try:
	                                alert=driver.switch_to_alert()
					alert.accept()
	                        except:
	                    	        pass
			        if "testFlag" not in locals().keys() or not testFlag:
			                #Filling configuration details
			                inputElement = driver.find_element_by_id('wirelessSSID0')
			                inputElement.clear()
			                inputElement.send_keys('%s'%f('SSID_NAME',conf[testcaseName],"NETGEAR"))
			                if 'BROADCAST' in conf[testcaseName].keys() and conf[testcaseName]['BROADCAST'] == '0':
			                	inputElement = driver.find_element_by_css_selector\
                                                ("input[type='radio'][id='idbroadcastSSID1'][value='1']").click()
			                else:
			                	inputElement = driver.find_element_by_css_selector\
                                                ("input[type='radio'][id='idbroadcastSSID1'][value='0']").click()
                                        
			                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'channel\']"]/option[text()="%s"]'%f('CHANNEL',conf[testcaseName],"Auto")).click()
			                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'mcsRate\']"]/option[text()="%s"]'%f('MSCRATE',conf[testcaseName],"Best")).click()
			                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'channelWidth\']"]/option[text()="%s"]'%f('CHANNELWIDHT',conf[testcaseName],"Dynamic 20/40 MHz")).click()
			                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'guardInterval\']"]/option[text()="%s"]'%f('GUARDINTERVAL',conf[testcaseName],"Auto")).click()
			                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan0\'][\'txPower\']"]/option[text()="%s"]'%f('TXPOWER',conf[testcaseName],"Full")).click()
		                
                                   
                if conf[testcaseName]['PROTOCOL'] == "802.11a/na":
                        inputElement = driver.find_element_by_xpath('//li[@currentid="2"]').click()
                        if conf[testcaseName]['WIRELESSMODE'] == '11na':
                	        inputElement = driver.find_element_by_css_selector("input[type='radio'][value='4']").click()
                                if conf[testcaseName]['TURN_RADIO_ON']=="1":
                	                if not driver.find_element_by_id("cb_chkRadio1").is_selected():
                                                inputElement = driver.find_element_by_id("cb_chkRadio1").click()
                                                testFlag=0
                                if conf[testcaseName]['TURN_RADIO_ON']=="0":
                                        if not driver.find_element_by_id("cb_chkRadio1").is_selected():
                                                inputElement = driver.find_element_by_id("cb_chkRadio1").click()
                                                testFlag=1
                                try:
                                        alert=driver.switch_to_alert()
                                        alert.accept()
                                except:
                                        pass
                                sleep(5)
                                if "testFlag" not in locals().keys() or not testFlag:
					        # click on the link that opens a new window
	                                inputElement = driver.find_element_by_id('wirelessSSID1')
	                                inputElement.clear()
	                                inputElement.send_keys('%s'%f('SSID_NAME',conf[testcaseName],"NETGEAR_11na"))
                                        ##########################################################################
                                        ##HAVE TO SOLVE FOR YES NO OPTION#########################################
                                        ##########################################################################	              
	                                #action = webdriver.ActionChains(driver)
	                                #action.move_to_element(driver.find_element_by_class_name('spacer5Percent'))
	                                #action.context_click()
                                        
                                    #    driver.switch_to.window(driver.window_handles[0])
	                                #frame = driver.find_element_by_xpath('//frame[@name="master"]')
    	                            #    driver.switch_to_frame(frame)
                                    #    action = webdriver.ActionChains(driver)
                                    #    action.move_to_element(driver.find_element_by_class_name('spacer5Percent'))
                                    #    action.perform()
                                    #    if 'BROADCAST' in conf[testcaseName].keys() and conf[testcaseName]['BROADCAST'] == '0':
                                    #            inputElement = driver.find_element_by_css_selector("input[type='radio'][id='idbroadcastSSID1'][value='1']").click()
                                    #    else:
                                    #            inputElement = driver.find_element_by_css_selector("input[type='radio'][id='idbroadcastSSID1'][value='0']").click()
	                                ##########################################################################
	                                inputElement = driver.find_element_by_xpath('//input[@name="system[\'vapSettings\'][\'vapSettingTable\'][\'wlan1\'][\'vap0\'][\'hideNetworkName\']"]').click()
	                                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'channel\']"]/option[text()="%s"]'%f('CHANNEL',conf[testcaseName],"Auto")).click()
	                                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'mcsRate\']"]/option[text()="%s"]'%f('MSCRATE',conf[testcaseName],"Best")).click()
	                                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'channelWidth\']"]/option[text()="%s"]'%f('CHANNELWIDHT',conf[testcaseName],"Dynamic 20/40 MHz")).click()
	                                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'guardInterval\']"]/option[text()="%s"]'%f('GUARDINTERVAL',conf[testcaseName],"Auto")).click()
	                                inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'txPower\']"]/option[text()="%s"]'%f('TXPOWER',conf[testcaseName],"Full")).click()
                        elif conf[testcaseName]['WIRELESSMODE']== '11a':
                                inputElement = driver.find_element_by_css_selector("input[type='radio'][value='3']").click()
                                if conf[testcaseName]['TURN_RADIO_ON']=="1":
 		                        if not driver.find_element_by_id("cb_chkRadio1").is_selected():
                                                inputElement = driver.find_element_by_id("cb_chkRadio1").click()
                                                testFlag=0

                                if conf[testcaseName]['TURN_RADIO_ON']=="0":
                                        if driver.find_element_by_id("cb_chkRadio1").is_selected():
                                                inputElement = driver.find_element_by_id("cb_chkRadio1").click()
                                                testFlag=1
					# click on the link that opens a new window
               		        try:
                    	                alert=driver.switch_to_alert()
			                alert.accept()
                                except:
                    	                pass
                                sleep(5)
                                if "testFlag" not in locals().keys() or not testFlag:
                                        inputElement = driver.find_element_by_id('wirelessSSID1')
                                        inputElement.clear()
                                        inputElement.send_keys('%s'%f('SSID_NAME',conf[testcaseName],"NETGEAR_11na"))
                                        ##########################################################################
                                        ##HAVE TO SOLVE FOR YES NO OPTION#########################################
                                        ##########################################################################
                                        #action = webdriver.ActionChains(driver)
                                        #sleep(5)
                                        #action.move_to_element(driver.find_element_by_class_name('spacer5Percent'))
                                        #print dir(action)
                    
                                        #action.move_to_element(driver.find_element_by_css_selector("input[type='radio'][value='1']"))
                                        #action.click()
                                        #inputElement = driver.find_element_by_css_selector("input[type='radio'][value='1']").click()
                                        #<input name="system['vapSettings']['vapSettingTable']['wlan1']['vap0']['hideNetworkName']" 
                                        #id="idbroadcastSSID1" label=
                                        #"Broadcast Wireless Network Name (SSID)" onclick="setActiveContent();" value="1" type="radio">

    				        #<input name="system['vapSettings']['vapSettingTable']['wlan1']['vap0']['hideNetworkName']"
					#id="idbroadcastSSID1" label=
					#"Broadcast Wireless Network Name (SSID)" onclick="setActiveContent();
                                        #" value="0" checked="checked" type="radio">

					###########################################################################

                                        inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'channel\']"]/option[text()="%s"]'%f('CHANNEL',conf[testcaseName],"Auto")).click()
                                        inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'dataRate\']"]/option[text()="%s"]'%f('DATARATE',conf[testcaseName],"Best")).click()
                                        inputElement = driver.find_element_by_xpath('//select[@name="system[\'wlanSettings\'][\'wlanSettingTable\'][\'wlan1\'][\'txPower\']"]/option[text()="%s"]'%f('TXPOWER',conf[testcaseName],"Full")).click()



                #configuration done
                #searching for apply button
                
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to_frame(frameaction)
                inputElement=driver.find_element_by_id('applyButton').click()

                
                driver.switch_to.window(driver.window_handles[0])
	        frame = driver.find_element_by_xpath('//frame[@name="master"]')
    	        driver.switch_to_frame(frame)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.ID,'inlineTabLink1')))
        except Exception as e:
                raise Exception(e)

if __name__ =='__main__':
        from re import match
        conf=read_config()
        if 'LOGIN CREDENTIALS' not in conf.keys():
                conf['LOGIN CREDENTIALS'] = ''
        #Opening Firefox browser
        try: 
            driver = webdriver.Firefox()
            driver.get(f('url',conf['LOGIN CREDENTIALS'],"http://192.168.100.166/"))

	    frame = driver.find_element_by_xpath('//frame[@name="master"]')
    	    driver.switch_to_frame(frame)
            action = webdriver.ActionChains(driver)
            action.move_to_element(driver.find_element_by_class_name('spacer25Percent'))
            action.perform()
            #login to GUI 
            inputElement = driver.find_element_by_name("username") 
            inputElement.send_keys('%s'%f('username',conf['LOGIN CREDENTIALS'],"admin"))
            inputElement = driver.find_element_by_id("password")
            inputElement.send_keys('%s'%f('password',conf['LOGIN CREDENTIALS'],"password"))
                 
       	    action.move_to_element(driver.find_element_by_xpath('//input[@onclick="doLogin(event);"]'))
            action.perform()

            inputElement = driver.find_element_by_xpath('//input[@onclick="doLogin(event);"]')
            inputElement.click() #login done
            try:
            	alert=driver.switch_to_alert()
            	alert.accept()
            except:
          	pass
        except Exception as e:
            print e
            driver.close()
        sleep(5) # sleep so as to give time to open the page
        for value in conf.keys():	
        	if not match("[^TESTCASE.]",value):
        		print value
        		try:
        			validate(conf,value,driver)
        		except Exception as e:
        		        driver.refresh()   
        			print e
                                continue            
        #logout the page
        try:
        	driver.switch_to.window(driver.window_handles[0])
        	frame = driver.find_element_by_xpath('//frame[@name="header"]')
        	driver.switch_to_frame(frame)
        	inputElement=driver.find_element_by_xpath('//img[@onclick="processLogout();"]').click()
        	driver.close()
        except Exception as e:
        	print "Error form logout section",e
	        driver.close()			
