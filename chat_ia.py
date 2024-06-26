from http import client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() 
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/profile/login")
driver = webdriver.Chrome(options=chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(10)

def bot():
    try:
        bolinha = driver.find_element(By.CLASS_NAME, 'aumms1qt')
        bolinha = driver.find_elements(By.CLASS_NAME, 'aumms1qt')
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        time.sleep(1)

        todas_msgs = driver.find_elements(By.CLASS_NAME,'_21Ahp')
        todas_msgs_txt = [e.text for e in todas_msgs]
        msg = todas_msgs_txt[-1]
        print(msg)
        time.sleep(10)

        client = OpenAI()

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "você tira minhas dúvidas"},
            {"role": "user", "content": msg}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        resposta = completion.choices[0].message.content
        print(resposta)
        time.sleep(1)
        campo_de_texto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_de_texto.click()
        time.sleep(1)
        campo_de_texto.send_keys(resposta, Keys.ENTER)

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except: 
        print('Aguardando as mensagens!')      
while True:
    bot()