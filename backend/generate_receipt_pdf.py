from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime
import os

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from backend.translations import translations


# -----------------------------
# FONT REGISTRATION
# -----------------------------
def register_fonts():
    pdfmetrics.registerFont(TTFont('Hindi', 'backend/fonts/NotoSansDevanagari-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Tamil', 'backend/fonts/NotoSansTamil-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Telugu', 'backend/fonts/NotoSansTelugu-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Malayalam', 'backend/fonts/NotoSansMalayalam-Regular.ttf'))


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def generate_receipt_pdf(receipt_id, voter_name, voter_id, system_status, lang="en"):

    register_fonts()

    # 🔥 Select translation
    text = translations.get(lang, translations["en"])

    # 🔥 Font mapping
    font_map = {
        "en": "Helvetica",
        "hi": "Hindi",
        "ta": "Tamil",
        "te": "Telugu",
        "ml": "Malayalam"
    }

    font_name = font_map.get(lang, "Helvetica")

    # 🔥 Custom style with font
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        name="Custom",
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=11
    )

    title_style = ParagraphStyle(
        name="Title",
        parent=styles['Title'],
        fontName=font_name
    )

    # 🔥 File creation
    filename = f"receipt_{receipt_id}.pdf"
    filepath = os.path.abspath(filename)

    content = []

    # -----------------------------
    # TITLE
    # -----------------------------
    content.append(Paragraph(f"<b>{text['title']}</b>", title_style))
    content.append(Spacer(1, 20))

    # -----------------------------
    # BASIC DETAILS
    # -----------------------------
    content.append(Paragraph(f"<b>{text['voter_name']}:</b> {voter_name}", custom_style))
    content.append(Paragraph(f"<b>{text['voter_id']}:</b> {voter_id}", custom_style))
    content.append(Paragraph(f"<b>{text['receipt_id']}:</b> {receipt_id}", custom_style))
    content.append(Paragraph(f"<b>{text['date']}:</b> {datetime.now()}", custom_style))

    content.append(Spacer(1, 15))

    # -----------------------------
    # SYSTEM STATUS
    # -----------------------------
    if system_status == "COMPROMISED":

        content.append(
            Paragraph(
                f"<b>{text['system_status']}:</b> <font color='red'>{text['compromised']}</font>",
                custom_style
            )
        )

        content.append(
            Paragraph(text["warn_msg"], custom_style)
        )

    else:

        content.append(
            Paragraph(
                f"<b>{text['system_status']}:</b> <font color='green'>{text['safe']}</font>",
                custom_style
            )
        )

        content.append(
            Paragraph(text["safe_msg"], custom_style)
        )

    content.append(Spacer(1, 20))

    # -----------------------------
    # DESCRIPTION
    # -----------------------------
    content.append(
        Paragraph(text["desc"], custom_style)
    )

    content.append(Spacer(1, 20))

    # -----------------------------
    # FOOTER NOTE
    # -----------------------------
    content.append(
        Paragraph(f"<i>{text['note']}</i>", custom_style)
    )

    # -----------------------------
    # BUILD PDF
    # -----------------------------
    doc = SimpleDocTemplate(filepath)
    doc.build(content)

    print("\nPDF Receipt Generated:", filepath)

    return filepath