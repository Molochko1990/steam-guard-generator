#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для генерации кодов Steam Guard из maFile
"""

import json
import sys
import base64
import hmac
import hashlib
import time
from pathlib import Path


# Путь к папке с maFiles
MAFILES_DIR = Path(__file__).parent / "maFiles"

# Специальный алфавит Steam Guard (без похожих символов: 0, 1, I, L, O)
STEAM_ALPHABET = "23456789BCDFGHJKMNPQRTVWXY"


def generate_code_from_shared_secret(shared_secret: str) -> str:
    """Генерирует код Steam Guard из shared_secret"""
    # Декодируем shared_secret из base64
    secret_bytes = base64.b64decode(shared_secret)
    
    # Получаем текущее время в виде количества 30-секундных интервалов
    timestamp = int(time.time())
    time_counter = timestamp // 30
    
    # Конвертируем time_counter в байты (big-endian, 8 байт)
    time_bytes = time_counter.to_bytes(8, byteorder='big')
    
    # Вычисляем HMAC-SHA1
    hmac_digest = hmac.new(secret_bytes, time_bytes, hashlib.sha1).digest()
    
    # Берем последний байт для определения начальной позиции
    start = hmac_digest[19] & 0x0F
    
    # Извлекаем 4 байта начиная с позиции start
    code_bytes = hmac_digest[start:start+4]
    
    # Конвертируем в число
    code_int = int.from_bytes(code_bytes, byteorder='big') & 0x7FFFFFFF
    
    # Генерируем код из 5 символов используя алфавит Steam
    code = ""
    for _ in range(5):
        code += STEAM_ALPHABET[code_int % len(STEAM_ALPHABET)]
        code_int //= len(STEAM_ALPHABET)
    
    return code


def load_mafile(filename: str) -> dict:
    """Загружает maFile из папки maFiles"""
    filepath = MAFILES_DIR / filename
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_steam_guard_code(filename: str) -> str:
    """Извлекает shared_secret из maFile и генерирует код"""
    mafile_data = load_mafile(filename)
    shared_secret = mafile_data['shared_secret']
    return generate_code_from_shared_secret(shared_secret)


def find_mafile_by_account_name(account_name: str) -> str:
    """Находит maFile по account_name и возвращает код Steam Guard"""
    if not MAFILES_DIR.exists():
        raise FileNotFoundError("Папка maFiles не найдена")
    
    # Ищем файл с нужным account_name
    for mafile_path in MAFILES_DIR.glob("*.maFile"):
        try:
            mafile_data = load_mafile(mafile_path.name)
            if mafile_data.get('account_name') == account_name:
                shared_secret = mafile_data['shared_secret']
                return generate_code_from_shared_secret(shared_secret)
        except Exception:
            continue
    
    raise ValueError(f"Аккаунт с именем '{account_name}' не найден")


def list_mafiles() -> list[str]:
    """Возвращает список всех maFile файлов в папке maFiles"""
    if not MAFILES_DIR.exists():
        return []
    
    return sorted([f.name for f in MAFILES_DIR.glob("*.maFile")])


def main():
    """Основная функция"""
    print("=" * 50)
    print("Генератор кодов Steam Guard")
    print("=" * 50)
    print()
    
    # Получаем список доступных maFiles
    mafiles = list_mafiles()
    
    if len(sys.argv) >= 2:
        # Режим с аргументом командной строки
        filename = sys.argv[1]
        if not filename.endswith('.maFile'):
            filename += '.maFile'
    else:
        # Интерактивный режим
        if not mafiles:
            print("В папке maFiles нет файлов!")
            print(f"Поместите maFile (с расширением .maFile) в папку: {MAFILES_DIR}")
            return
        
        print("Доступные maFiles:")
        for i, mafile in enumerate(mafiles, 1):
            print(f"  {i}. {mafile}")
        print()
        
        choice = input("Введите номер файла или имя файла: ").strip()
        
        # Проверяем, это номер или имя
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(mafiles):
                filename = mafiles[idx]
            else:
                print("Неверный номер!")
                return
        else:
            filename = choice
            if not filename.endswith('.maFile'):
                filename += '.maFile'
    
    # Генерируем код
    try:
        code = get_steam_guard_code(filename)
        print(f"\n✓ Код Steam Guard: {code}")
    except FileNotFoundError:
        print(f"\n✗ Файл {filename} не найден в папке maFiles")
    except Exception as e:
        print(f"\n✗ Ошибка: {e}")


if __name__ == "__main__":
    main()

