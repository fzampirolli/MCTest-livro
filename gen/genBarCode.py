import cv2
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

def generate_isbn_barcode(isbn):
    # Gere o código de barras EAN-13 para o ISBN fornecido
    ean = EAN13(isbn, writer=ImageWriter())

    # Salve o código de barras gerado como uma imagem PNG
    filename = ean.save('barcode')

    # Abra a imagem usando a biblioteca cv2
    image = cv2.imread(filename)

    # Configurar o texto a ser inserido
    # 978-65-00-79086-3
    text = "ISBN " + isbn[:3]+'-'+ isbn[3:5]+'-'+ isbn[5:7]+'-'+ isbn[7:12]+'-'+ isbn[12]
    image[200:,:] = (255,255,255)
    print(image.shape)
    image = image[:-20,:]
    print(image.shape)
    # Configurar a posição do texto
    text_position = (58, image.shape[0] - 10)

    # Desenhar o texto na imagem
    cv2.putText(image, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2, cv2.LINE_AA)

    # Salvar a imagem com o texto
    cv2.imwrite('barcode.png', image)
  

    # Abra a imagem e converta o fundo branco em transparente
    barcode_image = Image.open(filename)
    barcode_image = barcode_image.convert('RGBA')
    barcode_data = barcode_image.getdata()

    new_barcode_data = []
    for item in barcode_data:
        if item[:3] >= (250, 250, 250):
            new_barcode_data.append((255, 255, 255, 0))
        else:
            new_barcode_data.append(item)

    barcode_image.putdata(new_barcode_data)
    barcode_image.save('barcode-impresso.png', format='PNG')

if __name__ == "__main__":
    isbn = "9786500790863"  # Substitua pelo ISBN desejado
    generate_isbn_barcode(isbn)
