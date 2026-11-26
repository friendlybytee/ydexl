import random
from PIL import Image

img = Image.open('winter.png').convert('RGB')
w, h = img.size
p = img.load()
a = []
for x in range(w):
    for y in range(h):
        r, g, b = p[x, y]
        if r == g == b and 50 <= r <= 200:
            a.append((x, y))
for x, y in random.sample(a, int(len(a) * 0.3)):
    p[x, y] = (34, 139, 34)
img.save('spring.png')
