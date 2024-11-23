from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
import requests
import time
import os
import io

File_directory = os.path.dirname(os.path.abspath(__file__))

Web_Driver_PATH = os.path.join(File_directory, "chromedriver.exe")

service = Service(executable_path = Web_Driver_PATH)

Chrome_Options = Options()
Chrome_Options.add_argument("--headless")
Chrome_Options.add_argument("--disable-logging")
Chrome_Options.add_argument("--output=/dev/null")
Chrome_Options.add_argument("--log-level=3")

Web_Driver_Chrome = webdriver.Chrome(service = service , options = Chrome_Options)

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Charset': 'utf-8, iso-8859-1;q=0.9, *;q=0.8',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive'
}

google_images = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

images_folder = os.path.join(File_directory, "Google Images")

if not os.path.exists(images_folder):
        os.mkdir(images_folder)

def download_image(download_path, url, file_name):

    try:
        # Try to get the image
        response = requests.get(url, headers=headers , timeout= 5)
        
        if response.status_code != 200:
            print(f"Failed to download image {file_name}, status code: {response.status_code}")
            return
        
        print(f"Downloaded {file_name}, Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error while downloading {file_name}: {e}")
        return

    try:
        # Convert the image data into an image object
        image_file = io.BytesIO(response.content)  # Convert image to bytes
        image = Image.open(image_file).convert('RGB')  # Convert bytes back to an image

        if not file_name.endswith('png'):
            file_name += '.png'

        image_path = os.path.join(download_path, file_name)
        with open(image_path, "wb") as f:
            image.save(f, "PNG")

        print(f"Saved image {file_name}")

    except Exception as e:
        print(f"Error while processing image {file_name}: {e}")

def scroll_down(time_to_run):

    reached_end = False

    start_time = time.time()

    while not reached_end:

        current_time = time.time() - start_time

        if current_time >= time_to_run:
            break

        last_height = Web_Driver_Chrome.execute_script("return window.scrollY;")

        Web_Driver_Chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1)

        current_height = Web_Driver_Chrome.execute_script("return window.scrollY")

        if current_height == last_height:
            reached_end = True

    time.sleep(2)

    Web_Driver_Chrome.execute_script("window.scrollTo(0, 0);")

def find_images_on_page(search_name, time_to_run):
    url = google_images + "q=" + search_name
    Web_Driver_Chrome.maximize_window()
    Web_Driver_Chrome.get(url)

    time.sleep(2)

    scroll_down(time_to_run)
    
    images = Web_Driver_Chrome.find_elements(By.CSS_SELECTOR, "div[data-q='{}'] div[style='position:relative'] img".format(search_name))

    return images

def find_google_images_url(max_images, images_found, from_n, every_n):

    images_url = set()

    url_count = 0

    images = images_found

    for image in range(from_n, len(images) + 1):
        if image % every_n == 0:
            images[image].click()
            time.sleep(2)

            large_images_div = Web_Driver_Chrome.find_elements(By.CSS_SELECTOR, "div[data-lnsmd] a[target='_blank'] img")

            for large_image in large_images_div:
                large_image_url = large_image.get_attribute('src')

                if "encrypted-tbn0." in large_image_url or large_image_url.startswith("data:image"):
                    continue

                full_url = large_image_url

                print(full_url)

                images_url.add(full_url)

                url_count += 1

                if url_count >= max_images:
                    break
                
            if url_count >= max_images:
                    break

    return images_url

def folder_for_images(download_folder, filename):
    category_folder = os.path.join(download_folder, filename)

    if not os.path.exists(category_folder):
        os.mkdir(category_folder)
        return category_folder

    folder_lengh = os.listdir(category_folder)

    if len(folder_lengh) == 0:
        return category_folder

    return "Exsits"

def main():

    data = input("Please Enter image(s) you want to search: ")

    try:
        time_to_find_images = int(input(f"Please enter time to find {data} images(Minimum 5S): "))
    except:
        return print("Please input integer!")

    images_found = find_images_on_page(data, time_to_find_images)

    print("\n ^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^- \n")

    print(f"Founded {len(images_found)} images of {data} ^-^-^-^-^-^-^-^-^-^-^-^-")

    if len(images_found) == 0:
        return print("No images found.")

    try:
        image_number = int(input(f"Please Enter number of {data} image(s) you want to search: "))

        if image_number <= 0:
            return print("Please enter integer above 0")

        from_number = int(input("Please Enter from where to start: "))

        step = int(input(f"Please Enter every N-th image to download: "))

        if step <= 0:
            return print("Please enter integer above 0")

    except:
        return print("Please input integer!")

    print("\n ^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^- \n")

    images_Subfolder = folder_for_images(images_folder, data)
    
    if images_Subfolder == "Exsits":
        return print(f"Please enter Different name of Subfolder or delete previous Subfolder of {data}!") 

    img_urls = find_google_images_url(image_number, images_found, from_number, step)

    for index , img_url in zip(range(image_number + 1), img_urls):
        download_image(images_Subfolder, img_url, data + "_" + str(index + 1))

if __name__ == "__main__":
    main()
