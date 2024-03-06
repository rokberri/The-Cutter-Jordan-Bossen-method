from main import encode, decode
import matplotlib.pyplot as plt
import numpy as np

ALPHA = 0.5
SIGMA = 1
ORIGIN = 'fire_apple.jpg'
NEW_IMG = 'encoded_image.png'
MESSAGE = """Canada is the second largest country in the world. Its territory stretches practically from the North Pole to the subtropical regions, from the Pacific Ocean to the Atlantic Ocean. Along with the capital - Ottawa, the largest metropolitan areas are Montreal, Calgary, Winnipeg and Toronto. A large number of islands make up the Canadian territory, including Baffin's Land, Victoria, Newfoundland and others. Canada is a constitutional monarchy with strong democratic traditions. The Queen of Great Britain is recognized as the head of state, she is represented by the Governor-General. The state flag features a red maple leaf on a white background with red stripes on the sides. The combination of the two colors proclaims the unity of the British and French nations. The population of this large country is 36 million people. In the country, two languages have an official status — English and French. English is the dominant language in all provinces with the exception of Quebec."""



errors = list()
for i in range(1,10):
    encode(ORIGIN,i)
    new_msg = decode(NEW_IMG,i)[0:len(MESSAGE)]   
    am_of_err = 0 
    for sim in range(len(MESSAGE)):
        if MESSAGE[sim] != new_msg[sim]:
            am_of_err += 1
    errors.append(am_of_err)

fig, ax = plt.subplots()

x = [1,2,3,4,5,6,7,8,9]
ax.plot(x,errors)
plt.show()