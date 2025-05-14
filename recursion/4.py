from PIL import Image
end=100
def show_board():
    img = Image.open(r"C:\python\recursion\snake.jpg")  # Note the r before the string
    img.show()

show_board()
