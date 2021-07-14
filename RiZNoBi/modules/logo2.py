#LoDa Lassun
from RiZNoBi.events import register
from RiZNoBi import OWNER_ID
from RiZNoBi import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont


@register(pattern="^/logo11 ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./RiZNoBi/Nobi/riz1.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "yellow"
    shadowcolor = "blue"
    font = ImageFont.truetype("./RiZNoBi/nobi/11.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="green", stroke_width=5, stroke_fill="white")
    fname2 = "RiZNoBi.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Created By RIZ-NOBI")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @DNHxHELL, {e}')
   
   
   
@register(pattern="^/logo12 ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./RiZNoBi/Nobi/riz1.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "yellow"
    shadowcolor = "blue"
    font = ImageFont.truetype("./RiZNoBi/nobi/11.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="red", stroke_width=5, stroke_fill="blue")
    fname2 = "RiZNoBi.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Created By RIZ-NOBI")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @DNHxHELL, {e}')   
   

   
@register(pattern="^/logo13 ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./RiZNoBi/Nobi/riz1.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "yellow"
    shadowcolor = "blue"
    font = ImageFont.truetype("./RiZNoBi/nobi/11.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="blue", stroke_width=5, stroke_fill="white")
    fname2 = "RiZNoBi.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Created By RIZ-NOBI")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @DNHxHELL, {e}')   
   
         

@register(pattern="^/logo14 ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./RiZNoBi/Nobi/riz1.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "yellow"
    shadowcolor = "blue"
    font = ImageFont.truetype("./RiZNoBi/nobi/11.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="pink", stroke_width=5, stroke_fill="white")
    fname2 = "RiZNoBi.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Created By RIZ-NOBI")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @DNHxHELL, {e}')

                                                      