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


### OpenCV
```Python
import cv2
import numpy as np


img_src = cv2.imread("sample_board.jpg")

corner_points = [
    (50, 60),   # 左上
    (600, 60),  # 右上
    (50, 400),  # 左下
    (600, 400)  # 右下
]

output_width = 480
output_height = 480

pts1 = np.float32(corner_points)
pts2 = np.float32([[0,0],[output_width,0],[0,output_height],[output_width,output_height]])

mat = cv2.getPerspectiveTransform(pts1,pts2)
img_dst = cv2.warpPerspective(img_src, mat, (output_width, output_height))

cv2.imshow("img_dst", img_dst)
cv2.waitKey()
cv2.destroyAllWindows()
```
