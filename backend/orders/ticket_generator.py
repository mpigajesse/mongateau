"""
Générateur de tickets JPG ultra-premium avec QR code pour les commandes MonGâteau
Design style ThemeForest/Envato Premium avec glassmorphism et effets modernes
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import qrcode
import os
from django.conf import settings
from datetime import datetime


def generate_order_ticket(order):
    """
    Génère un ticket JPG ultra-premium avec design ThemeForest et QR code de vérification
    
    Args:
        order: Instance du modèle Order
    
    Returns:
        str: Chemin du fichier JPG généré
    """
    # Dimensions compactes (ticket réduit)
    width = 1200
    height = 800
    
    # === CRÉATION DU CANVAS PRINCIPAL ===
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # === ARRIÈRE-PLAN DÉGRADÉ ULTRA-PREMIUM (NEUTRE) ===
    # Dégradé gris élégant: Anthracite → Gris clair → Ivoire
    for y in range(height):
        progress = y / height
        
        if progress < 0.5:
            # Anthracite vers gris moyen
            factor = progress * 2
            r = int(45 + (120 - 45) * factor)   # #2D2D2D → #787878
            g = int(45 + (120 - 45) * factor)
            b = int(45 + (120 - 45) * factor)
        else:
            # Gris moyen vers ivoire
            factor = (progress - 0.5) * 2
            r = int(120 + (245 - 120) * factor)  # #787878 → #F5F5F0
            g = int(120 + (245 - 120) * factor)
            b = int(120 + (240 - 120) * factor)
        
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))
    
    # === OVERLAY AVEC FORMES DÉCORATIVES (NEUTRE) ===
    overlay = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # Grands cercles décoratifs (style ThemeForest - neutre)
    # Cercle top-right
    overlay_draw.ellipse([1200, -300, 2100, 600], fill=(255, 255, 255, 20))
    overlay_draw.ellipse([1250, -250, 2050, 550], fill=(255, 255, 255, 12))
    
    # Cercle bottom-left
    overlay_draw.ellipse([-300, 800, 600, 1700], fill=(255, 255, 255, 18))
    overlay_draw.ellipse([-250, 850, 550, 1650], fill=(255, 255, 255, 10))
    
    # Petits cercles accent gris clair
    overlay_draw.ellipse([100, 100, 250, 250], fill=(255, 255, 255, 15))
    overlay_draw.ellipse([1600, 950, 1750, 1100], fill=(255, 255, 255, 12))
    
    # Fusionner l'overlay
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    # === CARTE PRINCIPALE GLASSMORPHISM ===
    card_margin = 70
    card_x1 = card_margin
    card_y1 = 90
    card_x2 = width - card_margin
    card_y2 = height - 60
    card_radius = 24
    
    # Effet d'ombre portée multicouche
    shadow_layers = [
        (15, 15, (0, 0, 0, 60)),
        (10, 10, (0, 0, 0, 40)),
        (5, 5, (0, 0, 0, 30))
    ]
    
    for offset_x, offset_y, color in shadow_layers:
        draw.rounded_rectangle(
            [card_x1 + offset_x, card_y1 + offset_y, card_x2 + offset_x, card_y2 + offset_y],
            radius=card_radius,
            fill=color
        )
    
    # Carte blanche principale avec bordure dorée
    draw.rounded_rectangle(
        [card_x1, card_y1, card_x2, card_y2],
        radius=card_radius,
        fill='white',
        outline='#C0C0C0',
        width=3
    )
    
    # === CHARGEMENT DES POLICES ===
    try:
        # Linux fonts
        font_brand = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
        font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        font_value = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_highlight = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        try:
            # Windows fonts
            font_brand = ImageFont.truetype("arial.ttf", 70)
            font_title = ImageFont.truetype("arialbd.ttf", 38)
            font_subtitle = ImageFont.truetype("arial.ttf", 26)
            font_label = ImageFont.truetype("arialbd.ttf", 22)
            font_value = ImageFont.truetype("arial.ttf", 24)
            font_highlight = ImageFont.truetype("arialbd.ttf", 48)
            font_small = ImageFont.truetype("arial.ttf", 18)
        except:
            # Fallback
            font_brand = ImageFont.load_default()
            font_title = ImageFont.load_default()
            font_subtitle = ImageFont.load_default()
            font_label = ImageFont.load_default()
            font_value = ImageFont.load_default()
            font_highlight = ImageFont.load_default()
            font_small = ImageFont.load_default()
    
    # === HEADER SUPPRIMÉ ===
    # Logo MonGâteau supprimé
    
    # === BADGE "TICKET DE RÉSERVATION" ===
    badge_y = card_y1 + 18
    badge_text = "TICKET DE RÉSERVATION"
    badge_bbox = draw.textbbox((0, 0), badge_text, font=font_title)
    badge_width = badge_bbox[2] - badge_bbox[0]
    badge_x = (width - badge_width) // 2
    
    # Badge background neutre
    badge_bg_x1 = badge_x - 40
    badge_bg_y1 = badge_y - 12
    badge_bg_x2 = badge_x + badge_width + 40
    badge_bg_y2 = badge_y + 42
    
    draw.rounded_rectangle(
        [badge_bg_x1, badge_bg_y1, badge_bg_x2, badge_bg_y2],
        radius=14,
        fill='#3A3A3A'
    )
    
    draw.text((badge_x, badge_y), badge_text, fill='#F5F5F0', font=font_title)
    
    # === LAYOUT EN 2 COLONNES ===
    col_left_x = card_x1 + 36
    col_right_x = card_x1 + (card_x2 - card_x1) // 2 + 40  # Décalage plus large
    content_y = badge_bg_y2 + 38  # Plus d'espace sous le badge
    
    # === COLONNE GAUCHE: INFORMATIONS PRINCIPALES ===
    
    # NUMÉRO DE COMMANDE (Très visible)
    order_y = content_y
    draw.text((col_left_x, order_y), "N° COMMANDE", fill='#3A3A3A', font=font_label)
    # Ajout d'espace entre le label et le numéro
    order_num_y = order_y + 36
    order_num_bg = [col_left_x - 10, order_num_y - 6, col_left_x + 320, order_num_y + 54]
    draw.rounded_rectangle(order_num_bg, radius=8, fill='#F2F2F2', outline='#B0B0B0', width=2)
    draw.text((col_left_x + 12, order_num_y), order.order_number, fill='#2B2B2B', font=font_title)
    
    # CLIENT
    client_y = order_num_y + 80
    draw.text((col_left_x, client_y), "CLIENT", fill='#666666', font=font_label)
    draw.text((col_left_x, client_y + 36), order.customer_name, fill='#333333', font=font_value)
    
    # TÉLÉPHONE
    phone_y = client_y + 70
    draw.text((col_left_x, phone_y), "TÉLÉPHONE", fill='#666666', font=font_label)
    draw.text((col_left_x, phone_y + 36), order.customer_phone, fill='#333333', font=font_value)
    
    # TYPE DE GÂTEAU
    cake_y = phone_y + 70
    draw.text((col_left_x, cake_y), "GÂTEAU", fill='#666666', font=font_label)
    cake_name = _truncate_text(order.cake_type.name, 25)
    draw.text((col_left_x, cake_y + 36), cake_name, fill='#333333', font=font_value)
    
    # DESCRIPTION
    desc_y = cake_y + 70
    draw.text((col_left_x, desc_y), "DESCRIPTION", fill='#666666', font=font_label)
    cake_desc = _truncate_text(order.cake_type.description, 30)
    draw.text((col_left_x, desc_y + 36), cake_desc, fill='#333333', font=font_small)
    
    # === COLONNE DROITE: LIVRAISON & QR CODE ===
    
    # LIVRAISON
    delivery_y = content_y + 16
    draw.text((col_right_x, delivery_y), "LIVRAISON", fill='#666666', font=font_label)
    delivery_date = order.delivery_date.strftime('%d/%m/%Y')
    draw.text((col_right_x, delivery_y + 36), delivery_date, fill='#333333', font=font_value)
    
    # ADRESSE
    address_y = delivery_y + 80
    draw.text((col_right_x, address_y), "ADRESSE", fill='#666666', font=font_label)
    
    # Multi-lignes pour l'adresse
    address_lines = _wrap_text(order.delivery_address, 30)
    address_text_y = address_y + 36
    for line in address_lines[:2]:  # Max 2 lignes
        draw.text((col_right_x, address_text_y), line, fill='#333333', font=font_small)
        address_text_y += 26
    
    # MESSAGE PERSONNALISÉ (si existe)
    if order.custom_message:
        msg_y = address_text_y + 16
        draw.text((col_right_x, msg_y), "MESSAGE", fill='#666666', font=font_label)
        msg_lines = _wrap_text(order.custom_message, 30)
        msg_text_y = msg_y + 32
        for line in msg_lines[:2]:  # Max 2 lignes
            draw.text((col_right_x, msg_text_y), f'"{line}"', fill='#8A2387', font=font_small)
            msg_text_y += 26
    
    # QR CODE (plus compact)
    qr_y = content_y + 240
    qr_size = 170
    
    # Générer le QR code
    verification_url = f"http://localhost:8000/verify/{order.order_number}/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=2,
    )
    qr.add_data(verification_url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="#2B2B2B", back_color="white")
    qr_img = qr_img.resize((qr_size, qr_size))
    
    # Background pour QR code (neutre)
    qr_bg_margin = 16
    qr_bg = [
        col_right_x - qr_bg_margin, 
        qr_y - qr_bg_margin, 
        col_right_x + qr_size + qr_bg_margin, 
        qr_y + qr_size + qr_bg_margin
    ]
    draw.rounded_rectangle(qr_bg, radius=15, fill='#F2F2F2', outline='#C0C0C0', width=3)
    
    # Coller le QR code
    img.paste(qr_img, (col_right_x, qr_y))
    
    # Texte sous le QR code supprimé
        # === DATE DE CRÉATION sous le QR code ===
    created_text = f"Créé le {order.created_at.strftime('%d/%m/%Y à %H:%M')}"
    # Calculer la largeur du texte pour centrer sous le QR code
    qr_date_y = qr_y + qr_size + 36
    created_bbox = draw.textbbox((0, 0), created_text, font=font_small)
    created_width = created_bbox[2] - created_bbox[0]
    created_x = col_right_x + (qr_size - created_width) // 2
    draw.text((created_x, qr_date_y), created_text, fill='#999999', font=font_small)
    
    # === PRIX TOTAL (Bottom highlight) ===
    price_y = card_y2 - 90
    price_width = card_x2 - card_x1 - 100
    price_x = card_x1 + 50
    
    # Rectangle premium pour le prix (neutre)
    price_bg = [price_x, price_y, price_x + price_width, price_y + 80]
    draw.rounded_rectangle(price_bg, radius=15, fill='#2B2B2B')
    
    # Ligne argentée supprimée
    
    price_label = "PRIX TOTAL"
    price_value = f"{order.total_price} FCFA"
    
    draw.text((price_x + 40, price_y + 12), price_label, fill='#F5F5F0', font=font_subtitle)
    draw.text((price_x + 40, price_y + 42), price_value, fill='#C0C0C0', font=font_title)
    
    # Paiement à la livraison (sans icône)
    payment_text = "Paiement à la livraison"
    payment_x = price_x + price_width - 320
    draw.text((payment_x, price_y + 32), payment_text, fill='#F5F5F0', font=font_small)
    
    # Footer supprimé
    
    # Date de création supprimée
    
    # === SAUVEGARDER L'IMAGE ===
    filename = f"ticket_{order.order_number}.jpg"
    filepath = os.path.join(settings.TICKETS_DIR, filename)
    
    # Sauvegarder avec haute qualité
    img.save(filepath, 'JPEG', quality=95, optimize=True)
    
    return filepath


def _truncate_text(text, max_length):
    """Tronque le texte s'il dépasse la longueur maximale"""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def _wrap_text(text, max_chars_per_line):
    """Découpe le texte en plusieurs lignes"""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= max_chars_per_line:
            current_line.append(word)
            current_length += len(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines
