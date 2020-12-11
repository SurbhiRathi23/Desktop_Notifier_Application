from plyer import notification
import requests
import time
from bs4 import BeautifulSoup



def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'C:\\Users\\Dell\\Downloads\\covid_.ico',
        timeout = 18
    )

def getData(url):
    r= requests.get(url)
    return r.text

i = 0
while i<3:   
    # notifyMe("harry","let thth uiooo")
    myhtml = getData("https://www.mohfw.gov.in/")
    # print(myhtml)
    # myhtml = getData("https://www.worldometers.info/coronavirus/country/india/")
    soup = BeautifulSoup(myhtml, 'html.parser')   

    # for tr in soup.find_all('ul')[2]:
    #     print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    #     print(tr)

    soup.encode('utf-8')




    main =[]
    total_cases =[]
    total_cases = soup.find('li',{'class':'bg-blue'}).get_text().split(" ")
    # print(total_cases)
    x = total_cases[3]
    y=x.split('(')
    z1=y[0]
    print(z1.split("\n")[1])
    main.append(z1.split("\n")[1])
    z2=y[1]
    print(z2.split(")")[0])
    main.append(z2.split(")")[0])
    print(main)






    discharge_cases =[]
    discharge_cases = soup.find('li',{'class':'bg-green'}).get_text().split(" ")
    # print(discharge_cases)
    x = discharge_cases[3]
    y=x.split('(')
    z1=y[0]
    print(z1.split("\n")[1])
    main.append(z1.split("\n")[1])
    z2=y[1]
    print(z2.split(")")[0])
    main.append(z2.split(")")[0])
    print(main)





    d_cases =[]
    d_cases = soup.find('li',{'class':'bg-red'}).get_text().split(" ")
    # print(d_cases)
    x = d_cases[6]
    # print(x)
    y=x.split('(')
    z1=y[0]
    # print(z1)
    print(z1.split("\n")[1])
    main.append(z1.split("\n")[1])
    z2=y[1]
    print(z2.split(")")[0])
    main.append(z2.split(")")[0])
    print(main)


    text = " CASES OF COVID-19 IN INDIA \n"
    nTitle = "\u0332".join(text)
    t1="active"
    # nTitle = 'CASES OF COVID-19 IN INDIA\n\n'
    ntext = f"\n\nACTIVE : {main[0]}              ({main[1]} Dec)\nDISCHARGED: {main[2]}   ({main[3]} Inc)\nDEATHS : {main[4]}             ({main[5]} Inc)"

    notifyMe(nTitle,ntext)

    print("\u0332".join("active"))  # it is a way to underline the text or string
    i = i+1
time.sleep(14)