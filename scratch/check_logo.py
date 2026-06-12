from PIL import Image
import os

img_path = 'assets/logo.png'
if os.path.exists(img_path):
    img = Image.open(img_path)
    bg_color = (252, 249, 243)
    
    # Find bounding box of pixels that are different from the background color
    width, height = img.size
    left, top, right, bottom = width, height, 0, 0
    
    # We can scan pixels
    # To be fast, let's scan with a tolerance
    tolerance = 15
    for y in range(height):
        for x in range(width):
            p = img.getpixel((x, y))
            # diff from background
            diff = sum(abs(p[i] - bg_color[i]) for i in range(3))
            if diff > tolerance:
                if x < left: left = x
                if x > right: right = x
                if y < top: top = y
                if y > bottom: bottom = y
                
    print(f"Bounding box: left={left}, top={top}, right={right}, bottom={bottom}")
    print(f"Width={right-left}, Height={bottom-top}")
else:
    print("File not found")
