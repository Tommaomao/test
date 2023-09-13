import time

def focus_timer(duration_minutes):
    duration_seconds = duration_minutes * 60
    print(f"专注倒计时 {duration_minutes} 分钟...")
    time.sleep(duration_seconds)
    print("专注时间结束！")

if __name__ == "__main__":
    try:
        minutes = int(input("请输入专注时间（分钟）："))
        focus_timer(minutes)
    except ValueError:
        print("请输入有效的分钟数。")
