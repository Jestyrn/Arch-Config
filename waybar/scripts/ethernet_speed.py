#!/usr/bin/env python3
import time
import json
import sys

# === НАСТРОЙКА: замени на свой интерфейс! ===
INTERFACE = "wlan0"  # ← ОБЯЗАТЕЛЬНО ЗАМЕНИ!
# ============================================

def read_bytes():
    with open("/proc/net/dev", "r") as f:
        for line in f:
            if INTERFACE in line:
                parts = line.split()
                rx = int(parts[1])   # received bytes
                tx = int(parts[9])   # transmitted bytes
                return rx, tx
    raise RuntimeError(f"Interface '{INTERFACE}' not found in /proc/net/dev")

def main():
    try:
        rx1, tx1 = read_bytes()
        time.sleep(1)
        rx2, tx2 = read_bytes()

        # Скорость в Мбит/с
        rx_speed = (rx2 - rx1) * 8 / 1_000_000
        tx_speed = (tx2 - tx1) * 8 / 1_000_000

        # Защита от отрицательных значений (при переполнении счётчика)
        rx_speed = max(0.0, round(rx_speed, 1))
        tx_speed = max(0.0, round(tx_speed, 1))

        parts = ["🌐"]
        if rx_speed > 0.0:
            parts.append(f"↓{rx_speed}")
        if tx_speed > 0.0:
            parts.append(f"↑{tx_speed}")
        text = " ".join(parts)
        tooltip = f"Download: {rx_speed} Mbps\nUpload: {tx_speed} Mbps\nInterface: {INTERFACE}"

        print(json.dumps({
            "text": text,
            "tooltip": tooltip,
            "class": "net"
        }))

    except Exception as e:
        print(json.dumps({
            "text": "⚠",
            "tooltip": f"Net error: {str(e)}",
            "class": "error"
        }))
        sys.exit(1)

if __name__ == "__main__":
    main()