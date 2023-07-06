# Extract text from pdf image
#### Multilanguage README Pattern
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Almaz2312/extract_pdf/blob/master/README.en.md)
[![ru](https://img.shields.io/badge/lang-ru-green.svg)](https://github.com/Almaz2312/extract_pdf/blob/master/README.md)

## Начнём


### ◦ Виртуальное окружение

Создайте виртуальное окружение. 

```commandline
python -m venv venv
```

> Здесь используется утилита "venv" для создания виртуального окружения, но вы в праве использовать любой другой инструмент.


### ◦ Переменные окружения

В данном проекте вам необходимо использовать переменные окружения. Это данные, которые вы записываете в файл .env, чтобы скрыть информацию от ненужных глаз. 

Скопируйте содержимое .env.example и подставьте нужные значения.

```commandline
cp .env.example .env
```

## База
В данном проекте все файлы сохраняются в текстовом файле


## Установка

Для начала вам нужно установить двигатель Tesseract OCR. Его можно установить следуя инструкциям по ссылке: https://tesseract-ocr.github.io/tessdoc/Installation.html

Проверить успешную установку можно в терминале

```commandline
C:\Program Files\Tesseract-OCR\tesseract.exe --version
```

Если вы на windows, то вам также нужно будет скачать poppler. \
Рекомендованная версия: https://github.com/oschwartz10612/poppler-windows/releases/


### Зависимости

После создания виртуального окружения вам необходимо установить зависимости.
Вы можете это сделать посредством poetry или же напрямую через pip install.
Но для начала желательно обновить пакет пип

```commandline
python -m pip install --upgrade pip
```

Затем вы можете использовать один из двух вариантов установки зависимостей

### pip

```commandline
python -m pip install -r requirements.txt
```

### poetry

```commandline
python -m pip install poetry
poetry install
```

### Запуск программы
Запускается проект в main.py

```commandline
python main.py
```
