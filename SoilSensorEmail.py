import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from datetime import datetime

# ========== 1. 引脚&邮箱配置 ==========
SOIL_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_PIN, GPIO.IN)

sender = "360818543@qq.com"
auth_code = "bcsicsyvqhinbgjc"# 替换为你的授权码
receiver = "xyhdmn@qq.com"
smtp_server = "smtp.qq.com"
smtp_port = 465

# ========== 2. 邮件发送函数（已修正） ==========
def send_email(alert_msg):
    msg = MIMEText(alert_msg, 'plain', 'utf-8')
    # 修正 From 头格式
    msg['From'] = formataddr(("盆栽养护提醒", sender))
    msg['To'] = receiver
    msg['Subject'] = Header("🌱 植物土壤湿度每日状态报告", 'utf-8')

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender, auth_code)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    print(f"{datetime.now()} 邮件发送完成")

# ========== 3. 快速演示：直接执行4次检测 ==========
try:
    print("植物湿度监控+邮件上报系统启动（快速演示模式）")
    # 4次检测模拟
    times = ["08:00", "12:00", "18:00", "22:00"]
    for t in times:
        now = datetime.now()
        soil_state = GPIO.input(SOIL_PIN)
        
        if soil_state == 0:
            content = f"{now.strftime('%Y-%m-%d')} {t}\n土壤状态：湿润\n无需浇水 Water NOT needed"
        else:
            content = f"{now.strftime('%Y-%m-%d')} {t}\n⚠️ 土壤干燥缺水\n请及时给你的植物浇水 Please water your plant"
        
        print(f"模拟 {t} 检测…")
        send_email(content)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\n程序安全退出")
