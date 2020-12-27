print(""" 
██╗██████╗░  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║██████╔╝  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║██╔═══╝░  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║██║░░░░░  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝╚═╝░░░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                            Create By ./Spy ~  """) 
print(" ")
print(" ")
while True:
    import bs4 #import beatifulsoup module
    import requests as r #import requests module as r
    from bs4 import BeautifulSoup as soup #for import beautifulsoup module from bs4 package
    #this is the url get requests for scan ip
    ip = input("Enter IP: ")
    print(" ")
    print(" ")
    url = "https://www.ip-tracker.org/locator/ip-lookup.php?ip="+ip
    #this is used for requests like a user
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189"}     
    #for get response
    res = r.post(url , headers=headers)
    #for get page html
    pagehtml = (res).text
    #for pass page html to bs4
    ps = soup(pagehtml , "html.parser")
    #get tag want to us
    thall = ps.findAll("td", {"class":"tracking"})
    k = ps.findAll("td")
    #for print that tag
    print("_________________________________________________________")
    print(" ")
    print("IP Address : " + thall[1].text)
    print("---------------------------------------------------------")
    print("Continent: "+thall[2].text)
    print("---------------------------------------------------------")
    print("Country and  City: "+k[11].text +"/"+ thall[3].text)
    print("---------------------------------------------------------")
    print("Province: "+thall[4].text)
    print("---------------------------------------------------------")
    print("ISP: "+k[16].text.strip())
    print("---------------------------------------------------------")
    print("Time Zone: "+thall[7].text)
    print("---------------------------------------------------------")
    print("Timezone GMT offset: "+thall[8].text)
    print("---------------------------------------------------------")
    print("Continent Lat/Lon: "+thall[9].text)
    print("---------------------------------------------------------")
    rup = ps.findAll("td", {"class":"myip"})
    print("IP Currency: "+rup[0].text)
    print("---------------------------------------------------------")
    lan = ps.findAll("td", {"width":"80%"})
    print("IP Language: "+lan[0].text)
    print("_________________________________________________________")
