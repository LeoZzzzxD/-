import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CONSTA = 3
HEADER = {'User-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}
PARAMS = {'types': 'opersvodki', 'group':'all', 'end_date': '04.01.1945', 'begin_date': '01.01.1941', 'use_main_string': 'false', 'static_hash': '756880f7c115e1a1770c29b649c678cav1'}

def get_and_parse_data():

  counter = 1
  driver = webdriver.Chrome()
  
  try:
    with open("data_from_page.txt", "w") as file_ya:
     while counter != CONSTA:
      
      finally_list_of_data = list()
      new_list_of_operation_name = []
      link = f"https://pamyat-naroda.ru/documents/?group=all&use_main_string=true&begin_date=01.01.1920&types=opersvodki:rasporyajeniya:otcheti:peregovori:jbd:direktivi:prikazi:posnatovleniya:dokladi:raporti:doneseniya:svedeniya:plani:plani_operaciy:karti:shemi:spravki:drugie&page={counter}"
      driver.get(link)
      time.sleep(2)
      first_info = driver.find_elements_by_class_name('heroes-list-item-name')
    
      another_one_info = driver.find_elements_by_class_name('heroes-list-item-name-wrap')
    
      links = []
      id = []
      i = 0
    
      for (info, info1) in zip(first_info, another_one_info):
        links.append(info.get_attribute('href'))
        new_list_of_operation_name.append(info1.find_element_by_tag_name('a').text)
      
      counter_for_ya = 0
      i = 0
      for info2 in links:
      
        dict_of_data = dict()
        driver.get(info2)
        time.sleep(2)
        second_info = driver.find_element_by_class_name('archive-data')
        new_list_of_strings = second_info.text.split("\n")

      
        dict_of_data['Дата создания документа'] = new_list_of_strings[i].split(':')[1]
        dict_of_data['Фонд'] = new_list_of_strings[i + 1].split(':')[2].split(',')[0]
        dict_of_data['Опись'] = new_list_of_strings[i + 1].split(':')[3].split(',')[0]
        dict_of_data['Дело'] = new_list_of_strings[i + 1].split(':')[4].split(',')[0]
        dict_of_data['Авторы документа'] = new_list_of_strings[i + 2].split(':')[1]
        dict_of_data['Название операции'] = new_list_of_operation_name[counter_for_ya]
        dict_of_data['ID'] = info2.split('?')[1].split('=')[1].split('&')[0]
        counter_for_ya += 1
        finally_list_of_data.append(dict_of_data)
   
      with open("data_from_page.txt", "a") as file_ya:
        print("Страница:", counter, "\n", file = file_ya)

        for j in range(len(finally_list_of_data)):  
          print("ID:", finally_list_of_data[j]['ID'], " ", "Фонд:", finally_list_of_data[j]['Фонд'], " ", "Опись:", finally_list_of_data[j]['Опись'], " ", "Дело:", finally_list_of_data[j]['Дело'], " ", 
          "Название операции:", finally_list_of_data[j]['Название операции'], " ", "Авторы документа:", finally_list_of_data[j]['Авторы документа'], " ", "Дата создания документа:", finally_list_of_data[j]['Дата создания документа'], "\n", file = file_ya)   
      counter += 1  
  except:
    print("Работа программы завершилась не корректно!")
    return

if __name__ == "__main__":
  get_and_parse_data() 




 