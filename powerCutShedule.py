from bs4 import BeautifulSoup
import requests
session = requests.Session()

payload = {
    "username": "0505863710"
}
url = "http://lecoapp.leco.lk:8091/LecoWebViews/Outage2022"
try:
    post = session.post(url, data=payload)
    soup = BeautifulSoup(post.text, 'lxml')
    table = soup.find("table", class_="table")
    tr = soup.find_all("tr")
    array = []
    date = []
    powerOff = []
    powerOn = []
    array.append(table.text.split("\n"))
    newArray = []
    for i in range(len(array[0])):
        if(array[0][i] != ""):
            newArray.append(array[0][i])

    for j in range(len(newArray)):
        if(j % 3 == 0):
            date.append(newArray[j])
        elif(j % 3 == 1):
            powerOff.append(newArray[j])
        else:
            powerOn.append(newArray[j])

    for k in range(len(date)):
        print(date[k], powerOff[k], powerOn[k])
    input()


except:
    print("failed to loggin")
