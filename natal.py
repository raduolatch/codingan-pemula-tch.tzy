import pygame
import random
import time
import os

# ===== PATH MUSIK =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIK = os.path.join(BASE_DIR, "natal.mp3")

# ===== WARNA =====
HIJAU = "\033[92m"
COKLAT = "\033[33m"
KUNING = "\033[93m"
PUTIH = "\033[97m"
RESET = "\033[0m"

HIASAN = [
    "\033[91m", "\033[94m", "\033[95m", "\033[96m"
]

# ===== MUSIK =====
def musik():
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIK)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # loop terus

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def gambar_pohon(tinggi_daun, tinggi_batang):
    pohon = []
    pohon.append(" " * (tinggi_daun - 1) + KUNING + "★" + RESET)

    for i in range(tinggi_daun):
        spasi = " " * (tinggi_daun - i - 1)
        daun = ""
        for _ in range(2 * i + 1):
            if random.randint(1, 6) == 1:
                daun += random.choice(HIASAN) + "o"
            else:
                daun += HIJAU + "*"
        pohon.append(spasi + daun + RESET)

    for _ in range(tinggi_batang):
        pohon.append(" " * (tinggi_daun - 1) + COKLAT + "||" + RESET)

    return pohon

def salju_jatuh():
    tinggi_daun = 10
    tinggi_batang = 3
    pohon = gambar_pohon(tinggi_daun, tinggi_batang)

    tinggi_layar = len(pohon) + 5
    lebar = tinggi_daun * 2
    salju = []

    while True:
        clear()

        if random.randint(1, 2) == 1:
            salju.append([0, random.randint(0, lebar)])

        layar = [[" " for _ in range(lebar + 1)] for _ in range(tinggi_layar)]
        for s in salju:
            if s[0] < tinggi_layar:
                layar[s[0]][s[1]] = PUTIH + "*" + RESET
            s[0] += 1

        salju = [s for s in salju if s[0] < tinggi_layar]

        for i in range(tinggi_layar):
            if i < len(pohon):
                print(pohon[i])
            else:
                print("".join(layar[i]))

        time.sleep(0.2)

# ▶️ JALANKAN
musik()
salju_jatuh()
