from pathlib import Path
import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from decouple import config


file_path = Path(__file__).resolve().parent / config("file_path")
poppler = Path(__file__).resolve().parent / config("poppler")
tesseract_path = Path(config("tesseract_path"))


pytesseract.pytesseract.tesseract_cmd = tesseract_path

images = convert_from_path(file_path, poppler_path=poppler)


def extract_pdf_image():
    for count, img in enumerate(images, start=1):
        img_name = f"page_{count}.png"
        img.save("images/" + img_name, "PNG")


def extract_text():
    png_files = [f for f in os.listdir(".") if f.endswith(".png")]
    for count, png_file in enumerate(png_files, start=1):
        extracted_text = pytesseract.image_to_string(Image.open(png_file))
        with open(f"exctracted_texts/page_{count}.txt", "w", encoding="utf-8") as file:
            file.write(extracted_text)
        # print(extracted_text)


def main():
    extract_pdf_image()
    extract_text()


if __name__ == "__main__":
    main()
