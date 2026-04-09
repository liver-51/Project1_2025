from gpiozero import LED, Button
from time import sleep, time
from random import uniform

led = LED(4)
left_btn = Button(14)
right_btn = Button(15)

left_name = input("左玩家名字：")
right_name = input("右玩家名字：")

score_left = 0
score_right = 0
off_time = 0

def on_press(btn):
    global score_left, score_right, off_time
    react = round(time() - off_time, 3)
    if btn.pin.number == 14:
        print(f"\n{left_name} 赢了！反应时间：{react}s")
        score_left += 1
    else:
        print(f"\n{right_name} 赢了！反应时间：{react}s")
        score_right += 1
    print(f"当前比分：{left_name} {score_left} - {score_right} {right_name}")
    sleep(1)
    start_round()

def start_round():
    global off_time
    print("\n准备就绪！灯灭后尽快按按钮！")
    led.on()
    sleep(uniform(3, 7))
    led.off()
    off_time = time()

left_btn.when_pressed = on_press
right_btn.when_pressed = on_press

start_round()
while True:
    sleep(0.1)
