import webbrowser
import time 

break_waiting_time = 3
counting_down = 0

print("this is the current time" + time.ctime())
while counting_down  < break_waiting_time:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=UK3ivQxxNNk")
    break_waiting_time += 1