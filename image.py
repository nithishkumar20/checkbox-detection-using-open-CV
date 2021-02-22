import cv2
import matplotlib.pyplot as plt

# reading image
image = cv2.imread('form.jpg')

# displaying image
plt.imshow("Image",image)
cv2.waitKey(0)
plt.show()
