from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

'''
Algorithm created by João Filipe "jaozin3bola" da Silva Brandão
'''

'''
This Python algorithm get some informations from the "csgo empire" cassino website
The objective is to create a big dataset for a future Data Science project

I'm using python with some libraries to help me doing that work
Those libraries are:
- selenium to access the website and gather the desired information
- time for pausing the execution and creating a delay for the execution of the algorithm
- pandas to create, manage and export the dataset as csv as well
'''

'''
To use that program you only need to have python 3.8+ installed on your computer and the following libraries as well:
- selenium
- time
- pandas
'''

'''
The dataset have the following table columns:
- moeda(1 to 9) (represents the 9 previous coins on the roulette game)
- ct100 (represents the number of counter-terrorist coins on the last 100 games)
- b100 (represents the number of bonus coins on the last 100 games)
- tr100 (represents the number of terrorist coins on the last 100 games)
- result (represent the coin on the last roulette roll)

The coins on the "moeda(1 to 9)" are being represented according to the following rule:
- 0 represents the counter-terorist coins
- 1 represents the terrorist coins
- 2 represents the bonus coins
'''

'''
To use the algorithm you only need to run the program on your desired compilator
and press ctrl+c to stop the execution
The program wil automatically stop the execution and save the data on a csv file called: "data.csv"
'''

'''
Good work and thanks for using my program :)
'''

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get('https://csgoempire.com')
navegador.implicitly_wait(30)

d = {"moeda1":[],"moeda2":[],"moeda3":[],"moeda4":[],"moeda5":[],"moeda6":[],"moeda7":[],"moeda8":[],"moeda9":[],"ct100":[],"b100":[],"tr100":[],"result":[]}
df = pd.DataFrame(data=d)

try:
    while(True):
        listMoedas = []
        list100 = []
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[4]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[5]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[6]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[7]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[8]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[9]/div').get_attribute('class'))
        listMoedas.append(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[10]/div').get_attribute('class'))
        list100.append(int(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[2]/div[3]').get_attribute("textContent")))
        list100.append(int(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[2]/div[5]').get_attribute("textContent")))
        list100.append(int(navegador.find_element(By.XPATH ,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[3]/div/div[2]/div[7]').get_attribute("textContent")))
        listaFinal=[]
        for i in listMoedas:
            palavra=i.split(" ")
            if(palavra[-1].split("-")[-1]=="ct"):
                listaFinal.append(0)
            elif(palavra[-1].split("-")[-1]=="t"):
                listaFinal.append(1)
            else:
                listaFinal.append(2)
            #listaFinal.append(palavra[-1].split("-")[-1])
        print(listaFinal)
        print(list100)
        new_row = {"moeda1":listaFinal[0],"moeda2":listaFinal[1],"moeda3":listaFinal[2],"moeda4":listaFinal[3],"moeda5":listaFinal[4],"moeda6":listaFinal[5],"moeda7":listaFinal[6],"moeda8":listaFinal[7],"moeda9":listaFinal[8],"ct100":list100[0],"b100":list100[1],"tr100":list100[2],"result":listaFinal[9]}
        df = df.append(new_row, ignore_index=True)
        listaFinal = []
        listMoedas = []
        list100 = []
        time.sleep(32)
except KeyboardInterrupt:
    print('Interrupted!')
    df.to_csv('data.csv')