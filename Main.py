"""
This program is an Ebay web scraper utilizing BeautifulSoup, 
json, and get requests to get product information. 
links.json contains the URLs of the desired products. 
Class Ebay contains the HTML attributes for specific data fields. 
Ebay.txt contains the parsed information.
"""

from bs4 import BeautifulSoup
import requests
import json

class Ebay:

    def __init__(self):
        pass
    
    #HTML tags
    attributes = {
        "name": "vim x-item-title",
        "price": "x-price-primary",
        "asin": "ux-layout-section__textual-display ux-layout-section__textual-display--itemId",
        "seller": "d-stores-info-categories__container__info__section__title"
    }

class Worker:

    def __init__(self):
        self.list = []
        self.dict = {}
    
    #gets info from Ebay class
    def getInfo(self, product):
        for i in product:
            soup = BeautifulSoup(self.r.content, 'html.parser')
            result = soup.find('div', class_ = product[i]).text
            print(result)#prints info to console
            self.list.append(result)

    #sets list for recieved info and adds it to text file
    def saveInfo(self, filename):
        with open(filename, 'a') as file_object:
            file_object.write('\n')
            #adds info to txt file
            for i in self.list:
                file_object.write(i)
                file_object.write('\n')

    #reads links from json file and finds if its from Ebay/Amazon
    def readJSON(self):
        with open("links.json", "r") as json_file:#opens json file holding the links
            links = json.load(json_file)#loads to python
            #loops through elements in json array of dicts, checks source of link(Ebay) and runs through class methods
            for link in links:
                self.r = requests.get(link["link"])
                if link['source'] == 'Ebay':   
                    self.getInfo(Ebay.attributes)
        self.saveInfo('ebay.txt')

run = Worker()
run.readJSON()