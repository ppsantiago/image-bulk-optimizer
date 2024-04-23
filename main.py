from PIL import Image
import os
import webptools

def resize_image(image, max_width):
    """
    Redimensiona la image si su ancho es mayor que max_width.
    Retorna la image redimensionada y el porcentaje de reducción aplicado.
    """
    width, height = image.size
    if width > max_width:
        reduction = (max_width / float(width))
        new_height = int((float(height) * reduction))
        resized_image = image.resize((max_width, new_height), Image.ANTIALIAS)
        return resized_image, reduction
    else:
        return image, 0

def converter(input, output, calidad=60, max_width=1800):
    try:    
        image = Image.open(input)
        image_resized, reduction = resize_image(image, max_width)
        image_resized.save(output, 'WEBP', quality=calidad)
        print(f"La imagen {input} fue convertida exitosamente.")
    except Exception as e:
        print(f"Error al convertir la imagen {input}: {e}")
 

def main():
    prefix = input("Ingresa el prefijo de tu image: ")
    dir = os.path.dirname(__file__)
    dir_files = os.listdir(dir+'/input/')
    count = 0
    for file in dir_files:
        fil , ext = os.path.splitext(file)
        count = count + 1
        if ext == '.jpg' or ext == '.png' or ext == '.jpeg':
            converter(os.path.join(dir+'/input/', file), os.path.join(dir+'/output/'+prefix+'-('+str(count) +').webp'))


if __name__ == "__main__":
    main()