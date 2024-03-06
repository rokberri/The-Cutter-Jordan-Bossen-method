from PIL import Image
import metriks



ORIGIN_IMG = Image.open('fire_apple.jpg')
NEW_IMG = Image.open('encoded_image.png')

print(metriks.max_absolute_deviation(ORIGIN_IMG,NEW_IMG))
print(metriks.normalized_root_mean_square_deviation(ORIGIN_IMG,NEW_IMG))
print(metriks.uiqi(ORIGIN_IMG,NEW_IMG))