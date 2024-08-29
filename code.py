import time
import board
import neopixel
import random

# Set up the NeoPixels on the Neo Trinkey
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.5, auto_write=False)

# Helper function to randomize brightness
def randomize_brightness():
    pixels.brightness = random.uniform(0.1, 1)
# Existing Disco-inspired effects

def classic_strobe():
    randomize_brightness()
    for _ in range(10):  # Strobe 10 times
        pixels.fill((255, 255, 255))
        pixels.show()
        time.sleep(0.05)  # Fast flash
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.05)

def multi_color_flash():
    randomize_brightness()
    for _ in range(10):
        pixels.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        pixels.show()
        time.sleep(0.1)

def color_chase():
    randomize_brightness()
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    for _ in range(10):
        for i in range(4):
            pixels.fill((0, 0, 0))
            pixels[i] = colors[i % len(colors)]
            pixels.show()
            time.sleep(0.1)

def slow_color_fade():
    randomize_brightness()
    for r in range(0, 256, 5):
        pixels.fill((r, 0, 255-r))
        pixels.show()
        time.sleep(0.1)
    for r in range(255, -1, -5):
        pixels.fill((r, 0, 255-r))
        pixels.show()
        time.sleep(0.1)

def rainbow_cycle():
    randomize_brightness()
    for j in range(255):
        for i in range(4):
            pixel_index = (i * 256 // 4) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(0.05)

# Helper function for rainbow colors
def wheel(pos):
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

# New LED effects

def twinkle():
    for _ in range(20):  # Twinkle 20 times
        randomize_brightness()
        pixels.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        #pixels[random.randint(0, 3)] = (255, 255, 255)
        pixels.show()
        time.sleep(1)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.1)

def pulse_all():
    randomize_brightness()
    for brightness in range(0, 255, 10):
        pixels.fill((brightness, 0, 255 - brightness))
        pixels.show()
        time.sleep(0.05)
    for brightness in range(255, -1, -10):
        pixels.fill((brightness, 0, 255 - brightness))
        pixels.show()
        time.sleep(0.05)

def theater_chase():
    randomize_brightness()
    color = (255, 0, 0)
    for _ in range(10):
        for i in range(4):
            pixels.fill((0, 0, 0))
            pixels[i] = color
            pixels.show()
            time.sleep(0.1)
            color = (0, 255, 0) if color == (255, 0, 0) else (255, 0, 0)

def wave_pattern():
    randomize_brightness()
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    for _ in range(10):
        for i in range(4):
            pixels.fill((0, 0, 0))
            pixels[i] = colors[(i + _ ) % len(colors)]
            pixels.show()
            time.sleep(0.15)

def confetti():
    randomize_brightness()
    for _ in range(20):  # Simulate 20 confetti drops
        pixels[random.randint(0, 3)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(0.1)
        pixels.fill((0, 0, 0))
        pixels.show()

def sparkle():
    randomize_brightness()
    for _ in range(50):
        index = random.randint(0, 3)
        pixels[index] = (255, 255, 255)
        pixels.show()
        time.sleep(0.05)
        pixels[index] = (0, 0, 0)


# Adding all effects to the list
effects = [
    classic_strobe,
    multi_color_flash,
    color_chase,
    slow_color_fade,
    rainbow_cycle,
    twinkle,
    pulse_all,
    theater_chase,
    wave_pattern,
    confetti,
    sparkle,
]

# Main loop: Randomly cycle through the effects
while True:
    effect = random.choice(effects)
    effect()
    time.sleep(0.1)
