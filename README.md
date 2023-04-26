# api_final_yatube 

Учебный проект 9 спринта.

# Описание  api_final_yatube 

Это полноценный API-сервис для Yatube.

## Как запустить локально

 1. Клонировать репозиторий:

    ```python
    git clone https://github.com/Evkasonka/api_final_yatube 
    ```

 2. Перейти в папку с проектом:

    ```python
    cd api_final_yatube/
    ```

 3. Установите виртуальное окружение 
    ```python
    python -m venv venv
    ```

 4. Активируйте виртуальное окружение 
    ```python
    # для OS Lunix и MacOS
    source venv/bin/activate
    # для OS Windows
    source venv/Scripts/activate
    ```

 5. Установите зависимости из файла requirements.txt 
    ```python
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
 6. Выполнить миграции:
    ```python
    python3 manage.py migrate
    ```
 7. Запустить проект локально:

    ```python
    # для OS Lunix и MacOS
    python homework_bot.py
    # для OS Windows
    python3 homework_bot.py
    ```