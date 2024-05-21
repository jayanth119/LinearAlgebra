import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt 
def rotate_image(image_path, degrees):
    # Load the image and convert it to a NumPy array
    image = Image.open(image_path)
    image_array = np.array(image)
    print(image_array)
    print(np.shape(image_array))
    # Convert the degrees to radians
    radians = np.deg2rad(degrees)

    # Create the rotation matrix
    rotation_matrix = np.array([
        [np.cos(radians), -np.sin(radians)],
        [np.sin(radians), np.cos(radians)]
    ])

    # Compute the size of the new image
    height, width = image_array.shape[:2]
    print('height=',height,'width=', width)
    new_width = int(width * np.abs(np.cos(radians)) + height * np.abs(np.sin(radians)))
    new_height = int(width * np.abs(np.sin(radians)) + height * np.abs(np.cos(radians)))
    print('height=',new_height,'width=', new_width)    

    # Compute the center of the image
    center = np.array([width / 2, height / 2])

    # Compute the new center of the image after rotation
    new_center = np.array([new_width / 2, new_height / 2])

    # Compute the translation matrix to move the center of the image to the origin
    translation_matrix = np.array([
        [1, 0, -center[0]],
        [0, 1, -center[1]],
        [0, 0, 1]
    ])

    # Compute the rotation and translation matrix
    rotation_translation_matrix = np.array([
        [rotation_matrix[0, 0], rotation_matrix[0, 1], 0],
        [rotation_matrix[1, 0], rotation_matrix[1, 1], 0],
        [0, 0, 1]
    ]).dot(translation_matrix)

    # Compute the translation matrix to move the center of the image to the new center after rotation
    new_translation_matrix = np.array([
        [1, 0, new_center[0]],
        [0, 1, new_center[1]],
        [0, 0, 1]
    ])

    # Compute the final transformation matrix
    final_transformation_matrix = new_translation_matrix.dot(rotation_translation_matrix)

    # Apply the transformation to the image
    rotated_image_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    for i in range(new_height):
        for j in range(new_width):
            x, y, z = final_transformation_matrix.dot(np.array([j, i, 1])).astype(int)
            if x >= 0 and x < width and y >= 0 and y < height:
                rotated_image_array[i, j] = image_array[y, x]

    # Convert the NumPy array back to an image
    rotated_image = Image.fromarray(rotated_image_array)

    return rotated_image
##np.set_printoptions(precision=4 , suppress=True)
##rotated_image = rotate_image('1.jpg',90)
##rotated_image.show()
image_path = r'1.jpg'
image_array = cv2.imread(image_path)
print("ok dane")
scaled_image  = cv2.cvtColor(image_array,cv2.COLOR_BGR2GRAY)
print(np.shape(scaled_image))
u,s,v = np.linalg.svd(scaled_image)
print(np.shape(u),np.shape(s),np.shape(v))
x = np.zeros(np.shape(scaled_image))
n = len(s)-3050
x[[i for i in range(n)],[i for i in range(n)]] = s[:n]
plt.imshow(np.dot(np.dot(u,x),v))
plt.show()
completed = 'hello world'
print(completed)
