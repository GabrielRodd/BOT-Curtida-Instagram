#Project: BOT to like a instagram post
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']

    '''
    Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''

    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_download = 'C:\\Users\\Gabri\\Downloads'

    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_download,
        
        # Atualiza o diretório para diretório a cima
        'download.directory_upgrade': True,

        # Seta se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        
        # Desabilita notificações
        "profile.default_content_setting_values.notifications":2,

        # Permite multiplos downloads
        "profile.default_content_setting_values.automatic_downloads":1,
    })

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )

    return driver, wait

driver, wait = iniciar_driver()
driver.get('https://www.instagram.com/')
driver.maximize_window()

# Type user in user field
user_field = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@name='username']")))
user_field.send_keys("*****")
sleep(3)
# Type password in password field
password_field = driver.find_element(By.XPATH,"//input[@name='password']")
password_field.send_keys("*****")
sleep(3)

# Click enter/login button
login_button = driver.find_element(By.XPATH,"//div[text()='Entrar']")
login_button.click()

# Click in "not now" button
not_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[text()='Agora não']")))
not_button.click()

# Enter in profile 
driver.get('https://www.instagram.com/devaprender/')

# Click in the last post
posts = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,"//div[@class='_aagu']")))
posts[0].click()

chain = ActionChains(driver)

# Like or not like
try: # Not like
    red_button = wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR,"svg[aria-label='Descurtir']")))
    if red_button is not None:
        chain.pause(1).send_keys(Keys.ESCAPE).perform()
except: # Like
    white_button = wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR,"svg[aria-label='Curtir']")))
    if white_button is not None:
        chain.move_to_element(white_button[0]).pause(1).click().pause(1).send_keys(Keys.ESCAPE).perform()



input('')













 