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
        self.sct = None
        self.monitor = {
            'left': self.screen_config.monitor_x,
            'top': self.screen_config.monitor_y,
            'width': self.screen_config.monitor_width,
            'height': self.screen_config.monitor_height
        }

    def _load_templates(self):
        loaded = {}
        log("[INFO] 📦 Carregando templates...")
        for name in self.detection_config.templates:
            path = self.unified_config.get_template_path(name)
            if not (path and path.exists()):
                log(f"[INFO] ❌ {name} - não encontrado em '{path}'")
                continue

            img = cv.imread(str(path), cv.IMREAD_UNCHANGED)
            template_img, mask = None, None

            if img.shape[2] == 4:
                log(f"[INFO] ✅ {name} (com máscara de transparência)")
                mask = img[:, :, 3]
                template_img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
            else:
                log(f"[INFO] ✅ {name}")
                template_img = img
            
            loaded[name] = (template_img, mask)
        return loaded

    def capture_screen(self):
        if self.sct is None:
            self.sct = mss.mss()
            log("[INFO] ✅ MSS inicializado na thread do bot")

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

    def _perform_match(self, search_area, template_data):
        template_img, mask = template_data

        search_gray = cv.cvtColor(search_area, cv.COLOR_BGR2GRAY)
        template_gray = cv.cvtColor(template_img, cv.COLOR_BGR2GRAY)

        if search_gray.shape[0] < template_gray.shape[0] or search_gray.shape[1] < template_gray.shape[1]:
            return None, None

        result = cv.matchTemplate(search_gray, template_gray, cv.TM_CCOEFF_NORMED, mask=mask)
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

        template_data = self.templates[template_name]
        template_img, _ = template_data

        search_area, offset = self._get_search_area(screen, template_name)
        confidence, location = self._perform_match(search_area, template_data)

        if confidence is None:
            return None

        precision = self.detection_config.precision
        is_match = confidence >= precision

        if debug:
            status = 'MATCH' if is_match else 'NO MATCH'
            log(f"[DEBUG] [{template_name}] Confiança: {confidence:.2%} (precisa: {precision:.0%}) -> {status}")

        if is_match:
            return self._calculate_center(location, template_img.shape[:2], offset)

        return None