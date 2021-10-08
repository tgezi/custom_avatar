from PIL import Image
import settings

avatar = settings.avatar
background = settings.bg

w, h = avatar.size
background = background.resize((w, h))

for i in range(w):
    for j in range(h):
        color = background.getpixel((i, j))
        alpha = 255 - i // 2
        if alpha < 0:
            alpha = 0
        color = color[:-1] + (alpha,)
        background.putpixel((i, j), color)

avatar.paste(background, (0, 0), background)
avatar.save(settings.res)
print("new avatar is generate!")