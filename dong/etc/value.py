import requests
from bs4 import BeautifulSoup

def call_external_temp():
    req = requests.get('https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?0&MINDB_01&4108&a&K')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    temp_select = soup.select(
            'tr:nth-child(15) > td:nth-child(11)'
    )

    temp_value = 0
    for select in temp_select:
        temp_value = select.text
        return temp_value

def call_external_humidity():
    req = requests.get('https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_guide_test?0&MINDB_01&4108&a&K')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    humidity_select = soup.select(
            'tr:nth-child(15) > td:nth-child(18)'
    )

    humidity_value = 0

    for select in humidity_select:
        humidity_value = select.text
        return humidity_value

def call_external_pm10():
    req = requests.get('https://www.weatheri.co.kr/special/special05_1.php?')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    pm10_select = soup.select(
            'tr:nth-child(14) > td:nth-child(3)'
    )
    
    pm10_value = 0
    for select in pm10_select:
        pm10_value = int(select.text[0:select.text.find('&')])
        return pm10_value

def call_external_pm25():
    req = requests.get('https://www.weatheri.co.kr/special/special05_1.php?')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    pm25_select = soup.select(
            'tr:nth-child(14) > td:nth-child(5)'
    )
    pm25_value = 0
    for select in pm25_select:
        pm25_value = int(select.text[0:select.text.find('&')])
        return pm25_value





if __name__ == '__main__':
    print(type(call_external_temp()))
