import cv2 as cv
import numpy as np

from src.fishbot.utils.logger import log

try:
    import mss
except ImportError:
    log("[ERRO] ❌ Biblioteca MSS não encontrada! Instale com: pip install mss")
    log("[ERRO] O bot não pode funcionar sem o MSS.")
    exit(1)


class Detector:
    def __init__(self, config):
        self.unified_config = config
        self.detection_config = config.bot.detection
        self.screen_config = config.bot.screen

        self.templates = self._load_templates()
        self.sct = mss.mss()
        self.monitor = {
            'left': self.screen_config.monitor_x,
            'top': self.screen_config.monitor_y,
            'width': self.screen_config.monitor_width,
            'height': self.screen_config.monitor_height
        }
        log("[INFO] ✅ MSS inicializado")

    def _load_templates(self):
        loaded = {}
        log("[INFO] 📦 Carregando templates...")
        for name in self.detection_config.templates:
            path = self.unified_config.get_template_path(name)
            if path and path.exists():
                img = cv.imread(str(path), cv.IMREAD_UNCHANGED)
                if len(img.shape) == 3 and img.shape[2] == 4:
                    img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
                loaded[name] = img
                log(f"[INFO] ✅ {name}")
            else:
                log(f"[INFO] ❌ {name} - não encontrado em '{path}'")
        return loaded

    def capture_screen(self):
        screenshot = self.sct.grab(self.monitor)
        img = np.array(screenshot)
        return cv.cvtColor(img, cv.COLOR_BGRA2BGR)

    def _get_search_area(self, screen, template_name):
        roi_config = self.detection_config.rois.get(template_name)
        if isinstance(roi_config, str):
            roi = self.detection_config.rois.get(roi_config)
        else:
            roi = roi_config

        if not roi:
            return screen, (0, 0)

        x, y, w, h = roi
        screen_h, screen_w = screen.shape[:2]
        x = max(0, min(x, screen_w - 1))
        y = max(0, min(y, screen_h - 1))
        w = min(w, screen_w - x)
        h = min(h, screen_h - y)

        if w > 0 and h > 0:
            return screen[y:y + h, x:x + w], (x, y)

        return screen, (0, 0)

    def _perform_match(self, search_area, template):
        if search_area.shape[0] < template.shape[0] or search_area.shape[1] < template.shape[1]:
            return None, None

        result = cv.matchTemplate(search_area, template, cv.TM_CCOEFF_NORMED)
        _, confidence, _, location = cv.minMaxLoc(result)
        return confidence, location

    def _calculate_center(self, location, template_shape, offset):
        h_t, w_t = template_shape
        offset_x, offset_y = offset
        return (
            location[0] + w_t // 2 + offset_x + self.screen_config.monitor_x,
            location[1] + h_t // 2 + offset_y + self.screen_config.monitor_y
        )

    def find(self, screen, template_name, debug=False):
        if template_name not in self.templates:
            log(f"[INFO] ❌ Template '{template_name}' não foi carregado.")
            return None

        template = self.templates[template_name]
        search_area, offset = self._get_search_area(screen, template_name)

        confidence, location = self._perform_match(search_area, template)

        if confidence is None:
            return None

        is_match = confidence >= self.detection_config.precision

        if debug:
            status = 'MATCH' if is_match else 'NO MATCH'
            log(f"[DEBUG] [{template_name}] Confiança: {confidence:.2%} (precisa: {self.detection_config.precision:.0%}) -> {status}")

        if is_match:
            return self._calculate_center(location, template.shape[:2], offset)

        return None