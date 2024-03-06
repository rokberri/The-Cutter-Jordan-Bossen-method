# 2 variant
from PIL import Image
from math import ceil, fmod 
from time import time 



ALPHA = 0.5
ORIGIN = 'fire_apple.jpg'
NEW_IMG = 'encoded_image.png'
MESSAGE = """Canada is the second largest country in the world. Its territory stretches practically from the North Pole to the subtropical regions, from the Pacific Ocean to the Atlantic Ocean. Along with the capital - Ottawa, the largest metropolitan areas are Montreal, Calgary, Winnipeg and Toronto. A large number of islands make up the Canadian territory, including Baffin's Land, Victoria, Newfoundland and others. Canada is a constitutional monarchy with strong democratic traditions. The Queen of Great Britain is recognized as the head of state, she is represented by the Governor-General. The state flag features a red maple leaf on a white background with red stripes on the sides. The combination of the two colors proclaims the unity of the British and French nations. The population of this large country is 36 million people. In the country, two languages have an official status — English and French. English is the dominant language in all provinces with the exception of Quebec."""
BIN_MESSAGE = ''.join(format(ord(sim), '08b') for sim in MESSAGE) + '1111111111111110'


def encode(img_path:str,SIGMA = 2):
    img = Image.open(img_path)
    width, height = img.size
    tmp = img.copy()

    index = 0

    for y in range(SIGMA,height,SIGMA):
        for x in range(SIGMA, width,SIGMA):
            # print(x,y)
            if index >= len(BIN_MESSAGE):
                    break
            pixel = list(tmp.getpixel((x, y)))
            if index < len(BIN_MESSAGE):
                L = 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]
                if BIN_MESSAGE[index] == '0':
                    pixel[2] = round(pixel[2] + ALPHA*L)
                else:
                    pixel[2] = round(pixel[2] - ALPHA*L)
                index += 1
            else: 
                break
            tmp.putpixel((x,y),tuple(pixel))
    tmp.save('encoded_image.png')
    print("FINISH")

def mean_blue(img:Image, curr_pxl:tuple,sigma=1):
    x,y = curr_pxl
    pxl_sum = 0
    for i in range(1, sigma+1):
        if x - i>=0:
            pxl_sum += img.getpixel((x - i,y))[2]
        if x + i<img.size[0]:
            pxl_sum += img.getpixel((x + i,y))[2]
        if y - i>=0:
            pxl_sum += img.getpixel((x,y - i))[2]
        if y + i<img.size[1]:
            pxl_sum += img.getpixel((x,y + i))[2]
    return ((1/(4*sigma))*pxl_sum)

def decode(img_path:str,SIGMA = 2):
    img = Image.open(img_path)
    message = ''
    width, height = img.size
    binary_message = ''
    

    for y in range(SIGMA,height,SIGMA):
        for x in range(SIGMA,width,SIGMA):
            pixel = img.getpixel((x,y))
            if pixel[2] <= int(mean_blue(img,(x,y),SIGMA)):
                binary_message += '1'
            else:
                binary_message += '0'

    # print(binary_message)
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == '11111111':
            break
        message += chr(int(byte, 2))
    return(message)

def main():
    encode(ORIGIN)
    print(decode(NEW_IMG))

if __name__=='__main__':
     main()









