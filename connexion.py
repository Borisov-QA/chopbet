
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

    # Trouver le bouton de connexion et cliquer
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-outline"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".btn-outline > div").click()

    # Attendre l'apparition du champ de numéro de téléphone
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control"))
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
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
    )
    submit_button.click()

    # Délai de 15 secondes
    time.sleep(15)

finally:
    # Fermer le driver
    driver.quit()
