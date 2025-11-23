# Генератор кодов Steam Guard

Скрипт для генерации кодов Steam Guard из maFile. Доступен как консольное приложение и телеграм бот.

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

### Консольный режим

1. Поместите ваши maFile в папку `maFiles/`

2. Запустите скрипт:

```bash
python steam_guard_code.py
```

В интерактивном режиме выберите файл из списка или введите имя файла.

Или укажите имя файла напрямую:

```bash
python steam_guard_code.py имя_файла.maFile
```

### Телеграм бот

1. Получите токен бота у [@BotFather](https://t.me/BotFather)

2. Установите токен через переменную окружения:
```bash
# Windows (PowerShell)
$env:BOT_TOKEN="your_bot_token_here"

# Linux/Mac
export BOT_TOKEN="your_bot_token_here"
```

Или измените `BOT_TOKEN` в файле `bot.py`

3. Запустите бота:
```bash
python bot.py
```

4. Отправьте боту ник аккаунта Steam (значение `account_name` из maFile), и бот вернет код Steam Guard.

### Запуск в Docker

1. Убедитесь, что у вас установлены Docker и Docker Compose

2. Создайте файл `.env` в корне проекта:
```bash
BOT_TOKEN=ваш_токен_здесь
```

3. Поместите ваши maFile в папку `maFiles/`

4. Запустите контейнер:
```bash
docker-compose up -d
```

5. Проверьте статус:
```bash
docker-compose ps
```

6. Просмотр логов:
```bash
docker-compose logs -f
```

7. Остановка:
```bash
docker-compose down
```

**Особенности:**
- Контейнер автоматически перезапускается при перезагрузке сервера (`restart: unless-stopped`)
- Папка `maFiles/` и файл `.env` монтируются как volumes, поэтому изменения применяются без пересборки образа
- Все зависимости устанавливаются автоматически при сборке образа

## Формат maFile

maFile должен быть JSON файлом со следующей структурой:

```json
{
  "account_name": "ваш_ник_steam",
  "shared_secret": "ваш_shared_secret_здесь",
  "identity_secret": "ваш_identity_secret_здесь"
}
```

**Важно**: Для работы телеграм бота в maFile должен быть ключ `account_name` с ником аккаунта Steam.

## Структура проекта

```
steam-guard-generator/
├── maFiles/          # Поместите сюда ваши maFile (файлы с расширением .maFile)
├── steam_guard_code.py  # Основной модуль для генерации кодов
├── bot.py            # Телеграм бот
├── requirements.txt
├── Dockerfile         # Конфигурация Docker образа
├── docker-compose.yml # Конфигурация Docker Compose
├── .dockerignore     # Исключения для Docker
└── README.md
```

## Важно

- **Безопасность**: Никогда не делитесь своим maFile или shared_secret с другими!
- maFile обычно получается при настройке мобильного аутентификатора Steam
- Коды обновляются каждые 30 секунд
- Все maFile должны находиться в папке `maFiles/`

## Примечания

- Для генерации кодов используются стандартные библиотеки Python (hmac, hashlib, base64)
- Для телеграм бота используется библиотека `aiogram`
- shared_secret можно получить только при настройке мобильного аутентификатора
- Телеграм бот ищет maFile по значению `account_name` из файла

