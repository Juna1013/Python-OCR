from PIL import Image
import pytesseract
import cv2
import numpy as np

print("必要なライブラリのインポートが完了しました")

image_path = input("\n画像ファイルのパスを入力してください（例：/home/ユーザー名/image.jpg）：")

try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"ファイルが見つかりません：{image_path}")

    image = Image.open(image_path)
    print(f"\n画像ファイル '{os.path.basename(image_path)}' を読み込みました")

    image_processed = image.convert('L')

    extracted_text = pytessract.image_to_string(img_processed, lang='jpn+eng')

    print("\n--- 抽出されたテキスト ---")
    if extracted_text_strip()
        print(extracted_text)
    else:
        print("テキストは抽出されませんでした、画像の品質を確認してください")
    print("--------------------")

except FileNotFoundError as e:
    print(f"エラー： {e}")
    print("指定されたパスにファイルが存在しないか、パスが間違っています")
except ValueError as e:
    print(f"エラー： {e}")
    print("画像ファイルとして読み込めませんでした、有効なファイルを指定してください")
except Exception as e:
    print(f"予期せぬエラーが発生しました： {e}")
