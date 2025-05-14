from PIL import Image
img=Image.open(r"C:\python\ImageProcessing\1066.jpg")
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save(r"C:\python\ImageProcessing\transposed_image.jpg")

transposed_img.show()
print("Image has been transposed and saved as transposed_image.jpg")
