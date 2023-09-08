import pyautogui
import time

COLOR = (83, 83, 83)

DARK_COLOR = (172, 172, 172)


def take_screenshot():
    screenshot = pyautogui.screenshot(region=(300, 400, 100, 100))
    return screenshot


def is_obstacle_ahead(screenshot):
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == COLOR or screenshot.getpixel((x, y)) == DARK_COLOR:
                return True
    return False


time.sleep(5)
while True:
    screen = take_screenshot()
    if is_obstacle_ahead(screen):
        pyautogui.keyDown('space')
        time.sleep(0.25)
        pyautogui.keyUp('space')
