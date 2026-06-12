from PIL import Image
import os

img_path = 'assets/logo.png'
if os.path.exists(img_path):
    img = Image.open(img_path)
    # Let's save slices
    left_slice = img.crop((138, 162, 650, 624))
    left_slice.save('scratch/left.png')
    
    mid_slice = img.crop((650, 162, 1350, 624))
    mid_slice.save('scratch/middle.png')
    
    right_slice = img.crop((1350, 162, 2057, 624))
    right_slice.save('scratch/right.png')
    
    print("Slices saved successfully!")
else:
    print("File not found")
