from PIL import Image

avatar = Image.open("test.jpeg")
nf = Image.open("national_flag.png")

w, h = avatar.size
nf = nf.resize((w, h))

for i in range(w):
    for j in range(h):
        color = nf.getpixel((i, j))
        alpha = 255 - i // 2
        if alpha < 0:
            alpha = 0
        color = color[:-1] + (alpha,)
        nf.putpixel((i, j), color)

avatar.paste(nf, (0, 0), nf)
avatar.save("national_avatar.png")
print("new avatar is generate!")
