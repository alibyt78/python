from PIL import Image
import os

def resize_images(source_folder, target_folder, size):
    os.makedirs(target_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            img = Image.open(os.path.join(source_folder, filename))
            img_resized = img.resize(size)
            img_resized.save(os.path.join(target_folder, filename))

if __name__ == "__main__":
    resize_images('images/', 'resized/', (800, 600))
    print("Images resized successfully.")
