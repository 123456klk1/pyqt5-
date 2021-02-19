import os
import cv2 as cv
def img_save(save_path, img):
    """
    该函数用于保存单张图像
    :param path: 保存地址，str
    :param img: 图像矩阵， np.array
    :return:
    """
    print(save_path, img)
    # plt.imsave(save_path, img, cmap="gray")
    i = 0
    path = save_path.replace("/", "\\")
    save_path = os.path.join(path, str(i)+".jpg")
    while os.path.exists(save_path):
        i += 1
        save_path = os.path.join(path, str(i) + ".jpg")
    cv.imwrite(save_path, img)



