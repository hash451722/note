# Image Processing


## 射影変換 (Projection transform)

### PIL
```Python
from PIL import Image


img_src = Image.open("sample_board.jpg")

point_corners = (
    50, 60,    # 左上
    50, 400,   # 左下
    600, 400,  # 右下
    600, 60    # 右上
    )

img_dst = img_src.transform(
    size = (480, 480),  # The output size in pixels, (width, height).
    method = Image.QUAD,
    data = point_corners,
    resample = Image.BICUBIC
    )

img_dst.show()
```
