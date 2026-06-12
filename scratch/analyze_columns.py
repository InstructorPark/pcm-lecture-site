from PIL import Image
import os

img_path = 'assets/logo.png'
if os.path.exists(img_path):
    img = Image.open(img_path).convert('RGB')
    width, height = img.size
    bg_color = (252, 249, 243)
    
    # Let's save three segments: left, middle, right to see what they contain
    # Or let's analyze columns: count number of non-background pixels in each column
    non_bg_cols = []
    tolerance = 15
    for x in range(width):
        count = 0
        for y in range(height):
            p = img.getpixel((x, y))
            diff = sum(abs(p[i] - bg_color[i]) for i in range(3))
            if diff > tolerance:
                count += 1
        non_bg_cols.append(count)
        
    # Print column density summary
    # Let's group into 10 bins and print
    bin_size = width // 10
    print("Column density bins (10):")
    for i in range(10):
        start = i * bin_size
        end = (i + 1) * bin_size if i < 9 else width
        avg = sum(non_bg_cols[start:end]) / (end - start)
        print(f"Bin {i} ({start}-{end}): avg non-bg pixels = {avg:.1f}")
        
else:
    print("File not found")
