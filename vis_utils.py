from PIL import Image, ImageDraw, ImageFont
import base64
import numpy as np
from io import BytesIO
import math
from gradio_client import Client, handle_file

def image_formatter(img_path,size=224,vertical_align='middle'):
    img = Image.open(img_path)
    img.thumbnail((size,size), Image.ANTIALIAS)
    with BytesIO() as buffer:
        img.save(buffer, 'jpeg')
        base64_img = base64.b64encode(buffer.getvalue()).decode()
    return f'<img style="vertical-align:{vertical_align}" src="data:image/jpeg;base64,{base64_img}">'


def html_embed_image(img,size=100):
    img =  img.copy()
    img.thumbnail((size,size), Image.ANTIALIAS)
    with BytesIO() as buffer:
        img.save(buffer, 'jpeg')
        base64_img = base64.b64encode(buffer.getvalue()).decode()
    return f'<img style="vertical-align:middle" src="data:image/jpeg;base64,{base64_img}">'

def html_colored_span(content,color):
    return f"<span style='color: {color};'>{content}</span>"


def mask_image(img,mask):
    mask = np.tile(mask[:,:,np.newaxis],(1,1,3))
    img = np.array(img).astype(float)
    img = np.array(mask*img).astype(np.uint8)
    return Image.fromarray(img)

def image_grid(imgs,rows,cols):
    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

def vis_masks(img,objs,labels=None):
    if len(objs)==0:
        return Image.new('RGB',size=img.size)

    imgs = []
    for obj in objs:
        obj_img = mask_image(img, obj['mask'])
        canvas = ImageDraw.Draw(obj_img)
        canvas.rectangle(obj['box'],outline='green',width=4)

        imgs.append(obj_img)

    if labels is not None:
        for img,label in zip(imgs,labels):
            canvas = ImageDraw.Draw(img)
            canvas.text((0,0),label,fill='white')

    cols=math.ceil(math.sqrt(len(imgs)))
    cols=min(3,len(imgs))
    rows=math.ceil(len(imgs)/3)
    return image_grid(imgs, rows, cols)

def turboedit_img(image, src_prompt, target_prompt, seed=2, w1=1):
    client = Client("turboedit/turbo_edit")
    result = client.predict(
        input_image=handle_file(save_image_and_get_path(image)),
        src_prompt=src_prompt,
        tgt_prompt=target_prompt,
        seed=seed,
        w1=w1,
        api_name="/main_pipeline",
    )
    with Image.open(result) as img:
        print(img)
        return img

    # return result

def save_image_and_get_path(image, save_path="output_image.png"):
    if image is None:
        raise ValueError("No image found in init_state dictionary.")
    image.save(save_path, format="PNG") 
    return save_path
