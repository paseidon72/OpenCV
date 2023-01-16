import matplotlib.pyplot as plt
import pytesseract
import cv2


def open_img(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    plt.axis('off')
    plt.imshow(carplate_img)
    plt.show()

    return carplate_img


def main():
    carplate_img_rgb = open_img(img_path='Users/Dell/PycharmProjects/OpenCV/images/namber_1.jpg')



if __name__ == '__main__':
    main()

