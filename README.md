# API коллекции мемов

Этот проект представляет собой веб-приложение, разработанное на Python с использованием FastAPI, которое предоставляет API для управления коллекцией мемов. Он состоит из двух сервисов: публичного API-сервиса для бизнес-логики и медиа-сервиса для обработки медиафайлов с использованием S3-совместимого хранилища (MinIO).

## Функциональность

- `GET /memes`: Получение списка всех мемов (с пагинацией)
- `GET /memes/{id}`: Получение конкретного мема по его ID
- `POST /memes`: Добавление нового мема (с изображением и текстом)
- `PUT /memes/{id}`: Обновление существующего мема
- `DELETE /memes/{id}`: Удаление мема

## Требования

- Docker
- Docker Compose

## Настройка локальной среды разработки

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/vlefr5v1l/task_mad_soft.git
   ```

2. Соберите и запустите сервисы:

   ```bash
   docker-compose up --build
   ```

3. Сервисы будут доступны по следующим адресам:
   - Публичный API: [http://localhost:8000](http://localhost:8000)
   - Медиа-сервис: [http://localhost:8001](http://localhost:8001)
   - MinIO: [http://localhost:9000](http://localhost:9000)

4. Документация API (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)



## Структура проекта

- `app/`: Содержит основное FastAPI-приложение с бизнес-логикой
- `media_service/`: Содержит сервис для обработки медиафайлов
- `tests/`: Содержит модульные тесты
- `docker-compose.yml`: Определяет и запускает многоконтейнерное Docker-приложение

## Используемые технологии

- FastAPI
- SQLAlchemy
- PostgreSQL
- MinIO (S3-совместимое хранилище)
- Docker
