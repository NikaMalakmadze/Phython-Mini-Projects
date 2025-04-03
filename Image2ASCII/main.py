
from PIL import Image

_str = r'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'   # ascii letters that will be used instead of pixels

# simple function to load image
def load_img(path_to_img):
    try:
        img = Image.open(path_to_img)
    except:
        print('Error loading image!')
    return img

# function to get info from image and resize it
def prepare_img(img, new_width, scale):
    width, height = img.size                                # get image size
    aspect_ratio = height/width                             # calculate aspect ratio
    new_height = int(aspect_ratio * new_width * scale)              # assign new height
    resized_img = img.resize((new_width, new_height))               # resize image

    return resized_img

# function to calculate average value of pixel's red green and blue values
def average(pixel_color):
    return int(sum(pixel_color)/3)

# function to normilize average value of pixel(it's brightness)
def normilize_brightness(brightness, gamma):
    index = int((brightness / 255) * gamma * (len(_str)-1))         # calculate index by brightness
    return min(index, len(_str)-1)                                      # for safety(if index is more than last index of _str variable)

# function to convert pixels into ascii letters
def pixel_to_ascii(img, new_width, gamma):
    img_pixels = img.getdata()                                      # get each pixel color
    ascii = ''                                                      # temp variable where asci all 'translated' ascii letters will be saved
    for img_pixel in img_pixels:
        pixel_average = average(img_pixel)                                      # average of pixel's RGB
        ascii += _str[normilize_brightness(pixel_average, gamma)]               # add converted pixel into ascii variable as a char
    
    rows = [ascii[i:i + new_width] for i in range(0, len(ascii), new_width)]    # slice ascii variable chars into many rows with chars

    asci_image = '\n'.join(rows)                                                # join those rows by new line('\n')

    return asci_image                                                  

# main function, join everything together
def main(new_width, scale, gamma):
    image_path = input('Enter path to image: ')                                 # get path to image
    loaded_img = load_img(image_path)                                               # load image
    prepared_img = prepare_img(loaded_img, new_width, scale)                        # get info and resize image

    ascii_img = pixel_to_ascii(prepared_img, new_width, gamma)                              # convert to ascii

    with open('asciioutput.txt', 'w', encoding='utf-8') as f:                               # save ascii art in txt file
        f.write(ascii_img)

if __name__ == '__main__':
    main(100, 0.5, 0.8)