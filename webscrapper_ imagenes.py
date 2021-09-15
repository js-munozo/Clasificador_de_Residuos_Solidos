# query: Buscar las imagenes en google , por ejemplo 'gato'
# max_links_to_fetch: Numero de links que se van a obtener desde google
# driver: instancia del Webdriver

import os
import io
import hashlib
from PIL import Image
import time

import requests
from selenium import webdriver


# obtener las urls
def fetch_img_url(query: str, max_links_fetch: int, driver: webdriver, sleep_between_iteractions: int = 1):

    def go_to_end(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_iteractions)

    # construir el query de google
    search_url = "https://www.google.com.co/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # cargar la página
    driver.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_fetch:

        go_to_end(driver)

        # aplicar selector css para encontrar elementos
        thumbnail_results = driver.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(
            f'Encontrados: {number_results} resultados buscados. Extracción de links desde: {results_start}:{number_results}')

        # obtener las imagenes
        for img in thumbnail_results[results_start:number_results]:

            # intentar dar click a cada imagen
            try:
                img.click()
                time.sleep(sleep_between_iteractions)
            except Exception:
                continue

            # extraer las url de las imagenes
            actual_imgs = driver.find_elements_by_css_selector('img.Q4LuWd')
            for actual_image in actual_imgs:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            # si se cumple la cantidad de imagenes, terminamos
            if len(image_urls) >= max_links_fetch:
                print(f'Encontrados {len(image_urls)} links de imágenes ')
                break

            # sino continuamos buscando imagenes
            else:
                print(f'Encontrados {len(image_urls)} links de imágenes. Continuando la búsqueda ...')
                time.sleep(30)
                return

                load_more_button = driver.find_elements_by_css_selector('img.tx8vtf')
                if load_more_button:
                    driver.execute_script("document.querySelector('.mye4qd').click();")

            # actualizando results_start
            results_start = len(thumbnail_results)

    return image_urls

# Guardar la imágen en la carpeta creada
def save_img(folder_path: str, url: str):

    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f'Error -- No se puede desacrgar {url} - {e}')

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')

        with open(file_path, 'wb') as f:
            image.save(f, 'JPEG', quality=85)
            print(f'Guardado exitosamente - {url} - as {file_path}')

    except Exception as e:
        print(f'Error no se puede descargar {url} - {e}')


# funcion para ejecutar el script
def search_and_download(search_word:str, driver_path=str, target_path='./images', number_images=5):
    target_folder = os.path.join(target_path, '_'.join(search_word.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Firefox() as wd:
        res = fetch_img_url(search_word, number_images, driver=wd)

    for elem in res:
        save_img(target_folder, elem)


list_to_search = ['plastico', 'metal', 'carton', 'vidrio', 'papel', 'residuos ordinarios']

for i in range(len(list_to_search)):
    search_word = list_to_search[i]
    search_and_download(search_word=search_word, driver_path='D:/Data/Desarrollo/Proyectos/waste_classification')