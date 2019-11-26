import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import os 
from fake_useragent import UserAgent
def np():
  from bs4 import BeautifulSoup
  import requests
  import random
  global l1
  l1=random.choice(["https://free-proxy-list.net/anonymous-proxy.html","https://www.sslproxies.org/"])
  a=requests.get(l1)
  s=BeautifulSoup(a.content,'html5lib')
  def n():
   global s
   try:
      k={"https":random.choice(list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x:x.text,s.findAll('td')[::8]),(map(lambda x:x.text,s.findAll('td')[1::8])))))))}
      h=requests.get("https://youtube.com",proxies=k)  
      return k
   except:
      pass
  k1=n()
  while k1==None:
   if k1==None:
    k1=n()
  return k1
def start():
 print("welcome to my bot")
 print("taking proxy ")
 a=time.time()
 proxy=np()
 print("using proxy ",proxy)
 print("got real working proxy now starting browser\nnow printing time taken to take proxy ")
 print(time.time()-a,"\n")
 print("Location =")
 ip,p=proxy['https'].split(":")
 os.system("curl https://ipapi.co/"+ip+"/country")
 start2(proxy)
def changeHostFirefox(proxy,b):
    ip, port =proxy['https'].split(":")
    port = int(port)
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    firefox_profile.set_preference("network.proxy.type", 1)
    firefox_profile.set_preference("network.proxy.http", ip)
    firefox_profile.set_preference("network.proxy.http_port", port)
    firefox_profile.set_preference("network.proxy.ssl", ip )
    firefox_profile.set_preference("network.proxy.ssl_port", port)
    firefox_profile.update_preferences() 
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',False)
    firefox_profile.set_preference("media.peerconnection.enabled", False)
    #firefox_profile.set_preference("general.useragent.override",UserAgent().firefox)
    firefox_profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.install_addon('~/.mozilla/firefox/ev5msvbp.default/extensions/{e58d3966-3d76-4cd9-8552-1582fbc800c1}.xpi')
    try:
      driver.get(b)
    except:
        print("something went wrong")
        driver.close()
        start()
    while True:
     try:
      if driver.find_element_by_xpath('//*[@id="skip_button"]').is_displayed():
            driver.find_element_by_xpath('//*[@id="skip_button"]').click()
            break
     except:
       pass
    driver.close()    
def start2(proxy):
 #b=raw_input("enter the link:")
 b="http://evassmat.com/MU0F"
 changeHostFirefox(proxy,b)
start()
