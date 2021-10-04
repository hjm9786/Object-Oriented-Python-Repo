#variables go here
choice = 0
import json
import shutil

#data scraping:
from bs4 import BeautifulSoup
import requests

def getHTML(url):
    response = requests.get(url)
    return response.content

html = getHTML("https://www.timeanddate.com/holidays/us/")


soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', attrs = {'class': "table table--left table--inner-borders-rows table--full-width table--sticky table--holidaycountry"})

A = []
B = []
for row in table.find_all_next('tr'):
    datecells = row.find_all('th')
    if len(datecells) ==1:
        A.append(datecells[0].find(text=True))
    namecells = row.find_all('td')
    if len(namecells)==4:
        B.append(namecells[1].find(text=True))

datedictionary = {A[i]: B[i] for i in range(len(A))}
#print(datedictionary)

date = A
name = B



filename = 'holidays.json'
listObj = []
with open('holidays.json') as fp:
    listObj = json.load(fp)

dict_key = {"date", "name"}
key = str(sorted(dict_key))
datedictionary[key] = True

with open(filename, 'w') as json_file:
    json.dump(datedictionary, json_file,
             indent = 1,
             separators=(',',': '))

#Holday Class

class Holiday:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        
    def get_name(self):
        return self._name
    
    def set_name(self):
        self.name = [name]
        
    def get_date(self):
        return self.date
    
    def set_date(self):
        self.date = [date]
        
    def display_holiday(self):
        print(name, date)
        
    def write_holiday(self, name, date):
        filename = 'holidays.json'
        listObj = []
        with open('holidays.json') as fp:
            listObj = json.load(fp)
        A = []
        A.append(date)
        B = []
        B.append(name)
        adddictionary = {A[i]: B[i] for i in range(len(A))}  

        with open(filename, 'w') as json_file:
            json.dump(adddictionary, json_file,
            indent = 1,
            separators=(',',': '))
        

    def remove_holiday(self, name):
        filename = 'holidays.json'
        obj = json.load(open("holidays.json"))
        if name in B:
            B.pop()
                
        open(filename, 'w').write(
            json.dumps(obj, sort_keys=True, indent=1, separators=(',', ': '))
        )
    
#Choice 1 section
def AddHolidays():
    print("ADD HOLIDAYS")
    print("--------------------")
    print("What is the name of the holiday you would like to add?")
    name = input()
    print("What is the date of that holiday?")
    date = input()
    print("Are you sure you'd like to add this? Please enter y for yes and n for no.")
    addchoice = input()
    if addchoice == 'y':
        print("Got it! Adding the holiday...")
        addholiday = Holiday(name, date)
        Holiday(name, date).write_holiday(name, date)
        print("Added! What else would you like to do?")
    elif addchoice == 'n':
        print("Understood. Anything else you want to do?")
    else:
        print("Sorry, I couldn't understand that. Would you like to do anything else?")


#Choice 2 section
def DeleteHolidays():
    print("DELETE HOLIDAYS")
    print("--------------------")
    print("What is the name of the holiday you'd like to delete?")
    name = input()
    Holiday(name, date).remove_holiday(name)
    print("Thank you!")
    
#Choice 3 section
def SaveHolidays():
    print("SAVE HOLIDAYS")
    print("---------------------")
    print("Would you like to save your changes to a copy of the file? Press y for yes, and n for no.")
    savechoice = input()
    if savechoice == 'y':
        print("Great! Saving your changes...")
        src_path = r"holidays.json"
        dst_path = r"holidayscopy.json"
        shutil.copy(src_path, dst_path)
        print("All done!! Your changes have been saved.")
    elif savechoice == 'n':
        print("Alright! Your save has been cancelled.")
    else:
        print("That was not a valid input. Please use a valid input next time.")


#Choice 4 section
def ViewHolidays():
    print("VIEW HOLIDAYS")
    print("---------------------")
    print("What month of holidays would you like to view? Enter the first 3 letters of that month. (i.e. Jan = January) (Leave blank for current week.)")
    month = input()
    if month is None:
        print("Here are this week's holidays, and the weather:")
        open('holidays.json', 'r')
        filename = 'holidays.json'
        listObj = []
        with open('holidays.json') as fp:
            listObj = json.load(fp)
            print(listObj) where date == None
        weather = api.openweathermap.org/data/2.5/forecast?q={Minneapolis}&appid={1b406ed29a106e93ed43408e778ecd5d}
        print(weather)
    else:
        print("Here are the holidays for the month you requested.")
        listObj = []
        with open('holidays.json') as fp:
            lambda datedictionary.date : date
            print(date)
    print("What else would you like to do?")

#Choice 5 section
def ExitProgram():
    global choice
    while choice == 5:
        print("EXIT PROGRAM")
        print("---------------------")
        print("Are you sure you want to exit? [y/n]")
        exit = input()
        if exit == 'y':
            print("Thank you for using Holiday Manager! See you again soon.")
            choice = 6
        elif exit == 'n':
            print("Alright, what would you like to do now?")



while choice != 6:
    print("Welcome to the holiday manager.")
    print("What would you like to do?")
    print("1. Add a Holiday")
    print("2. Remove a Holiday")
    print("3. Save Holiday List")
    print("4. View Holidays")
    print("5. Exit")
    print("Choosing 6 will force quit the program, and your progress will be lost. ")
    choice = int(input("Please print the number of your choice."))
    if choice == 1:
        AddHolidays()   
    elif choice == 2:
        DeleteHolidays()
    elif choice == 3:
        SaveHolidays()
    elif choice == 4:
        ViewHolidays()
    elif choice == 5:
        ExitProgram()