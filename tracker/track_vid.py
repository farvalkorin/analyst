'''
DAL atk HOU def - Stage 1 - Junkertown

frame 0 to 1175

Dallas gets full held on Junkertown A by Houston
'''
import tesserocr
from PIL import Image

img_path = 'frames/dal_hou_s1s1/frame%04d.jpg'
out_path = 'frames/dal_hou_s1s1/mod/%s%04d.jpg'

def time_left():
    '''
    Pixel box that isolates the current time left for the left team when they
    are attacking
    '''
    # Left, Upper, Right, Lower
    return (760, 50, 825, 75)

def team_left(player_idx):
    '''
    Player 1: (25, 70, 135, 145)
    Player 2: (135, 70, 245, 145)
    Player 3: (245, 70, 355, 145)
    '''
    return (player_idx * 110 + 25, 70, (player_idx+1)*110 + 25, 145)

def ult_left():
    return (25, 10, 55, 40)

fps = 5.0
start_time = 3 * 60 + 54 # 3 min, 5 sec

for img_id in range(500, 1175):
    img_time = start_time - (img_id * fps)

    filled_path = img_path % (img_id+1,)
    image = Image.open(filled_path)
    ult_image = image.crop(team_left(0))
    ult_image = ult_image.crop(ult_left())
    width, height = ult_image.size
    # print(width, height)
    ult_image = ult_image.resize((width * 2, height * 2), Image.BICUBIC)
    where = out_path % ('ultL1_', img_id,)
    ult_image.save(where)
    print(tesserocr.image_to_text(ult_image))

    break
