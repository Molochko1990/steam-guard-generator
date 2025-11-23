#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Телеграм бот для генерации кодов Steam Guard
"""

import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from steam_guard_code import find_mafile_by_account_name

# Загружаем переменные из .env файла
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота (получите у @BotFather)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ID разрешенного пользователя
ALLOWED_USER_ID = os.getenv("ALLOWED_USER", "")

# Инициализация диспетчера
dp = Dispatcher()


def check_user_id(message: types.Message) -> bool:
    """Проверяет, разрешен ли пользователь"""
    return message.from_user.id == ALLOWED_USER_ID


@dp.message()
async def process_account_name(message: types.Message):
    """Обработчик сообщений с ником аккаунта"""
    if not check_user_id(message):
        await message.answer("❌ Доступ запрещен")
        return
    
    account_name = message.text.strip()
    
    if not account_name:
        await message.answer("❌ Пожалуйста, отправь ник аккаунта Steam")
        return
    
    try:
        # Генерируем код для аккаунта
        code = find_mafile_by_account_name(account_name)
        await message.answer(
            f"✅ Код Steam Guard для аккаунта <b>{account_name}</b>:\n\n"
            f"🔐 <code>{code}</code>",
            parse_mode="HTML"
        )
    except ValueError as e:
        await message.answer(f"❌ {str(e)}")
    except Exception as e:
        logger.error(f"Ошибка при генерации кода: {e}", exc_info=True)
        await message.answer("❌ Произошла ошибка при генерации кода. Попробуй еще раз.")


async def main():
    """Запуск бота"""
    if not BOT_TOKEN:
        print("❌ Ошибка: BOT_TOKEN не установлен!")
        print("Установите токен в файле .env или через переменную окружения")
        print("Формат .env файла: BOT_TOKEN=ваш_токен_здесь")
        print("Создайте файл .env в папке с bot.py с содержимым: BOT_TOKEN=ваш_токен")
        return
    
    # Проверяем формат токена (должен быть примерно 46 символов и содержать :)
    if ':' not in BOT_TOKEN or len(BOT_TOKEN) < 40:
        print("❌ Ошибка: Токен имеет неверный формат!")
        print("Токен должен быть в формате: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz")
        print(f"Текущий токен (первые 10 символов): {BOT_TOKEN[:10]}...")
        return
    
    # Инициализация бота
    try:
        bot = Bot(token=BOT_TOKEN)
        logger.info("Бот запущен...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Ошибка при инициализации бота: {e}")
        print("Проверьте правильность токена в файле .env")


if __name__ == "__main__":
    asyncio.run(main())

