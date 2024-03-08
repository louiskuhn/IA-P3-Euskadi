from pickle import TRUE

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import requests
import shutil
import os
import sys
import argparse
from binascii import a2b_base64
from tqdm import tqdm

def parse_arguments():
    parser = argparse.ArgumentParser(description='Un petit scraper pour Google Image')
    parser.add_argument('type',
                        help='type of object to search for, this will be used as the directory name and as a name stem for image storage')
    parser.add_argument('search',
                        help='Google search for which you want to get the images')
    parser.add_argument('-n', '--number', type=int, default=10,
                        help='Number of images you want to store')
    parser.add_argument('-d', '--directory', default='scraped_images',
                        help='The parent directory in which to store the files, images will be stored in a subdirectory named after the type parameter')
    
    args = parser.parse_args()

    return args.type, args.search, args.number, args.directory


def scrap_imgs(obj_type, search, number=10, directory='scraped_images'):

    print(f"---------------------------------------------\nConnection et recherche google:\n{search}\n...")
    # OLD with Firefox : pbm with Firefox from Snap in ubuntu 22.04
    # opts = webdriver.FirefoxOptions()
    # opts.add_argument("--headless")
    # driver = webdriver.Firefox(options=opts)

    # Chrome solution using new service argument
    opts = Options()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.maximize_window()
    
    script_dir = os.path.dirname(os.path.realpath(__file__))
    store_dir = os.path.join(script_dir, directory, obj_type)

    if not os.path.exists(store_dir) :
        os.makedirs(store_dir, exist_ok=TRUE)
        i_max = 0
    elif len(os.listdir(store_dir)) == 0 :
        i_max = 0
    else :
        i_max = max(map(lambda name : int(name.split('_')[1].split('.')[0]),
                    os.listdir(store_dir)))

    url = f'https://www.google.com/search?q={search}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'

    driver.get(url)

    # on accepte les cookies Google si nécessaire (avec 2 langues possibles EN ou FR)
    if driver.title == "Before you continue":
        driver.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()

    if driver.title == "Avant de continuer":
        driver.find_element(By.XPATH,"//button[@aria-label='Tout accepter']").click()

    # on scroll pour pouvoir scraper plus d'images
    print("Scrolling de la page de résultats de Google Image:")
    for _ in tqdm(range(10)):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
        time.sleep(0.5)
    
    print("Récupération des images:")
    cpt=0
    flag=False
    for i in tqdm(range(1,number)):

        img_src = driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img').get_attribute("src")
        # img_src = driver.find_element(By.XPATH, f'//div//div//div//div//div//div//div//div//div//div[{i+1}]//a[1]//div[1]//img[1]').get_attribute("src")
        filename = f'/{obj_type}_{i_max+i}.jpg'

        if img_src is None:
            cpt+=1
            flag=True

        else:
            if img_src[:10] == 'data:image':
                data = img_src.split(',')[1]
                binary_data = a2b_base64(data)
                with open(store_dir + filename, 'wb') as f:
                    f.write(binary_data)
            
            elif img_src[:4] == 'http':
                response = requests.get(img_src,stream=True)
                with open(store_dir + filename, 'wb') as f:
                    shutil.copyfileobj(response.raw, f)

    print(f"{number-cpt} images sauvegardées dans le dossier {store_dir}")
    
    if flag:
        print(f"*** !! ATTENTION !! ***\n{cpt} image(s) n'a(ont) pas pu être scrappée(s)")

def main():
    args = parse_arguments()
    scrap_imgs(*args)

if __name__ == "__main__":
    main()
