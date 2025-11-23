FROM python:3.11-slim

WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY bot.py steam_guard_code.py ./

# Создаем папку для maFiles (будет монтироваться как volume)
RUN mkdir -p maFiles

# Запускаем бота
CMD ["python", "bot.py"]


