import cv2 as cv
import numpy as np

try:
    import mss
except ImportError:
    print("❌ Biblioteca MSS não encontrada! Instale com: pip install mss")
    print("O bot não pode funcionar sem o MSS.")
    exit(1)


class Detector:
    def __init__(self, config):
        self.unified_config = config
        self.config = config.bot
        self.templates = self._load_templates()
        self.sct = mss.mss()
        self.monitor = {
            'left': self.config.monitor_x,
            'top': self.config.monitor_y,
            'width': self.config.monitor_width,
            'height': self.config.monitor_height
        }
        print("✅ MSS inicializado")

    def _load_templates(self):
        loaded = {}
        print("\n📦 Carregando templates...")
        for name in self.config.templates:
            path = self.unified_config.get_template_path(name)
            if path and path.exists():
                img = cv.imread(str(path), cv.IMREAD_UNCHANGED)
                if len(img.shape) == 3 and img.shape[2] == 4:
                    img = cv.cvtColor(img, cv.COLOR_BGRA2BGR)
                loaded[name] = img
                print(f"  ✅ {name}")
            else:
                print(f"  ❌ {name} - não encontrado em '{path}'")
        return loaded

    def capture_screen(self):
        screenshot = self.sct.grab(self.monitor)
        img = np.array(screenshot)
        return cv.cvtColor(img, cv.COLOR_BGRA2BGR)

    def find(self, screen, template_name, debug=False):
        if template_name not in self.templates:
            print(f"❌ Template '{template_name}' não foi carregado.")
            return None

        template = self.templates[template_name]
        roi_config = self.config.rois.get(template_name)

        if isinstance(roi_config, str):
            roi = self.config.rois.get(roi_config)
        else:
            roi = roi_config

        search_area = screen
        offset_x, offset_y = 0, 0

        if roi:
            x, y, w, h = roi
            screen_h, screen_w = screen.shape[:2]
            x = max(0, min(x, screen_w - 1))
            y = max(0, min(y, screen_h - 1))
            w = min(w, screen_w - x)
            h = min(h, screen_h - y)

            if w > 0 and h > 0:
                search_area = screen[y:y + h, x:x + w]
                offset_x, offset_y = x, y

        if search_area.shape[0] < template.shape[0] or search_area.shape[1] < template.shape[1]:
            search_area = screen
            offset_x, offset_y = 0, 0

        result = cv.matchTemplate(search_area, template, cv.TM_CCOEFF_NORMED)
        _, confidence, _, location = cv.minMaxLoc(result)

        if debug:
            print(f"  [{template_name}] Confiança: {confidence:.2%} (precisa: {self.config.precision:.0%})")

        if confidence >= self.config.precision:
            h_t, w_t = template.shape[:2]
            center = (location[0] + w_t // 2 + offset_x + self.config.monitor_x,
                      location[1] + h_t // 2 + offset_y + self.config.monitor_y)
            return center

        return None
