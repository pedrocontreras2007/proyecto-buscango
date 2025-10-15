from reportlab.pdfgen import canvas
from datetime import datetime

class ReportGenerator:
    def generar_reporte_diario(self, buses):
        doc = canvas.Canvas(f"reporte_{datetime.now().strftime('%Y%m%d')}.pdf")
        # Implementar generación del reporte
        doc.save()