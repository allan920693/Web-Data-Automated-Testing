# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
import schedule
import time


def simmWebAutoTest():
    
    fromaddr = 'YourEmail@YourEmailDNS.com'
    toaddrs  = 'YourEmail@YourEmailDNS.com'
    username = 'YourEmail@YourEmailDNS.com'
    password = 'YourEmailPassWord'
    server = smtplib.SMTP('smtp.YourEmailDNS.com:XXX')
    thresholdNumber = 0 
    
    browser = webdriver.Firefox()
    browser.get('http://www.simmcloud.com/')
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source)
    
    
    try: 
        strategyCount = soup.select('.content h1#numberOfStrategy span')[0].text
        if int(strategyCount) < thresholdNumber:        
            msg = msg = "\r\n".join([
                  "From: YourEmail@YourEmailDNS.com",
                  "To: YourEmail@YourEmailDNS.com",
                  "Subject: Strategy count abnoraml",
                  "Strategy count = "+str(strategyCount),
                  "Please check XXXXX."
                  ])
            server.ehlo()
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()   
        else: print "Strategy Count pass!" 
        
        try:
            browser.find_element_by_link_text(u"登入").click()
            browser.find_element_by_id("inputUsername").clear()
            browser.find_element_by_id("inputUsername").send_keys("YourEmail@YourEmailDNS.com")
            browser.find_element_by_id("inputPassword").clear()
            browser.find_element_by_id("inputPassword").send_keys("YourAccountPassWord")
            browser.find_element_by_xpath("//button[@type='submit']").click() 
            print "Login Pass" 
            try:
                browser.find_element_by_link_text(u"籌碼策略").click()
                browser.find_element_by_xpath("//div[@id='chip_header']/ul/li[3]/a/p").click()
                browser.find_element_by_xpath("(//button[@type='button'])[4]").click()
                browser.find_element_by_xpath("(//button[@type='button'])[5]").click()
                soup = BeautifulSoup(browser.page_source)
                tableContent = soup.find('div', class_='col-md-4 brokerTables')
                print u"第一名券商: "+ (tableContent.select('.table.table-striped tbody .info td')[1].text)
                print "Broker Pass" 
                try: 
                    browser.find_element_by_link_text(u"策略回測").click()
                    browser.find_element_by_id("itype").click()
                    browser.find_element_by_css_selector("div.box_btn1 > button[type=\"button\"]").click()
                    browser.find_element_by_css_selector("div.Step3_cate_title").click()
                    browser.find_element_by_link_text(u"技術指標交叉").click()
                    browser.find_element_by_link_text(u"開始回測").click()
                    time.sleep(32)
                    soup = BeautifulSoup(browser.page_source)
                    RoIContent = soup.find('div', class_='Step4_main_item')
                            
                    if (RoIContent.select('ul.factor li p .percentValue')[5].text) != "" :           
                        print u"===== 回測結果 ======"
                        print u"交易勝率: {}%".format(RoIContent.select('ul.factor li p .percentValue')[0].text)
                        print u"單筆最高報酬: {}%".format(RoIContent.select('ul.factor li p .percentValue')[1].text)
                        print u"單筆最低報酬: {}%".format(RoIContent.select('ul.factor li p .percentValue')[2].text)
                        print u" 回測年化報酬率: : {}%".format(RoIContent.select('ul.factor li p .percentValue')[3].text)
                        print u" 回測累積報酬率: : {}%".format(RoIContent.select('ul.factor li p .percentValue')[4].text)
                        print u"同期間大盤報酬率: {}%".format(RoIContent.select('ul.factor li p .percentValue')[5].text)
                        print u"=============="                
                        print "BackTest Pass"
                    
                    else: 
                         print "Unable to get BackTest Result!" 
                         msg = msg = "\r\n".join([
                              "From: YourEmail@YourEmailDNS.com",
                              "To: YourEmail@YourEmailDNS.com",
                              "Subject: Unable to get BackTest Result!",
                              "Unable to get BackTest Result!",
                              "Please check the XXXXX."
                              ])
                         server.ehlo()
                         server.starttls()
                         server.login(username,password)
                         server.sendmail(fromaddr, toaddrs, msg)
                         server.quit() 
                    
                except:
                     print "Unable to get BackTest Result!" 
                     msg = msg = "\r\n".join([
                              "From: YourEmail@YourEmailDNS.com",
                              "To: YourEmail@YourEmailDNS.com",
                              "Subject: Unable to get BackTest Result!",
                              "Unable to get BackTest Result!",
                              "Please check the XXXXX."
                              ])
                     server.ehlo()
                     server.starttls()
                     server.login(username,password)
                     server.sendmail(fromaddr, toaddrs, msg)
                     server.quit()  
                    
                
            except:
                print "Unable to get Broker Data!" 
                msg = msg = "\r\n".join([
                      "From: YourEmail@YourEmailDNS.com",
                      "To: YourEmail@YourEmailDNS.com",
                      "Subject: Unable to get Broker Data!",
                      "Unable to get Broker Data!",
                      "Please check the XXXXX."
                      ])
                server.ehlo()
                server.starttls()
                server.login(username,password)
                server.sendmail(fromaddr, toaddrs, msg)
                server.quit()     
        
        except:   
             print "Unable to Log in to SimmCloud!" 
             msg = msg = "\r\n".join([
                  "From: YourEmail@YourEmailDNS.com",
                  "To: YourEmail@YourEmailDNS.com",
                  "Subject: Unable to Log in to SimmCloud!",
                  "Unable to Log in to SimmCloud!",
                  "Please check the XXXXX."
                  ])
             server.ehlo()
             server.starttls()
             server.login(username,password)
             server.sendmail(fromaddr, toaddrs, msg)
             server.quit()   
        
    
    except:
        print("Service down !!!")
        msg = msg = "\r\n".join([
                  "From: YourEmail@YourEmailDNS.com",
                  "To: YourEmail@YourEmailDNS.com",
                  "Subject: Fail to get HTTP response",
                  "Fail to get HTTP response",
                  "Please check the XXXXX."
                  ])
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()             

    browser.close()
    

schedule.every(100).minutes.do(simmWebAutoTest)


while 1:
    schedule.run_pending()
    time.sleep(1)    
    
    