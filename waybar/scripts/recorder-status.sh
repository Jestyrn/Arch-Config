#!/bin/sh

# Проверяем, записывает ли wf-recorder
if pgrep -x "wf-recorder" > /dev/null; then
    # Получаем время работы процесса (в секундах)
    PID=$(pgrep -x "wf-recorder")
    ELAPSED=$(ps -o etimes= -p "$PID" 2>/dev/null | tr -d ' ')
    if [ -z "$ELAPSED" ]; then
        ELAPSED=0
    fi

    # Форматируем в ЧЧ:ММ:СС
    HOURS=$((ELAPSED / 3600))
    MINUTES=$(((ELAPSED % 3600) / 60))
    SECONDS=$((ELAPSED % 60))
    TIME=$(printf "%02d:%02d:%02d" $HOURS $MINUTES $SECONDS)

    echo "{\"text\": \" $TIME\", \"tooltip\": \"Recording... Click to stop\", \"class\": \"recording\"}"
else
    echo "{\"text\": \"\", \"tooltip\": \"Click to start recording\", \"class\": \"inactive\"}"
fi