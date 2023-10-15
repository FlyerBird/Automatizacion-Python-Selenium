from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa el navegador web 
driver = webdriver.Chrome()

# Abre Google y realiza la búsqueda
driver.get("https://www.google.com/?hl=es")
time.sleep(5)

# Encuentra el botón del pop-up por su selector 
popup_button = driver.find_element(By.XPATH, "//*[@id='W0wltc']")

# Haz clic en el botón del pop-up para cerrarlo
popup_button.click()
time.sleep(2)

# Busca en el navegador de Google "automatización"
google_search_box = driver.find_element(By.NAME,"q")
google_search_box.send_keys("automatización")
time.sleep(2)

google_search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Encuentra y abre el enlace de Wikipedia
wikipedia_link = driver.find_element(By.CSS_SELECTOR, "a[href*='wikipedia.org']")
wikipedia_link.click()
time.sleep(3)

# Realiza captura de pantalla y guarda en un archivo
driver.save_screenshot("screenshot.png")

time.sleep(3)

# Cierra el navegador
driver.quit()

