#!/bin/sh

# Название окна или класс приложения (можно уточнить через `hyprctl clients`)
APP_NAME="Telegram"
EXEC_CMD="Telegram"

# Проверяем, запущено ли приложение
if hyprctl clients -j | jq -e ".[] | select(.class == \"$APP_NAME\")" > /dev/null 2>&1; then
    # Если запущено — фокусируем его
    hyprctl dispatch focuswindow "^$APP_NAME$"
    echo '{"text": "", "tooltip": "Telegram — click to focus", "class": "running"}'
else
    # Если не запущено — просто показываем иконку (запуск по клику сделаем в on-click)
    echo '{"text": "", "tooltip": "Telegram — click to launch", "class": "not-running"}'
fi