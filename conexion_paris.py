import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialiser le driver
driver = webdriver.Chrome()

try:
    # Ouvrir le site
    driver.get("https://www.chopbet.ci/")
    driver.set_window_size(994, 942)

    # Fermer la fenêtre modale
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".close_modal > svg"))
    ).click()

    # Accéder à "Jackpots"
    element = driver.find_element(By.LINK_TEXT, "Jackpots")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    # Déplacer le curseur pour revenir à la position de départ
    actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "body")).perform()

    # Cliquer sur "Connexion"
    driver.find_element(By.LINK_TEXT, "Connexion").click()

    # Remplir le numéro de téléphone
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control:nth-child(3)"))
    )
    phone_input.click()
    phone_input.send_keys("0711653032")

    # Remplir le mot de passe
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputPass"))
    )
    password_input.click()
    password_input.send_keys("azertyuiop")

    # Soumettre le formulaire
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    # Attendre que l'élément de pari soit disponible et cliquer dessus
    outcome_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#odd\\.match-54013019\\.market-1\\.specifier-\\.outcome-3 span > span:nth-child(1)"))
    )
    outcome_element.click()

    # Accéder à un menu
    driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) .item-name").click()

    # Ajouter un montant automatique
    driver.find_element(By.CSS_SELECTOR, ".auto_add > button:nth-child(1)").click()

    # Valider le pari
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()

    # Naviguer vers le logo pour revenir à l'accueil
    logo_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".logo:nth-child(1) g:nth-child(4) path:nth-child(3)"))
    )
    actions.move_to_element(logo_element).perform()

    # Délai de 15 secondes pour observer les résultats
    time.sleep(15)

finally:
    # Fermer le driver
    driver.quit()
