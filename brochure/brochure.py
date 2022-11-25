import PIL
from PIL import Image
import qrcode
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask
from qrcode.image.styledpil import StyledPilImage

COLOR_GS = (116, 154, 199)
COLOR_RIGHT = (9, 96, 155)
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
    # img.save('zzz.png')
    return img


def create_brochure(qr_img):
    with Image.open(IMAGE_PATH) as img:
        img_w, img_h = img.size
        qr_w, qr_h = qr_img.size
        img.paste(qr_img, (img_w - qr_w - 150, img_h - qr_h - 100))
        img.save('brochure.png')


if __name__ == "__main__":
    create_brochure(create_qr('asdfasf'))
