import bs4, requests,datetime

miasto = input('podaj miasto w ktorym chcesz sprawdzic pogode, małe litery,bez polskich znakow \n')
url = 'https://www.wprost.pl/pogoda/' + miasto
d = datetime.datetime.today()
while True:
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    miasto1 = soup.find("strong", class_="city-name").text
    dzien = soup.find("span", class_="weather-day").text
    data = soup.find("span", class_="weather-date").text
    temperatura = soup.find("dd", class_="weather-temp").text
    cisnienie = soup.find("dd", class_="weather-pressure").text
    wiatr = soup.find("dd", class_="weather-wind").text
    wilgotnosc = soup.find("dd", class_="weather-humidity").text
    zachmurzenie = soup.find("dd", class_="weather-clouds").text
    print('pogoda na dzien ' + data + ' ' + dzien + ' w mieście ' + miasto1)
    print('dokładna data wraz z godziną ', d)
    print('temeratura: ' + temperatura)
    print('cisnienie: ' + cisnienie)
    print('wiatr: ' + wiatr)
    print('wilgotnosc: ' + wilgotnosc)
    print('zachmurzenie: ' + zachmurzenie)
    break
print('Koniec działania programu, dane pogodowe pochodza ze strony: https://www.wprost.pl/pogoda/')