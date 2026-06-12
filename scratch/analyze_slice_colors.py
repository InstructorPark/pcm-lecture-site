from PIL import Image
import os

slices = ['scratch/left.png', 'scratch/middle.png', 'scratch/right.png']
for path in slices:
    if os.path.exists(path):
        img = Image.open(path).convert('RGB')
        w, h = img.size
        
        # Count navy pixels and pink pixels
        navy_count = 0
        pink_count = 0
        bg_count = 0
        other_count = 0
        
        bg_color = (252, 249, 243)
        
        for y in range(h):
            for x in range(w):
                p = img.getpixel((x, y))
                # Check if it's bg
                if sum(abs(p[i] - bg_color[i]) for i in range(3)) < 20:
                    bg_count += 1
                elif p[0] < 50 and p[1] < 60 and p[2] > 80: # navy
                    navy_count += 1
                elif p[0] > 180 and p[1] < 150 and p[2] > 120: # pink
                    pink_count += 1
                else:
                    other_count += 1
                    
        total = w * h
        print(f"Slice {path}:")
        print(f"  BG: {bg_count/total*100:.1f}%, Navy: {navy_count/total*100:.1f}%, Pink: {pink_count/total*100:.1f}%, Other: {other_count/total*100:.1f}%")
    else:
        print(f"{path} not found")
