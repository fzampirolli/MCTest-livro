import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_transparent_qr_code_with_text(data, filename, text):
    # Gere o QR Code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Crie uma imagem do QR Code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Abra a imagem e adicione um fundo transparente
    qr_image = qr_image.convert('RGBA')
    qr_data = qr_image.getdata()

    new_qr_data = []
    for item in qr_data:
        if item[:3] == (255, 255, 255):
            new_qr_data.append((255, 255, 255, 0))
        else:
            new_qr_data.append(item)

    qr_image.putdata(new_qr_data)

    # Crie uma nova imagem combinando o QR Code com o texto
    img_with_text = Image.new('RGBA', (qr_image.width, qr_image.height + 50))
    img_with_text.paste(qr_image, (0, 0))

    draw = ImageDraw.Draw(img_with_text)
    
    # Especifique o tamanho da fonte desejado
    font_size = 27
    
    # Carregue uma fonte TrueType com o tamanho especificado
    font = ImageFont.truetype("Roboto-Regular.ttf", font_size)
    
    textbbox = draw.textbbox((0, qr_image.height), text, font=font)
    text_position = ((qr_image.width - textbbox[2]) // 2, qr_image.height)
    draw.text(text_position, text, fill=(0, 0, 0, 255), font=font)

    img_with_text.save(filename, format='PNG')

if __name__ == "__main__":
    qr_data = "https://github.com/fzampirolli/mctest"  # Substitua pelo seu link desejado
    qr_filename = "qrcode.png"
    qr_text = "github.com/fzampirolli/mctest"  # Substitua pelo texto desejado
    generate_transparent_qr_code_with_text(qr_data, qr_filename, qr_text)

