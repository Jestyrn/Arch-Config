#!/bin/sh

# === Настройки ===
OUTPUT_DIR="$HOME/Videos/Screenshots"
FILE_NAME="screen_recording_$(date '+%Y-%m-%d_%H-%M-%S').mp4"
FULL_PATH="$OUTPUT_DIR/$FILE_NAME"
AUDIO_MONITOR=$(pactl get-default-sink).monitor

if [ -z "$AUDIO_MONITOR" ] || ! pactl list sources short | grep -q "$AUDIO_MONITOR"; then
    AUDIO_MONITOR=$(pactl list sources short | grep ".monitor" | head -n1 | awk '{print $2}')
fi

# Создаём папку на всякий случай
mkdir -p "$OUTPUT_DIR"

if pgrep -x "wf-recorder" > /dev/null; then
    # Останавливаем запись
    pkill -x wf-recorder
    # Опционально: уведомление об остановке
    # notify-send "Recording stopped" "$FULL_PATH"
else
    # Запускаем запись
     wf-recorder -f "$FULL_PATH" -a "$AUDIO_MONITOR" &
fi