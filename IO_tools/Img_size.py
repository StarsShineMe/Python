import time

from PIL import Image

def Img_size(img,size,save = 1,savePath = 'img'):
    # 打开图片
    image = Image.open(f'{img}')

    # 缩放图片
    resized_image = image.resize(size, Image.Resampling.LANCZOS)
    if save == 1 and savePath != 'img':
        # 保存缩放后的图片
        resized_image.save(f'{savePath}')
    if save == 1 and savePath == 'img':
        # 保存缩放后的图片
        resized_image.save(f'{img}')
    return resized_image
if __name__ == '__main__':
    a = time.time()
    Img_size(r"D:\code\python\Projects\Scripting tools3.0\test tools\img.png", (1604, 2945))
    b = time.time()
    print(b - a)

