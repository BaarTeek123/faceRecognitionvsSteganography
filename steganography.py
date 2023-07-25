'''
from PIL import Image
import numpy as np

def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

def hide_data(image, secret_image):
    # make sure images have the same size
    assert image.shape == secret_image.shape
    hidden_image = np.copy(image)
    # flatten both images
    image_flat = image.flatten()

    for i in range(len(image_flat)):
        # modify least significant bits
        hidden_flat = list(to_bin(hidden_image[i]))
        secret_flat = list(to_bin(secret_image[i]))
        hidden_flat[-1] = secret_flat[-1]
        hidden_flat[-2] = secret_flat[-2]
        hidden_image[i] = int(''.join(hidden_flat), 2)
    return hidden_image

def encode_images(image, secret_image, dest_image_path = None):
    # read images
    if isinstance(image, str):
        image = np.array(Image.open(image))
    if isinstance(secret_image, str):
        secret_image = np.array(Image.open(secret_image))
    # hide the secret_image inside image
    hidden_image = hide_data(image, secret_image)
    # save the resulting image
"""

'''


from PIL import Image
import numpy as np


def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data])
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        return data.tobytes()
    raise TypeError("Type not supported.")


def hide_data(image, secret_image):
    # make sure images have the same size
    assert image.shape == secret_image.shape
    hidden_image = np.copy(image)
    # flatten both images
    image_flat = image.flatten()
    secret_flat = secret_image.flatten()
    for i in range(len(image_flat)):
        # modify least significant bits
        hidden_flat = list(to_bin(hidden_image[i]))
        secret_bits = list(to_bin(secret_flat[i]))
        hidden_flat[-1] = secret_bits[-1]
        hidden_flat[-2] = secret_bits[-2]
        hidden_image[i] = int(''.join(hidden_flat), 2)
    return hidden_image


def encode_images(src_image, src_secret_image, dest_image_path):
    # read images if they're provided as file paths
    if isinstance(src_image, str):
        src_image = np.array(Image.open(src_image))
    if isinstance(src_secret_image, str):
        src_secret_image = np.array(Image.open(src_secret_image))

    # hide the secret_image inside image
    hidden_image = hide_data(src_image, src_secret_image)
    # save the resulting image
    if dest_image_path is None:
        Image.fromarray(hidden_image).save(dest_image_path)
    return hidden_image
    # Image.fromarray(hidden_image).save(dest_image_path)

# use the function like this with file paths:
# encode_images("image.jpg", "secret_image.jpg", "hidden_image.jpg")

# or with numpy arrays:
# img1 = np.array(Image.open("image.jpg"))
# img2 = np.array(Image.open("secret_image.jpg"))
# encode_images(img1, img2, "hidden_image.jpg")

