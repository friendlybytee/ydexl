import io
import os
import zipfile
from PIL import Image

with zipfile.ZipFile('narnia_thumbnails.zip', 'w') as z:
    for f in sorted(os.listdir('narnia_photos')):
        if not f.endswith('.png'):
            continue
        img = Image.open(os.path.join('narnia_photos', f))
        m = min(img.size)
        img = img.crop((0, 0, m, m)).resize((100, 100), Image.Resampling.LANCZOS)
        b = io.BytesIO()
        img.save(b, 'PNG')
        z.writestr(f, b.getvalue())
