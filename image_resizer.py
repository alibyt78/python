from PIL import Image

# Resize an image to 200x200 pixels
image = Image.new('RGB', (500, 300), color = 'red')
image = image.resize((200, 200))
image.save('resized_image.jpg')
print('Image resized successfully!')
