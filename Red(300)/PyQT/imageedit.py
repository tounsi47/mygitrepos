from PIL import Image , ImageFilter
with Image.open('fedora-30-wallpaper.jpg') as original :
    mirrored = original.transpose(Image.ROTATE_90)
    gray = original.convert('L')
    original.show()
    mirrored.show()
    gray.show()