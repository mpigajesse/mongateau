"""
Générateur de tickets PDF pour les commandes MonGâteau
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime
import os
from django.conf import settings


def generate_order_ticket(order):
    """
    Génère un ticket PDF pour une commande
    
    Args:
        order: Instance du modèle Order
    
    Returns:
        str: Chemin du fichier PDF généré
    """
    # Créer le nom du fichier
    filename = f"ticket_{order.order_number}.pdf"
    filepath = os.path.join(settings.TICKETS_DIR, filename)
    
    # Créer le document PDF
    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Container pour les éléments du PDF
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Style titre
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#FF6B9D'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Style sous-titre
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#666666'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Style normal
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        alignment=TA_LEFT
    )
    
    # Titre
    elements.append(Paragraph("🍰 MonGâteau", title_style))
    elements.append(Paragraph("Ticket de Réservation", subtitle_style))
    elements.append(Spacer(1, 0.5*cm))
    
    # Ligne de séparation
    line_data = [['_' * 80]]
    line_table = Table(line_data, colWidths=[16*cm])
    line_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#CCCCCC')),
        ('ALIGNMENT', (0, 0), (-1, -1), 'CENTER'),
    ]))
    elements.append(line_table)
    elements.append(Spacer(1, 0.5*cm))
    
    # Informations de commande
    data = [
        ['Numéro de commande:', order.order_number],
        ['Date de commande:', order.created_at.strftime('%d/%m/%Y %H:%M')],
        ['', ''],
        ['Client:', order.customer_name],
        ['Téléphone:', order.customer_phone],
        ['', ''],
        ['Type de gâteau:', order.cake_type.name],
        ['Description:', order.cake_type.description],
    ]
    
    if order.custom_message:
        data.append(['Message personnalisé:', order.custom_message])
    
    data.extend([
        ['', ''],
        ['Date de livraison:', order.delivery_date.strftime('%d/%m/%Y')],
        ['Adresse de livraison:', order.delivery_address],
        ['', ''],
        ['Prix total:', f"{order.total_price} FCFA"],
        ['Mode de paiement:', 'À LA LIVRAISON'],
    ])
    
    # Création du tableau
    table = Table(data, colWidths=[5*cm, 11*cm])
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#333333')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#666666')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 1*cm))
    
    # Note importante
    note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#FF6B9D'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    elements.append(Paragraph("⚠️ IMPORTANT", note_style))
    elements.append(Paragraph(
        "Veuillez conserver ce ticket pour la récupération de votre commande.<br/>"
        "Le paiement s'effectue à la livraison.",
        normal_style
    ))
    
    elements.append(Spacer(1, 1*cm))
    
    # Pied de page
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#999999'),
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    
    elements.append(Paragraph("MonGâteau — pâtisserie artisanale", footer_style))
    elements.append(Paragraph("MonGâteau - Des gâteaux artisanaux avec amour 💕", footer_style))
    
    # Générer le PDF
    doc.build(elements)
    
    return filepath
