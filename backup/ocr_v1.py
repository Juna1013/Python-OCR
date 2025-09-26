from PIL import Image
import pytesseract
from google.colab import drive
import os
import cv2
import numpy as np

print("必要なライブラリのインストールとTesseract OCRエンジンの導入が完了しました。")

print("\nGoogle Driveをマウントします。認証が必要です。")
drive.mount('/content/drive')
print("Google Driveのマウントが完了しました。")

# Google Drive内の画像ファイルのパスを指定
image_path = input("\nGoogle Drive内の画像ファイルのパスを入力してください (例: /content/drive/MyDrive/フォルダ名/ファイル名.png): ")

# 画像の読み込みと前処理
try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"ファイルが見つかりません: {image_path}")

    image = Image.open(image_path)
    print(f"\n画像ファイル '{os.path.basename(image_path)}' を読み込みました。")

    img_processed = image.convert('L') # グレースケール変換

    # OCRの実行とテキストの抽出
    extracted_text = pytesseract.image_to_string(img_processed, lang='jpn+eng')

    print("\n--- 抽出されたテキスト ---")
    if extracted_text.strip(): # テキストが空でないか確認
        print(extracted_text)
    else:
        print("テキストは抽出されませんでした。画像の品質を確認してください。")
    print("------------------------")

# 例外処理
except FileNotFoundError as e:
    print(f"エラー: {e}")
    print("指定されたパスにファイルが存在しないか、パスが間違っています。")
except ValueError as e:
    print(f"エラー: {e}")
    print("画像ファイルとして読み込めませんでした。有効な画像ファイル（例: .png, .jpg）を指定してください。")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
