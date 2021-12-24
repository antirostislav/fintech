# main

Правила использования репозитория:

1. Названия и описания коммитов на русском, начинаются с большой буквы. Пишем в настоящем времени без точки в конце.
   Пример: удаление "название файла" за ненадобностью
2. Названия файлов на английском, документация кода на русском

# Установка и запуск

## Установка

1. Клонировать репозиторий

```
git clone https://github.com/antirostislav/fintech.git
git checkout dev
```

2. Скачать и установить [Docker](https://www.docker.com/products/docker-desktop)
3. Запустить установку проекта

```
cd <project_directory>
docker-compose -f docker-compose.yml up --build
```

## Запуск

1. Запустить проект

```
cd <project_directory>
docker-compose -f docker-compose.yml up
```