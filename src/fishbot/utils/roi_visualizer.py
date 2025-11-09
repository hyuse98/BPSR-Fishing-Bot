import sys
import multiprocessing
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt, QRect

# Importa as configurações de detecção do seu projeto
from src.fishbot.config.detection_config import DetectionConfig

class RoiVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.detection_config = DetectionConfig()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.WindowTransparentForInput
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.showFullScreen()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        colors = [QColor(255, 0, 0, 150), QColor(0, 255, 0, 150), QColor(0, 0, 255, 150),
                  QColor(255, 255, 0, 150), QColor(255, 0, 255, 150), QColor(0, 255, 255, 150)]
        color_index = 0

        for name, roi in self.detection_config.rois.items():
            if not roi:
                continue

            x, y, w, h = roi
            color = colors[color_index % len(colors)]
            color_index += 1

            pen = QPen(color, 2, Qt.PenStyle.SolidLine)
            painter.setPen(pen)
            painter.drawRect(x, y, w, h)

            font = QFont("Arial", 10, QFont.Weight.Bold)
            painter.setFont(font)
            painter.drawText(x + 5, y + 15, name)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

def main():
    print("Iniciando visualizador de ROIs (PyQt)...")
    print("Pressione a tecla 'Esc' para fechar a janela.")
    
    app = QApplication(sys.argv)
    visualizer = RoiVisualizer()
    visualizer.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
