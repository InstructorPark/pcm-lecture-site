from PIL import Image
import os

img_path = 'assets/logo.png'
if os.path.exists(img_path):
    img = Image.open(img_path).convert('RGBA')
    
    # Bounding box is (138, 162, 2057, 624)
    # Height is 462. Let's crop the square (138, 162, 138 + 462, 162 + 462)
    left = 138
    top = 162
    size = 462
    
    icon_img = img.crop((left, top, left + size, top + size))
    
    # Make background transparent (bg_color = (252, 249, 243))
    bg_color = (252, 249, 243)
    tolerance = 20
    
    datas = icon_img.getdata()
    new_data = []
    for item in datas:
        diff = sum(abs(item[i] - bg_color[i]) for i in range(3))
        if diff < tolerance:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    icon_img.putdata(new_data)
    icon_img.save('assets/logo_icon.png', 'PNG')
    print("Saved logo_icon.png")
else:
    print("File not found")
