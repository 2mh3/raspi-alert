from flask import Flask, request, jsonify
from gpiozero import LED
from time import sleep

app = Flask(__name__)
led = LED(21)  # GPIO 21を使用

@app.route('/blink', methods=['POST'])
def blink_led():
    data = request.get_json()
    blink_count = data.get("count", 3)  # デフォルト3回点滅
    blink_speed = data.get("speed", 0.5)  # デフォルト0.5秒間隔
    
    for _ in range(blink_count):
        led.on()
        sleep(blink_speed)
        led.off()
        sleep(blink_speed)
    
    return jsonify({"message": f"LED blinked {blink_count} times"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
