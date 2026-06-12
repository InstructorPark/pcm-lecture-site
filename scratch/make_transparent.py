from PIL import Image
import os

img_path = 'assets/logo.png'
if os.path.exists(img_path):
    img = Image.open(img_path).convert('RGBA')
    datas = img.getdata()
    
    new_data = []
    bg_color = (252, 249, 243)
    tolerance = 20  # color distance tolerance
    
    for item in datas:
        # Check if the pixel is close to the background color
        diff = sum(abs(item[i] - bg_color[i]) for i in range(3))
        if diff < tolerance:
            # Make it transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    # Save the transparent image
    out_path = 'assets/logo_transparent.png'
    img.save(out_path, 'PNG')
    print(f"Saved transparent image to {out_path}")
    
    # Let's also find the bounding box of non-transparent pixels in the new image
    bbox = img.getbbox()
    print("Transparent image BBox:", bbox)
    if bbox:
        print("Cropped size:", bbox[2]-bbox[0], "x", bbox[3]-bbox[1])
        # Save a cropped version as well
        cropped = img.crop(bbox)
        cropped.save('assets/logo_cropped.png', 'PNG')
        print("Saved cropped version to assets/logo_cropped.png")
else:
    print("File not found")
