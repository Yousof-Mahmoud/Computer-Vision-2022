import numpy as np
import cv2

def normalize_images(images):
    # initial zero ndarray
    normalized_images = np.zeros_like(images.astype(float))

    # The first images index is number of images where the other indices indicates
    # hieight, width and depth of the image
    num_images = images.shape[0]

    # Computing the minimum and maximum value of the input image to do the normalization based on them
    maximum_value, minimum_value = images.max(), images.min()

    # Normalize all the pixel values of the images to be from 0 to 1
    for img in range(num_images):
        normalized_images[img, ...] = (images[img, ...] - float(minimum_value)) / float(maximum_value - minimum_value)
    print('image:', images)
    print('normalized image: ', normalized_images)

    return normalized_images

# Load an color image in grayscale
img = cv2.imread('images/Mona-Lisa.jpg', 0)

normalized_img = normalize_images(img)

# Display the original Image
cv2.imshow('Original image', img)

# Display the Normalized image
cv2.imshow('Normalized image', normalized_img)
#key binding function
cv2.waitKey(0)
#Destroyed all window we created earlier.
cv2.destroyAllWindows()