from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Defina o modelo de dados para o corpo da requisição
class LoginData(BaseModel):
    usuario: str
    senha: str

# URL da página de login e de acesso protegido
LOGIN_URL = 'https://sigaa.unifesspa.edu.br/sigaa/verTelaLogin.do'
# Substitua pelo ID de um elemento que só aparece após o login
ELEMENTO_PROTEGIDO_ID_1 = 'painel-mensagem-envio_c' 
ELEMENTO_PROTEGIDO_ID_2 = 'portais' 
ELEMENTO_PROTEGIDO_ID_3 = 'perfil-docente' 

def extracting_service(data: LoginData):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    
    try:
        # Abra a página de login
        driver.get(LOGIN_URL)

        # Espere até que os campos de usuário e senha estejam visíveis
        # A espera explícita é uma boa prática para evitar erros
        wait = WebDriverWait(driver, 10)
        campo_usuario = wait.until(EC.presence_of_element_located((By.NAME, 'user.login')))
        campo_senha = driver.find_element(By.NAME, 'user.senha')
        botao_entrar = driver.find_element(By.XPATH, '//input[@type="submit"]')

        # Preencha os campos de usuário e senha
        campo_usuario.send_keys(data.usuario)
        campo_senha.send_keys(data.senha)

        print("Campos preenchidos. Clicando no botão 'Entrar'...")

        # Clique no botão de submissão do formulário
        botao_entrar.click()

        # Espere por um elemento da página protegida para confirmar o login
        # Substitua 'elemento_da_pagina_protegida' por algo que só aparece após o login
        wait.until(EC.presence_of_element_located((By.ID, ELEMENTO_PROTEGIDO_ID_1)))

        print("Login bem-sucedido! 🎉")

        # Agora você pode raspar o conteúdo da página protegida com Selenium
        # Exemplo: Imprimir o título da página
        print(f"Título da página: {driver.title}")

        
        link_xpath = '//a[contains(@href, "escolhaCalendario")]'
        # link_calendario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '2025-4')))
        link_calendario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_xpath)))
        print(f"Encontrei o link: {link_calendario.text}")
        
        # Clicar no link
        link_calendario.click()
        wait.until(EC.presence_of_element_located((By.ID, ELEMENTO_PROTEGIDO_ID_2)))
        print("Periodo clicado com sucesso! 🎉")
        print(f"Título da página: {driver.title}")


        link_xpath = '//a[contains(@href, "verPortalDiscente")]'
        # link_calendario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '2025-4')))
        link_calendario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_xpath)))
        print(f"Encontrei o link: {link_calendario.text}")
        
        # Clicar no link
        link_calendario.click()
        wait.until(EC.presence_of_element_located((By.ID, ELEMENTO_PROTEGIDO_ID_3)))
        print("Portal clicado com sucesso! 🎉")
        print(f"Título da página: {driver.title}")
        # Para raspar o HTML da página atual e usar com BeautifulSoup:
        html_content = driver.page_source
        driver.quit()
        return html_content
    except Exception as err:
        return err