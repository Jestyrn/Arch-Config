#!/usr/bin/env python3
import subprocess
import json
import sys
import urllib.parse

CITY = "Саратов"

def get_weather():
    # Кодируем город для URL
    encoded_city = urllib.parse.quote(CITY)
    url = f"https://wttr.in/{encoded_city}?format=%t+%C"

    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", url],
            capture_output=True,
            text=True
        )
        if result.returncode != 0 or "error" in result.stdout.lower():
            raise RuntimeError("Failed to fetch weather")

        raw = result.stdout.strip()
        if not raw or "Unknown location" in raw:
            raise RuntimeError("Unknown location")

        # Пример: "+23°C partly cloudy"
        parts = raw.split(" ", 1)
        temp = parts[0]  # "+23°C"
        condition = parts[1] if len(parts) > 1 else ""

        # Иконка по условию (упрощённо)
        icon = ""  # солнце по умолчанию
        if "rain" in condition.lower():
            icon = ""
        elif "cloud" in condition.lower():
            icon = ""
        elif "snow" in condition.lower():
            icon = ""

        text = f"{icon}{temp}"
        tooltip = f"Weather in {CITY}\n{raw}"

        return text, tooltip

    except Exception as e:
        return "⚠", f"Weather error: {str(e)}"

def main():
    text, tooltip = get_weather()
    print(json.dumps({
        "text": text,
        "tooltip": tooltip,
        "class": "weather"
    }))

if __name__ == "__main__":
    main()