from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import date

"""
Instalações necessárias :
COMANDOS PARA USAR NO TERMINAL PYTHON:
- pip install pytest-playwright
- playwright install
Link para doc : https://playwright.dev/python/docs/intro
"""

def download_relatorio(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) # Ao settar headless = True , o navegador irá rodar em modo "invisível" 
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    ############                    LOGIN NA WRS                    #############

    page.goto("https://wrs.solutions.iqvia.com/login.php")
    page.get_by_label("Usuário").click()
    page.get_by_label("Usuário").fill("**")##aqui usuario
    page.get_by_label("Senha").click() 
    page.get_by_label("Senha").fill("**") ##aqui senha
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("https://wrs.solutions.iqvia.com/run.php?file=MAIN&class=WRS_MAIN&ncon")
    page.locator("md-card:has-text(\"FMB Base de Dados contendo demanda Brasil Abrir Novo Mensal: 2022/08/01 - Semana\")").get_by_role("link", name="Abrir").click()
    page.wait_for_url("https://wrs.solutions.iqvia.com/run.php?file=PANEL&class=WRS_PANEL&cube_s=1&exec_reports=1")


    ###########                   Download dos Relatórios                 ############

    #--------------- Selecionando a Box número 1  (Apresentação MFT)
    page.locator(".wrs_open_modal").click() # Clica no botão que abre o gerenciamento de relatórios
    page.wait_for_url("https://wrs.solutions.iqvia.com/run.php?file=PANEL&class=WRS_PANEL&cube_s=1&exec_reports=1#")
    page.get_by_role("row", name="Apresentação MFT - Share por categoria YTD Sim 2020/08/20 19:50:29 Não VINICIUS MARQUES [MERCADOS].[MERCADO],[PRODUTOS].[FAMÍLIA],[PRODUTOS].[APRESENTAÇÃO],[PRODUTOS].[FCC],[TIPOS ASSOCIADOS DO PDV].[TIPO ASSOCIADO DO PDV],[ESTADOS].[UF] [MEASURES].[UNIDADE YTD ANTERIOR],[MEASURES].[UNIDADE YTD],[MEASURES].[REAL PPP YTD ANTERIOR],[MEASURES].[REAL PPP YTD],[MEASURES].[REAL CH YTD ANTERIOR],[MEASURES].[REAL CH YTD] [MERCADOS].[MERCADO],[CANAIS].[GRUPO CANAL] [CANAIS].[GRUPO CANAL],[MERCADOS].[MERCADO]").locator("input[type=\"checkbox\"]").check()
    page.get_by_role("button", name=" Abrir Relatório").click()
    page.get_by_role("button", name=" Exportar").click()

    # TRY CSV
    with page.expect_download() as download_info:
        page.get_by_role("link", name=" Texto (CSV)").click()
    download = download_info.value
    download.save_as('C:/Teste/download-teste-box1-vendas.csv') #-----> CAMINHO PARA SALVAR O ARQUIVO
    print('Dowload Box número 1 - (Apresentação MFT) - realizado com sucesso ')
    page.wait_for_timeout(9000)

    #------------------ Selecionando a Box número 2 (Apresentação MFT)

    page.locator(".wrs_open_modal").click() # Clica no botão que abre o gerenciamento de relatórios
    page.wait_for_url("https://wrs.solutions.iqvia.com/run.php?file=PANEL&class=WRS_PANEL&cube_s=1&exec_reports=1#")
    page.get_by_role("row", name="Apresentação MFT - Share por categoria YTD Sim 2020/08/20 19:50:29 Não VINICIUS MARQUES [MERCADOS].[MERCADO],[PRODUTOS].[FAMÍLIA],[PRODUTOS].[APRESENTAÇÃO],[PRODUTOS].[FCC],[TIPOS ASSOCIADOS DO PDV].[TIPO ASSOCIADO DO PDV],[ESTADOS].[UF] [MEASURES].[UNIDADE YTD ANTERIOR],[MEASURES].[UNIDADE YTD],[MEASURES].[REAL PPP YTD ANTERIOR],[MEASURES].[REAL PPP YTD],[MEASURES].[REAL CH YTD ANTERIOR],[MEASURES].[REAL CH YTD] [MERCADOS].[MERCADO],[CANAIS].[GRUPO CANAL] [CANAIS].[GRUPO CANAL],[MERCADOS].[MERCADO]").locator("input[type=\"checkbox\"]").check()
    page.get_by_role("button", name=" Abrir Relatório").click()
    page.get_by_role("button", name=" Exportar").click()

    # TRY CSV

    with page.expect_download() as download_info:
        page.get_by_role("link", name=" Texto (CSV)").click()
    download = download_info.value
    download.save_as('C:/Teste/download-teste-box2-vendas.csv')
    print('Dowload Box número 2 - (Apresentação MFT) - realizado com sucesso ')
    page.wait_for_timeout(12000)


    #----------------- Selecionando as Boxs de 3 a 8 (Cadastros)
    page.locator(".wrs_open_modal").click() # Clica no botão que abre o gerenciamento de relatórios
    page.wait_for_url("https://wrs.solutions.iqvia.com/run.php?file=PANEL&class=WRS_PANEL&cube_s=1&exec_reports=1#")
    page.get_by_role("row", name="Cadastro1 Sim 2022/05/03 21:30:43 Não VINICIUS MARQUES [PRODUTOS].[FCC],[PRODUTOS].[APRESENTAÇÃO],[PRODUTOS].[AREA FINAL],[PRODUTOS].[BABY KIDS],[PRODUTOS].[BIOLÓGICO],[PRODUTOS].[BU CIMED],[PRODUTOS].[CADEIA FRIA],[PRODUTOS].[CATEGORIA],[PRODUTOS].[CLASSE NEC NÍVEL 1],[PRODUTOS].[CLASSE NEC NÍVEL 2],[PRODUTOS].[CLASSE NEC NÍVEL 3],[PRODUTOS].[CLASSE NEC NÍVEL 4],[PRODUTOS].[CLASSE NÍVEL 1],[PRODUTOS].[CLASSE NÍVEL 2],[PRODUTOS].[CLASSE NÍVEL 3] [MEASURES].[UNIDADE] null").locator("input[type=\"checkbox\"]").check()
    page.get_by_role("row", name="Cadastro2 Sim 2022/05/03 21:34:16 Não VINICIUS MARQUES [PRODUTOS].[FCC],[PRODUTOS].[CLASSE NÍVEL 4],[PRODUTOS].[CLASSE SEGMENTO MERCADO NÍVEL 1],[PRODUTOS].[CLASSE SEGMENTO MERCADO NÍVEL 2],[PRODUTOS].[CLASSE SEGMENTO MERCADO NÍVEL 3],[PRODUTOS].[CONCENTRAÇÃO],[PRODUTOS].[CONTROLADO],[PRODUTOS].[CORPORAÇÃO],[PRODUTOS].[DERMOCOSMETIC],[PRODUTOS].[DOENÇA CRÔNICA TRANSMISSÍVEL],[PRODUTOS].[EAN],[PRODUTOS].[ÉTICOS],[PRODUTOS].[FABRICANTE],[PRODUTOS].[FAMÍLIA],[PRODUTOS].[FITOTERÁPICO] [MEASURES].[UNIDADE] null").locator("input[type=\"checkbox\"]").check()
    page.get_by_role("row", name="Cadastro3 Sim 2022/05/03 21:45:41 Não VINICIUS MARQUES [PRODUTOS].[FCC],[PRODUTOS].[FORMA NÍVEL 1],[PRODUTOS].[FORMA NÍVEL 2],[PRODUTOS].[FORMA NÍVEL 3],[PRODUTOS].[FORMA],[PRODUTOS].[GENÉRICOS],[PRODUTOS].[KIT],[PRODUTOS].[LABORATÓRIO],[PRODUTOS].[LANÇAMENTO APRESENTAÇÃO],[PRODUTOS].[LANÇAMENTO MARCA],[PRODUTOS].[MARCA],[PRODUTOS].[MEDICAMENTO],[PRODUTOS].[MOLÉCULA LOCAL],[PRODUTOS].[MOLÉCULA],[PRODUTOS].[NUTRACEUTICAL] [MEASURES].[UNIDADE] null").locator("input[type=\"checkbox\"]").check()
    page.get_by_role("row", name="Cadastro4 Sim 2022/05/03 21:57:33 Não VINICIUS MARQUES [PRODUTOS].[FCC],[PRODUTOS].[NUTRICOSMETIC],[PRODUTOS].[OBSERV],[PRODUTOS].[ORÍGEM],[PRODUTOS].[PATENTEADO],[PRODUTOS].[PRESCRITO],[PRODUTOS].[PRODCODE],[PRODUTOS].[PROGRAMA FARMÁCIA POPULAR],[PRODUTOS].[SEGMENTO CH],[PRODUTOS].[SEGMENTO],[PRODUTOS].[SENIOR],[PRODUTOS].[SUB AREA],[PRODUTOS].[SUB CATEGORIA],[PRODUTOS].[SUB SEGMENTO],[PRODUTOS].[TIPO DOENÇA] [MEASURES].[UNIDADE] null").locator("input[type=\"checkbox\"]").check()
    page.get_by_role("row", name="Cadastro5 Sim 2022/05/03 22:00:55 Não VINICIUS MARQUES [PRODUTOS].[FCC],[PRODUTOS].[TIPO MOLÉCULA LOCAL],[PRODUTOS].[TIPO MOLÉCULA],[PRODUTOS].[TIPO PRODUTO] [MEASURES].[UNIDADE] null").locator("input[type=\"checkbox\"]").check()
    page.get_by_role("button", name=" Abrir Relatório").click()
    page.wait_for_timeout(30000)
    page.get_by_role("button", name=" Exportar").click()
    with page.expect_download() as download_info:
        page.get_by_role("link", name=" Texto (CSV)").click()
    download = download_info.value
    download.save_as('download-teste-cadastros.csv')
    print('Dowload Box número 3 a 8 - (Cadastros) - realizado com sucesso ')
    page.wait_for_timeout(5000)


    # --------------------- Fechamento do navegador
    context.close()
    browser.close()

with sync_playwright() as playwright:
    download_relatorio(playwright)
