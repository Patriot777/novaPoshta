import requests
from bs4 import BeautifulSoup

track = input("Введіть свій трек код: ")
#track = "20450244638521"
try:
    userCode = "https://novaposhta.ua/tracking/?cargo_number=" + track
    site = requests.get(userCode)

    soup = BeautifulSoup(site.text, 'html.parser')

    DeliveryAddress = soup.find_all('tr')[2].text.strip()    #Адреса доставки
    Address = DeliveryAddress[15:]

    Rout = soup.find_all('tr')[1].text.strip()               #Маршрут
    rout = Rout[7:]

    DateOfArrival = soup.find_all('tr')[3].text.strip()      #Дата прибуття
    dateofArrival = DateOfArrival[13:]
    print("Маршрут: " + rout)
    print("Адреса доставки - " + Address)
    print("Дата доставки: " + dateofArrival)
    print("")
    exitProgram = input("Натисніть любу кнопку для виходу з програми...")
#print(statusTime)
except:
    print("Виникла помилка, перевірте свій трекер")
    exitLose = input("Натисніть Enter для виходу з програми...")