import cv2

# Read the image
img = cv2.imread(r"C:\python\ImageProcessing\1066.jpg")

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create CLAHE object
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Apply CLAHE
enh_img = clahe.apply(gray_img)

# Save the enhanced image
cv2.imwrite(r"C:\python\ImageProcessing\enhanced.jpg", enh_img)
print("Done Enhancing")
