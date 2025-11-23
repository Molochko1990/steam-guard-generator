# Генератор кодов Steam Guard

Телеграм бот для генерации кодов Steam Guard из maFile.

## Развертывание

Подробная инструкция по развертыванию на сервере находится в файле [DEPLOY.md](DEPLOY.md)

**Быстрый старт:**

```bash
# Клонирование репозитория
git clone https://github.com/Molochko1990/steam-guard-generator.git
cd steam-guard-generator

# Создание .env файла с токеном бота
echo "BOT_TOKEN=ваш_токен_здесь" > .env

# Добавление maFiles в папку maFiles/

# Запуск в Docker
docker-compose up -d --build
```

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

## Как использовать

Отправьте боту ник аккаунта Steam (значение `account_name` из maFile), и бот вернет код Steam Guard.

## Важно

- **Безопасность**: Никогда не делитесь своим maFile или shared_secret с другими!
- maFile обычно получается при настройке мобильного аутентификатора Steam
- Коды обновляются каждые 30 секунд
- Все maFile должны находиться в папке `maFiles/`

## Управление контейнером

### Остановка контейнера
```bash
docker-compose down
```

### Перезапуск контейнера
```bash
docker-compose restart
```

### Обновление кода из репозитория
```bash
# Получить последние изменения
git pull

# Пересобрать и перезапустить контейнер
docker-compose up -d --build
```

### Просмотр логов
```bash
docker-compose logs -f
```

## Примечания

- Для генерации кодов используются стандартные библиотеки Python (hmac, hashlib, base64)
- Для телеграм бота используется библиотека `aiogram`
- shared_secret можно получить только при настройке мобильного аутентификатора
- Телеграм бот ищет maFile по значению `account_name` из файла

