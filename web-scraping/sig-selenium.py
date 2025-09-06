from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Defina a URL de login
login_url = 'https://sigaa.unifesspa.edu.br/sigaa/verTelaLogin.do'

# Credenciais de login (substitua com suas próprias)
usuario = 'ruan.vieira'
senha = 'x261433y'
options = Options()
# Adicione o argumento para rodar em modo headless
options.add_argument('--headless')
# Outros argumentos úteis
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Crie uma instância do navegador com as opções
driver = webdriver.Chrome(options=options)

try:
    # Abra a página de login
    driver.get(login_url)

    # Espere até que os campos de usuário e senha estejam visíveis
    # A espera explícita é uma boa prática para evitar erros
    wait = WebDriverWait(driver, 10)
    campo_usuario = wait.until(EC.presence_of_element_located((By.NAME, 'user.login')))
    campo_senha = driver.find_element(By.NAME, 'user.senha')
    botao_entrar = driver.find_element(By.XPATH, '//input[@type="submit"]')

    # Preencha os campos de usuário e senha
    campo_usuario.send_keys(usuario)
    campo_senha.send_keys(senha)

    print("Campos preenchidos. Clicando no botão 'Entrar'...")

    # Clique no botão de submissão do formulário
    botao_entrar.click()

    # Espere por um elemento da página protegida para confirmar o login
    # Substitua 'elemento_da_pagina_protegida' por algo que só aparece após o login
    wait.until(EC.presence_of_element_located((By.ID, 'painel-mensagem-envio_c')))

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
    wait.until(EC.presence_of_element_located((By.ID, 'portais')))
    print("Periodo clicado com sucesso! 🎉")
    print(f"Título da página: {driver.title}")


    link_xpath = '//a[contains(@href, "verPortalDiscente")]'
    # link_calendario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '2025-4')))
    link_calendario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_xpath)))
    print(f"Encontrei o link: {link_calendario.text}")
    
    # Clicar no link
    link_calendario.click()
    wait.until(EC.presence_of_element_located((By.ID, 'perfil-docente')))
    print("Portal clicado com sucesso! 🎉")
    print(f"Título da página: {driver.title}")
    # Para raspar o HTML da página atual e usar com BeautifulSoup:
    html_content = driver.page_source
    # Agora você pode passar html_content para BeautifulSoup
    # ... (exemplo da resposta anterior)

finally:
    # Feche o navegador no final
    driver.quit()