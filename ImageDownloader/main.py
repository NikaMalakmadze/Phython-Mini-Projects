
#importing libraries

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
import requests
import time
import os
import io

#setting things(Web_Driver, Headers, Images_Folder) for the functionality of code's main part:

File_directory = os.path.dirname(os.path.abspath(__file__))               #getting absolute path of current(main.py) file's directory

Web_Driver_PATH = os.path.join(File_directory, "chromedriver.exe")                  #getting absolute path of ChromeDriver

service = Service(executable_path = Web_Driver_PATH)      #service variable to handle ChromeDriver using executable_path             

#setting ChromeDriver options
Chrome_Options = Options()
Chrome_Options.add_argument("--headless")
Chrome_Options.add_argument("--disable-logging")
Chrome_Options.add_argument("--output=/dev/null")
Chrome_Options.add_argument("--log-level=3")

Web_Driver_Chrome = webdriver.Chrome(service = service , options = Chrome_Options)      #setting actual ChromeDriver

#setting headers for requests library to simulate a request from real-browser
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Charset': 'utf-8, iso-8859-1;q=0.9, *;q=0.8',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive'
}

google_images = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'      #url of Google Images

images_folder = os.path.join(File_directory, "Google Images") # <---------- You can type any name here

#create images folder if it doesn't exists
if not os.path.exists(images_folder):
        os.mkdir(images_folder)

#main part of code:

#function that downloads image | it needs where to download image, url of image and name of image |
def download_image(download_path, url, file_name):

    try:
        # Try to get the image
        response = requests.get(url, headers=headers , timeout= 5)
        
        if response.status_code != 200:                                                             #if unable to get image
            print(f"Failed to download image {file_name}, status code: {response.status_code}")
            return
        
        print(f"Downloaded {file_name}, Status code: {response.status_code}")                   #successfully downloaded

    except requests.exceptions.RequestException as e:
        print(f"Error while downloading {file_name}: {e}")                                      #if unable to get image
        return

    try:

        image_file = io.BytesIO(response.content)                               # Convert image to bytes
        image = Image.open(image_file).convert('RGB')                           # Convert bytes back to an image

        if not file_name.endswith('png'):                                       #save all images in png formaat
            file_name += '.png'

        image_path = os.path.join(download_path, file_name)                     #create path of image to save
        with open(image_path, "wb") as f:                                           #save image as PNG file
            image.save(f, "PNG")

        print(f"Saved image {file_name}")

    except Exception as e:
        print(f"Error while processing image {file_name}: {e}")

#function to scroll down and then go back on top |it needs time to run code inside of it |
def scroll_down(time_to_run):

    reached_end = False

    start_time = time.time()                                            #start timer

    while not reached_end:                                      #scroll down until page bottom is reached

        current_time = time.time() - start_time                     #get current time from the start time

        if current_time >= time_to_run:                         #if time elapsed = time to find images break
            break

        last_height = Web_Driver_Chrome.execute_script("return window.scrollY;")      #get height of page before scrolling down

        Web_Driver_Chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")     #scroll down

        time.sleep(1)           #wait 1s

        current_height = Web_Driver_Chrome.execute_script("return window.scrollY")          #get height of page after scrolling down

        if current_height == last_height:                       #check if reached bottom of page
            reached_end = True

    time.sleep(2)               #wait 2s

    Web_Driver_Chrome.execute_script("window.scrollTo(0, 0);")          #go at the top of page

#function that find images on page | it needs search name and time to find images |
def find_images_on_page(search_name, time_to_run):
    url = google_images + "q=" + search_name                        #get url of images you want to download in google images
    Web_Driver_Chrome.maximize_window()                             #maximize window
    Web_Driver_Chrome.get(url)                                          #go on that url

    time.sleep(2)                               #wait 2s until page is loaded

    scroll_down(time_to_run)                            #scroll down function to load more images
    
    #find images on Google Images page
    images = Web_Driver_Chrome.find_elements(By.CSS_SELECTOR, "div[data-q='{}'] div[style='position:relative'] img".format(search_name))                                               

    return images

#function to get urls of images
# 1. clicks on each image and opens larger format of it
# 2. gets url of larger image
# 3. checks image url(skips image if it's encrypted)
# 4. if checking is passed successfully saving image url
# 5. repeating this process
# | it needs number of images to download, images number that are on page, from which image to start getting urls and Which N-th image will be clicked |    
def find_google_images_url(max_images, images_found, from_n, every_n):

    images_url = set()                          #set in where urls will be saved after finding and filtering them

    url_count = 0                                   #count of urls that were added in images_url set

    images = images_found

    for image in range(from_n, len(images) + 1):          #looping through every image in images variable from start position to end
        if image % every_n == 0:                              #check if current image is N-thS
            images[image].click()                               #click on image
            time.sleep(2)

            #find all image with larger format(there are two img tags inside of div that is opened after clicking image thumbnail)
            large_images_div = Web_Driver_Chrome.find_elements(By.CSS_SELECTOR, "div[data-lnsmd] a[target='_blank'] img")

            for large_image in large_images_div:                            #looping through this two img tag
                large_image_url = large_image.get_attribute('src')              #get url of it

                #skip image url if it's encrypted
                if "encrypted-tbn0." in large_image_url or large_image_url.startswith("data:image"):
                    continue

                full_url = large_image_url          #if not it's full_url of image

                print(full_url)

                images_url.add(full_url)            #add image url in set

                url_count += 1                      #add +1 in count

                if url_count >= max_images:         #break if reached limit of images to download
                    break
                
            if url_count >= max_images:             #break if reached limit of images to download
                    break

    return images_url

#function that creates SubFolder for each search name inside of Google Images Folder | it needs where to create SubFolder and what to name it |
def folder_for_images(download_folder, filename):
    category_folder = os.path.join(download_folder, filename)     #create absolute path of SubFolder

    #if SubFolder doens't exsits create it
    if not os.path.exists(category_folder):
        os.mkdir(category_folder)
        return category_folder

    #if it exsits:
    folder_lengh = os.listdir(category_folder)              #list down all images that are in it

    if len(folder_lengh) == 0:                              #if it is empty it's ok to save images in it
        return category_folder

    return "Exsits"                                 #if it's not empty it's not ok to save images in it

#The main function of the code, from which we receive data from the user and connect other functions with each other
def main():

    data = input("Please Enter image(s) you want to search: ")          #input from user what to search

    try:
        time_to_find_images = int(input(f"Please enter time to find {data} images(Minimum 5S): "))      #input from user time to find images on page
    except:
        return print("Please input integer!")

    images_found = find_images_on_page(data, time_to_find_images)               #find images on page

    print("\n ^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^- \n")

    print(f"Founded {len(images_found)} images of {data} ^-^-^-^-^-^-^-^-^-^-^-^-")     #informate user how many images were found

    if len(images_found) == 0:                                                  #if no images were found
        return print("No images found.")

    try:
        image_number = int(input(f"Please Enter number of {data} image(s) you want to search: "))   #input from user image number to download

        if image_number <= 0:
            return print("Please enter integer above 0")

        from_number = int(input("Please Enter from where to start: "))                   #input from user from wich image to start

        step = int(input(f"Please Enter every N-th image to download: "))           #input from user wich N-th image to click

        if step <= 0:
            return print("Please enter integer above 0")

    except:
        return print("Please input integer!")

    print("\n ^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^- \n")

    images_Subfolder = folder_for_images(images_folder, data)               #create SubFolder for search name
    
    if images_Subfolder == "Exsits":
        return print(f"Please enter Different name of Subfolder or delete previous Subfolder of {data}!") 

    img_urls = find_google_images_url(image_number, images_found, from_number, step)        #get urls

    #download images
    for index , img_url in zip(range(image_number + 1), img_urls):
        download_image(images_Subfolder, img_url, data + "_" + str(index + 1))

if __name__ == "__main__":
    main()
