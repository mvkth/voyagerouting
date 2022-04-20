from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CURRENT_XPATH = '/html/body/main/div[3]/div[2]/div[2]/div'
HEIGHT_XPATH = '/html/body/main/div[3]/div[2]/div[3]/div'
DEFAULT_WAIT = 2

path_list = [CURRENT_XPATH,HEIGHT_XPATH]

option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

def parseCurrent(str):
    degree_sign = u'\N{DEGREE SIGN}'
    angle = float(str.split('@')[0].split(degree_sign)[0])
    mag = float(str.split('@')[1][2:])
    return(angle,mag)

def getWeatherFromNS(lon,lat):
    uri = f'https://earth.nullschool.net/#current/ocean/surface/currents/overlay=significant_wave_height/orthographic=-236.48,11.52,2582/loc={lon},{lat}'
    driver.get(uri)
    res = {}
    for path in path_list:
        try:
            WebDriverWait(driver,DEFAULT_WAIT).until(lambda nb: nb.find_element(By.XPATH,path).text != '')
            t = driver.find_element(By.XPATH,path)
        except:
            print(f'No data found for {lon,lat}')
            return
        if(path == CURRENT_XPATH):
            # current is (degrees, m/s)
            res['current'] = parseCurrent(t.text)
        if(path == HEIGHT_XPATH):
            # height is meters
            res['height'] = float(t.text)
    return res

class WeatherTools:
    def getWeather(matrix):
        weather = {}
        for row in matrix:
            for col in row:
                if col is not None:
                    lon, lat = col
                    weather[(lon, lat)] = getWeatherFromNS(lon, lat)
        return weather