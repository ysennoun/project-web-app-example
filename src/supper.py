import os
from super_image import EdsrModel, ImageLoader
from PIL import Image

output_image_path = f"{os.path.dirname(__file__)}/images/resized_image.jpg"
image = Image.open(output_image_path)

model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=2)
inputs = ImageLoader.load_image(image)
preds = model(inputs)

ImageLoader.save_image(preds, './scaled_2x.png')
ImageLoader.save_compare(inputs, preds, './scaled_2x_compare.png')
