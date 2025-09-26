import cv2
import easyocr
import pytesseract
import numpy as np

# --- 設定 ---
image_path = "sample.webp"          # 板書画像ファイル
output_md = "lecture_output.md"     # 出力Markdownファイル

# --- OCR初期化 ---
reader = easyocr.Reader(['ja', 'en'])  # 日本語＋英語

# --- 画像読み込み ---
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError(f"{image_path} が見つかりません")

# --- 前処理: コントラスト強調 + 適応二値化 + ノイズ除去 ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV, 15, 8
)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# --- OCR実行 (EasyOCR) ---
result_easy = reader.readtext(thresh)

# --- OCR補完 (Tesseract) ---
# 数式や特殊記号の補完用
tess_config = "--psm 6 -l jpn+eng"
text_tess = pytesseract.image_to_string(thresh, config=tess_config)

# --- 左上→右下順にソート (EasyOCR結果) ---
def sort_key(item):
    bbox = item[0]
    y_avg = sum([pt[1] for pt in bbox]) / 4
    x_avg = sum([pt[0] for pt in bbox]) / 4
    return (y_avg, x_avg)

result_sorted = sorted(result_easy, key=sort_key)

# --- Markdown形式で整形 ---
with open(output_md, "w", encoding="utf-8") as f:
    f.write("# 電磁気学講義 OCR 文字起こし\n\n")
    f.write("```\n")  # コードブロック開始

    # EasyOCRで抽出した文字を行ごとに出力
    for item in result_sorted:
        f.write(item[1] + "\n")

    # Tesseractで補完した文字列を追記（重複を除く場合は工夫が必要）
    f.write("\n# Tesseract補完:\n")
    f.write(text_tess.strip() + "\n")

    f.write("```\n")  # コードブロック終了

print(f"OCR完了。結果は {output_md} に保存されました。")
