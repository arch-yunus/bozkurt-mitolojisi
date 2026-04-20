import time
import random
import os
import sys
from interpreter import UluyiInterpreter

class Entity:
    def __init__(self, char, x, y, color):
        self.char = char
        self.x = x
        self.y = y
        self.color = color

    def move(self, width, height):
        self.x = max(0, min(width - 1, self.x + random.randint(-1, 1)))
        self.y = max(0, min(height - 1, self.y + random.randint(-1, 1)))

class Wolf(Entity):
    def __init__(self, x, y):
        super().__init__('W', x, y, '\033[91m') # Red

    def hunt(self, sheeps, width, height):
        if not sheeps:
            self.move(width, height)
            return

        # Find closest sheep
        target = min(sheeps, key=lambda s: (s.x - self.x)**2 + (s.y - self.y)**2)
        
        if target.x > self.x: self.x += 1
        elif target.x < self.x: self.x -= 1
        
        if target.y > self.y: self.y += 1
        elif target.y < self.y: self.y -= 1

class Sheep(Entity):
    def __init__(self, x, y):
        super().__init__('s', x, y, '\033[92m') # Green

def run_simulation(config):
    width = config["width"]
    height = config["height"]
    wolves = [Wolf(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(config["wolf_count"])]
    sheeps = [Sheep(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(config["sheep_count"])]
    
    for i in range(config["iterations"]):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"\033[93m--- {config['title']} --- Döngü: {i+1}/{config['iterations']}\033[0m")
        
        # Grid representation
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Place entities
        for s in sheeps:
            if 0 <= s.y < height and 0 <= s.x < width:
                grid[s.y][s.x] = f"{s.color}{s.char}\033[0m"
        
        for w in wolves:
            if 0 <= w.y < height and 0 <= w.x < width:
                grid[w.y][w.x] = f"{w.color}{w.char}\033[0m"

        # Print grid
        print("+" + "-" * width + "+")
        for row in grid:
            print("|" + "".join(row) + "|")
        print("+" + "-" * width + "+")
        
        # Logic
        for w in wolves:
            w.hunt(sheeps, width, height)
            # Catch sheep
            for s in sheeps[:]:
                if w.x == s.x and w.y == s.y:
                    sheeps.remove(s)
        
        for s in sheeps:
            s.move(width, height)

        if not sheeps:
            print("\033[91mAV TAMAMLANDI. Sürü doydu.\033[0m")
            break
            
        time.sleep(0.1)

if __name__ == "__main__":
    uluy_file = "kadim_strateji.uluy"
    if len(sys.argv) > 1:
        uluy_file = sys.argv[1]
        
    interp = UluyiInterpreter()
    config = interp.parse(uluy_file)
    if config:
        run_simulation(config)
