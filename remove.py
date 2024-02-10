from rembg import remove
from PIL import Image
image_input = Image.open("K:\Workbench\Snake Game\channels4_profile.jpg")
output=remove(image_input)
output.save("K:\Workbench\Snake Game\output.png")