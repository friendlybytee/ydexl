from PIL import Image, ImageDraw

n = int(input())
img = Image.new('RGB', (n, n), 'red')
d = ImageDraw.Draw(img)
c = n / 2
r = n / 3
d.ellipse((c - r, c - r, c + r, c + r), fill='yellow')
r = n / 4
d.ellipse((c - r, c - r, c + r, c + r), fill='yellow', outline='red', width=10)
img.save('emblema.png')
