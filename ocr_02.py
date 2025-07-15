from PIL import Image
import pytesseract
import cv2
import numpy as np

print("必要なライブラリのインポートが完了しました")

try:
    if not os.path.exists(image_path):

  image = Image.open(image_path)

except FileNotFoundError as e:

except ValueError as e:

except Exception as e:
