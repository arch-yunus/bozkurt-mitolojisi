import sys
import os
import re

class UluyiInterpreter:
    """
    ULUYI (Kurt Dili) Interpreter
    Kadim bozkır algoritmalarını işlemek için tasarlanmış egzotik dil motoru.
    """
    def __init__(self):
        self.config = {
            "title": "Adsız Strateji",
            "width": 80,
            "height": 24,
            "wolf_count": 3,
            "sheep_count": 10,
            "iterations": 50,
            "speed": 1.0
        }
        self.variables = {}

    def parse(self, file_path):
        if not os.path.exists(file_path):
            print(f"HATA: {file_path} bulunamadı. Kurt izini kaybetti.")
            return False

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # AUUUUUU [Title]
            if line.startswith("AUUUUUU"):
                match = re.search(r'"([^"]*)"', line)
                if match:
                    self.config["title"] = match.group(1)

            # TÖRE [Key] [Value]
            elif line.startswith("TÖRE"):
                parts = line.split()
                if len(parts) >= 3:
                    key = parts[1].lower()
                    val = parts[2]
                    if key == "genişlik": self.config["width"] = int(val)
                    elif key == "yükseklik": self.config["height"] = int(val)

            # BÖRÜ_SAYISI [Int]
            elif line.startswith("BÖRÜ_SAYISI"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["wolf_count"] = int(parts[1])

            # KOYUN_SAYISI [Int]
            elif line.startswith("KOYUN_SAYISI"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["sheep_count"] = int(parts[1])

            # DÖNGÜ [Int]
            elif line.startswith("DÖNGÜ"):
                parts = line.split()
                if len(parts) >= 2:
                    self.config["iterations"] = int(parts[1])

        return self.config

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python interpreter.py <dosya.uluy>")
    else:
        interp = UluyiInterpreter()
        conf = interp.parse(sys.argv[1])
        print(f"--- ULUYI Yapılandırması Yüklendi ---")
        for k, v in conf.items():
            print(f"{k}: {v}")
