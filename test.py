# def encode(img_path:str):
#     img = Image.open(img_path)
#     width, height = img.size
#     tmp = img.copy()

#     index = 0
#     # pixels_height = lin_rand_arr_flxd(SEED, height, height-1)
#     # pixels_width = lin_rand_arr_flxd(SEED, width,width-1)

#     for y in range(height):
#         for x in range(width):
#             if index >= len(BIN_MESSAGE):
#                     break
#             pixel = list(tmp.getpixel((x, y)))
#             if index < len(BIN_MESSAGE):
#                 L = 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]
#                 if BIN_MESSAGE[index] == '0':
#                     pixel[2] = round(pixel[2] + ALPHA*L)
#                 else:
#                     pixel[2] = round(pixel[2] - ALPHA*L)
#                 index += 1
#             else: 
#                 break
#             tmp.putpixel((x,y),tuple(pixel))
#             print('PIXEL',pixel)
#     tmp.save('encoded_image.png')
#     print("FINISH")


for i in range(2,10,4):
    print(i)