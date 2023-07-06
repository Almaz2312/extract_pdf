# Extract text from pdf image

#### Multilanguage README Pattern
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Almaz2312/extract_pdf/blob/master/README.en.md)
[![ru](https://img.shields.io/badge/lang-ru-green.svg)](https://github.com/Almaz2312/extract_pdf/blob/master/README.md)

## Get started


### ◦ Virtual environment

Create a virtual environment. 

```commandline
python -m venv venv
```

> Here we use utility called "venv" for creating a virtual environment, but you can use which ever you prefer.


### ◦ Environment variables

In this project you will have to use environment variables. Those are variables that needs to be hidden in .env file

Copy .env.examples content and fill in accordingly

```commandline
cp .env.example .env
```

## Database

Current project save everything in a text file, thus there is no need to introduce database

## Installation

First, you need to install Tesseract OCR engine. you can install it following insturctions in this link:  https://tesseract-ocr.github.io/tessdoc/Installation.html

You can check successful installation by running this command in terminal

```commandline
C:\Program Files\Tesseract-OCR\tesseract.exe --version
```

If you are on a windows, then you will have to download poppler. \
Reccomended version: https://github.com/oschwartz10612/poppler-windows/releases/

### Dependencies
After creating virtual environment you would need to install dependencies.
You can do it with poetry or directly using pip install.
But first I would suggest upgrading your pip package.

```commandline
python -m pip install --upgrade pip
```

Afterwards you can install dependencies with one of the two methods.

### pip

```commandline
python -m pip install -r requirements.txt
```

### poetry

```commandline
python -m pip install poetry
poetry install
```

### Launching program
Program is launched in main.py

```commandline
python main.py
```
