from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./geckodriver"
        )
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        # CONECTAR COM USUÁRIO E SENHA
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

        # CONECTAR COM FACEBOOK
        # driver.find_element_by_class_name("KPnG0").click()
        # time.sleep(5)

        # user_element = driver.find_element_by_xpath("//input[@name='email']")
        # user_element.clear()
        # user_element.send_keys(self.username)
        # time.sleep(3)

        # password_element = driver.find_element_by_xpath("//input[@name='pass']")
        # password_element.clear()
        # password_element.send_keys(self.password)
        # time.sleep(3)
        # password_element.send_keys(Keys.RETURN)
        # time.sleep(10)

        self.comente_nas_fotos_com_a_hashtag(self.username)  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        usernames = []
        formuleiros= []
        # formuleiros = get_names('formuleiros.txt')
        driver = self.driver

        with open('formuleiros.txt', 'r') as fp:
            followers = []
            line = fp.readline()
            cnt = 1
            while line:
                followers.append(line.strip())
                line = fp.readline()
                cnt += 1
        formuleiros = followers

        # driver.get("https://www.instagram.com/" + hashtag + "/")
        # time.sleep(5)
        # driver.find_element_by_xpath("//a[@href='/" + hashtag + "/following/']").click()
        # time.sleep(2)
        
        # for i in range(1, 10):
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(3)

        # hrefs = driver.find_elements_by_tag_name("a")
        # pic_hrefs = [elem.get_attribute("title") for elem in hrefs]

        # for name in pic_hrefs:
        #     if ((name != '') and (name != 'vaquinhabacashi')):
        #         usernames.append(name)

        # print("USUARIOS: " + str(len(usernames)))

        time.sleep(3)
        driver.get("https://www.instagram.com/p/CCGeafTAhcp/")
        time.sleep(5)

        for i in range(0, int(numero_comentarios)):
            try:
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))

                self.type_like_a_person("Tesla UFMG - Seja Tesla, seja o futuro @" + random.choice(formuleiros) + " @" + random.choice(formuleiros), comment_input_box)
                time.sleep(random.randint(15, 20))

                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(40)
            except Exception as e:
                print(e)
                time.sleep(120)
                driver.get("https://www.instagram.com/p/CCGeafTAhcp/")
                time.sleep(3)
                driver.refresh()



nome = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

numero_comentarios = input("Digite o numero de comentarios que deseja fazer: ")

# Entre com o usuário e senha aqui
jhonatanBot = InstagramBot(nome, senha)
jhonatanBot.login()
