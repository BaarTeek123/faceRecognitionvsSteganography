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
    secret_flat = secret_image.flatten()
    for i in range(len(image_flat)):
        # modify least significant bits
        hidden_flat = list(to_bin(hidden_image[i]))
        secret_flat = list(to_bin(secret_image[i]))
        hidden_flat[-1] = secret_flat[-1]
        hidden_flat[-2] = secret_flat[-2]
        hidden_image[i] = int(''.join(hidden_flat), 2)
    return hidden_image

def encode_images(src_image_path, src_secret_image_path, dest_image_path):
    # read images
    image = np.array(Image.open(src_image_path))
    secret_image = np.array(Image.open(src_secret_image_path))
    # hide the secret_image inside image
    hidden_image = hide_data(image, secret_image)
    # save the resulting image
    Image.fromarray(hidden_image).save(dest_image_path)

if __name__ == '__main__':
    IMG_PATH = ''
    SECRET_IMG_PATH = ''
    HIDDEN_IMG = ''
    encode_images(IMG_PATH, SECRET_IMG_PATH, HIDDEN_IMG)
