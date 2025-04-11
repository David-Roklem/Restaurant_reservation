# Обзор проекта
REST API для бронирования столиков в ресторане. Сервис позволяет создавать, просматривать и удалять брони, а также управлять столиками и временными слотами. Стек: FastAPI, PostgreSQL, SQLalchemy, Docker

## Начало работы
Склонируйте данный репозиторий командой:
```
https://github.com/David-Roklem/Restaurant_reservation
```

### Зависимости
Зависимости проекта описаны в файлах pyproject.toml и requirements.txt.

### Docker
По примеру переменных окружения, указанных в файле .env.example, видоизмените их по необходимости

Чтобы запустить проект на локальной машине, вам необходимо (находясь в корне проекта) выполнить следующие шаги:
1) поднять контейнеры командой:
```
docker compose up -d
```
2) Применить миграции к базе данных:
```
alembic upgrade head
```

### Запуск
В браузере перейдите по адресу http://127.0.0.1/docs, чтобы попасть в Swagger UI для взаимодействия с API
