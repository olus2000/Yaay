import qrcode
import argparse
from PIL import Image
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask
from qrcode.image.styledpil import StyledPilImage

COLOR_GS = (116, 154, 199)
COLOR_RIGHT = (9, 96, 155)
IMAGE_FOLDER_PATH = '../images/'
IMAGE_PATH = '../images/brochure_template.png'

QR = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=16,
    border=0,
)


def create_qr(text, qr_settings=QR):
    qr_settings.add_data(text)
    qr_settings.make(fit=True)
    img = qr_settings.make_image(image_factory=StyledPilImage,
                                 color_mask=HorizontalGradiantColorMask(right_color=COLOR_RIGHT))
    return img


def create_brochure(qr_img, event):
    with Image.open(IMAGE_PATH) as img:
        img_w, img_h = img.size
        qr_w, qr_h = qr_img.size
        img.paste(qr_img, (img_w - qr_w - 150, img_h - qr_h - 100))
        img.save(IMAGE_FOLDER_PATH + f'brochure_{event}.png')
        return img


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', type=str)
    parser.add_argument('-e', '--event', type=str)
    args = parser.parse_args()
    create_brochure(create_qr(args.text), args.event)
