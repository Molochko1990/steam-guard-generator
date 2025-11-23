# Инструкция по загрузке проекта на GitHub

## Шаг 1: Установите Git (если еще не установлен)

Скачайте и установите Git с официального сайта: https://git-scm.com/downloads

## Шаг 2: Создайте репозиторий на GitHub

1. Зайдите на https://github.com
2. Нажмите кнопку "+" в правом верхнем углу
3. Выберите "New repository"
4. Введите название репозитория (например: `steam-guard-generator`)
5. **НЕ** ставьте галочки на "Initialize with README", "Add .gitignore" или "Choose a license"
6. Нажмите "Create repository"

## Шаг 3: Инициализируйте Git в локальной папке

Откройте терминал (PowerShell или Command Prompt) в папке проекта и выполните:

```bash
# Перейдите в папку проекта
cd путь\к\steam-guard-generator

# Инициализируйте git репозиторий
git init

# Добавьте все файлы (кроме тех, что в .gitignore)
git add .

# Сделайте первый коммит
git commit -m "Initial commit: Steam Guard code generator with Telegram bot"
```

## Шаг 4: Подключите удаленный репозиторий

После создания репозитория на GitHub, скопируйте URL репозитория (например: `https://github.com/ваш_username/steam-guard-generator.git`)

Выполните:

```bash
# Добавьте удаленный репозиторий (замените URL на ваш)
git remote add origin https://github.com/ваш_username/steam-guard-generator.git

# Переименуйте ветку в main (если нужно)
git branch -M main

# Загрузите код на GitHub
git push -u origin main
```

## Шаг 5: Проверка

Зайдите на GitHub и убедитесь, что все файлы загружены.

## Важные замечания:

⚠️ **Убедитесь, что файл `.env` НЕ попал в репозиторий!** Он должен быть в `.gitignore`

⚠️ **Убедитесь, что файлы из папки `maFiles/` НЕ попали в репозиторий!** Они должны быть в `.gitignore`

## Если нужно обновить код позже:

```bash
# Добавьте измененные файлы
git add .

# Сделайте коммит
git commit -m "Описание изменений"

# Загрузите на GitHub
git push
```

## Если возникли проблемы:

1. **Ошибка авторизации**: GitHub больше не поддерживает пароли. Нужно использовать Personal Access Token:
   - Зайдите в Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Создайте новый токен с правами `repo`
   - Используйте токен вместо пароля при `git push`

2. **Проверьте, что файлы не игнорируются**:
   ```bash
   git status
   ```

3. **Если нужно удалить файл из git, но оставить локально**:
   ```bash
   git rm --cached имя_файла
   ```

