from PIL import Image
img=Image.open('test1.png')
rgb_img=img.convert('RGB')
# r,g,b=rgb_img.getpixel((1,1))
r,g,b=rgb_img.getpixel((150,1))
print(r,g,b)