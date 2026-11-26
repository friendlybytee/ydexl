import json
from PIL import Image, ImageDraw

with open("coat_of_arms.json", encoding="utf-8") as f:
    a = json.load(f)

img = Image.new("RGB", (800, 800), "white")
d = ImageDraw.Draw(img)
d.rectangle((0, 0, 799, 799), fill=a["background"], outline=a["border"]["color"], width=a["border"]["width"])

e = a["emblem"]
x, y = e["position"]
if e["shape"] == "circle":
    r = e["radius"]
    d.ellipse((x - r, y - r, x + r, y + r), fill=e["color"])
else:
    s = e["side"] / 2
    d.rectangle((x - s, y - s, x + s, y + s), fill=e["color"])

for b in a["symbols"]:
    x, y = b["position"]
    s = b["size"]
    if b["shape"] == "star":
        r = s / 2
        w = s / 10
        p = [(x, y - r), (x + w, y - w), (x + r, y), (x + w, y + w),
             (x, y + r), (x - w, y + w), (x - r, y), (x - w, y - w)]
        d.polygon(p, fill=b["color"])
    else:
        w = s / 10
        d.rectangle((x - w, y - s / 2, x + w, y + s / 2), fill=b["color"])
        d.rectangle((x - s / 2, y - w, x + s / 2, y + w), fill=b["color"])

img.save("narnia_shield.png")
