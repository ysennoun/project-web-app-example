import os
import cv2
from PIL import Image


def resize_image_opencv(input_image_path, output_image_path, new_size):
    # Load the image using OpenCV
    image = cv2.imread(input_image_path)

    # Resize the image using cv2.resize()
    resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)


def resize_image(input_image_path, output_image_path, new_size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    new_width, new_height = new_size

    # Calculate the aspect ratio of the original image
    aspect_ratio = width / height

    # Calculate the aspect ratio of the desired size
    new_aspect_ratio = new_width / new_height

    # Determine the actual size for resizing without changing the aspect ratio
    if new_aspect_ratio > aspect_ratio:
        # The desired size is wider
        resized_width = new_width
        resized_height = int(new_width / aspect_ratio)
    else:
        # The desired size is taller or has the same aspect ratio
        resized_height = new_height
        resized_width = int(new_height * aspect_ratio)

    # Resize the image
    resized_image = original_image.resize((resized_width, resized_height), Image.LANCZOS)

    # Create a new blank white background image
    new_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))

    # Calculate the position to paste the resized image on the new background
    left = (new_width - resized_width) // 2
    top = (new_height - resized_height) // 2
    right = left + resized_width
    bottom = top + resized_height

    # Paste the resized image onto the new background
    new_image.paste(resized_image, (left, top, right, bottom))

    # Save the resized image
    new_image.save(output_image_path)


def enlarge_image(input_image_path, output_image_path, scale_percent):
    # Load the image using OpenCV
    image = cv2.imread(input_image_path)

    # Calculate the new dimensions
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    new_size = (width, height)

    # Resize the image using cv2.resize()
    enlarged_image = cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)

    # Save the enlarged image
    cv2.imwrite(output_image_path, enlarged_image)


def get_image_dimensions(image_path):
    image = Image.open(image_path)
    width, height = image.size
    return width, height


# Example usage
if __name__ == "__main__":
    input_image_path = f"{os.path.dirname(__file__)}/images/input_image.jpg"
    output_image_path = f"{os.path.dirname(__file__)}/images/resized_image.jpg"
    new_size = (1920, 1280)
    resize_image(input_image_path, output_image_path, new_size)

    # OpenCV
    input_image_path = f"{os.path.dirname(__file__)}/images/input_image.jpg"
    output_image_path = f"{os.path.dirname(__file__)}/images/resized_image_opencv.jpg"
    new_size = (1920, 1280)
    resize_image_opencv(input_image_path, output_image_path, new_size)

    input_image_path = f"{os.path.dirname(__file__)}/images/input_image.jpg"
    output_image_path = f"{os.path.dirname(__file__)}/images/resized_image_enlarged.jpg"
    scale_percent = 250  # Increase size by 200%
    enlarge_image(input_image_path, output_image_path, scale_percent)

    image_path = f"{os.path.dirname(__file__)}/images/intro-bg.jpg"
    width, height = get_image_dimensions(image_path)
    print(f"The image dimensions are: {width} x {height}")
