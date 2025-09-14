#!/usr/bin/env python3
"""
Script pour transformer les couleurs orange des logos en couleurs noires.
Transforme les nuances orange en noir (#000000) pour un aspect ultra sérieux monochrome.
"""

from PIL import Image
import numpy as np
import os

def rgb_to_hsv(rgb):
    """Convertit RGB vers HSV"""
    r, g, b = rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val

    if max_val == min_val:
        h = 0
    elif max_val == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif max_val == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    if max_val == 0:
        s = 0
    else:
        s = diff / max_val

    v = max_val

    return h, s, v

def hsv_to_rgb(hsv):
    """Convertit HSV vers RGB"""
    h, s, v = hsv
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x
    else:
        r, g, b = 0, 0, 0

    return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)

def is_orange_color(pixel):
    """Détecte si un pixel est dans les tons orange/rouge-orange"""
    if len(pixel) < 3:
        return False

    r, g, b = pixel[0], pixel[1], pixel[2]

    # Ignorer les pixels transparents si alpha channel existe
    if len(pixel) == 4 and pixel[3] < 128:
        return False

    # Détection des tons orange/coral (plage HSV approximative)
    h, s, v = rgb_to_hsv((r, g, b))

    # Orange: hue entre 0-60 (rouge-orange)
    # Saturation élevée (> 0.3) et luminosité élevée (> 0.3)
    return (0 <= h <= 60 or 300 <= h <= 360) and s > 0.3 and v > 0.3

def transform_orange_to_black(pixel):
    """Transforme un pixel orange en noir professionnel"""
    if len(pixel) < 3:
        return pixel

    r, g, b = pixel[0], pixel[1], pixel[2]
    alpha = pixel[3] if len(pixel) == 4 else 255

    # Si ce n'est pas orange, on garde la couleur originale
    if not is_orange_color(pixel):
        return pixel

    # Convertir vers HSV pour préserver la luminosité et saturation
    h, s, v = rgb_to_hsv((r, g, b))

    # Couleur cible: Noir professionnel #000000
    target_r, target_g, target_b = 0, 0, 0  # #000000
    target_h, target_s, target_v = rgb_to_hsv((target_r, target_g, target_b))

    # Transformation agressive vers le noir pur
    # Tous les pixels orange deviennent complètement noirs
    new_r, new_g, new_b = 0, 0, 0  # #000000 - Noir pur

    # new_r, new_g, new_b déjà définis ci-dessus

    if len(pixel) == 4:
        return (new_r, new_g, new_b, alpha)
    else:
        return (new_r, new_g, new_b)

def transform_logo(input_path, output_path):
    """Transforme un logo en remplaçant orange par bleu professionnel"""
    try:
        # Ouvrir l'image
        img = Image.open(input_path)
        img = img.convert("RGBA")  # Assurer le support alpha

        # Convertir en array numpy pour traitement
        img_array = np.array(img)

        print(f"Transformation de {input_path}...")
        print(f"Taille: {img_array.shape}")

        # Traiter chaque pixel
        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                original_pixel = tuple(img_array[i, j])
                new_pixel = transform_orange_to_black(original_pixel)
                img_array[i, j] = new_pixel

        # Convertir de retour en image PIL
        new_img = Image.fromarray(img_array, mode='RGBA')

        # Sauvegarder
        if output_path.endswith('.png'):
            new_img.save(output_path, 'PNG')
        else:
            # Convertir en RGB pour JPG
            rgb_img = Image.new('RGB', new_img.size, (255, 255, 255))
            rgb_img.paste(new_img, mask=new_img.split()[-1])  # Use alpha channel as mask
            rgb_img.save(output_path, 'JPEG', quality=95)

        print(f"Logo transforme sauvegarde: {output_path}")

    except Exception as e:
        print(f"Erreur lors de la transformation de {input_path}: {str(e)}")

def main():
    """Fonction principale pour transformer tous les logos"""
    logos_dir = "logos"

    # Fichiers à traiter
    files_to_transform = [
        ("logo.png", "logo_professional.png"),
        ("logo_ECL.jpg", "logo_ECL_black.jpg")
    ]

    print("Transformation des couleurs orange vers noir professionnel")
    print("Couleurs cibles: Noir #000000 et gris foncés (ultra serieux et monochrome)")
    print()

    for input_file, output_file in files_to_transform:
        input_path = os.path.join(logos_dir, input_file)
        output_path = os.path.join(logos_dir, output_file)

        if os.path.exists(input_path):
            transform_logo(input_path, output_path)
        else:
            print(f"Fichier non trouve: {input_path}")

    print()
    print("Transformation terminee!")
    print("Les nouveaux logos utilisent maintenant du noir et des gris foncés")
    print("au lieu de l'orange, pour un aspect ultra serieux et monochrome.")

if __name__ == "__main__":
    main()