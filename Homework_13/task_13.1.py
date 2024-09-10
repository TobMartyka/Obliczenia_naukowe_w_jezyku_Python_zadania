from PIL import Image

image_path = "image.jpeg"
image = Image.open(image_path)

print(f"Mode: {image.mode}")
print(f"Size: {image.size}")
print(f"Format: {image.format}")

thumbnail_size = (128, 128)
image.thumbnail(thumbnail_size)

image.save('thumbnail_image.png')
