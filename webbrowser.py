import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while(break_count < total_breaks):
    time.sleep(1)
    webbrowser.open("https://youtu.be/BvP4RIqSbiw?t=1m25s")
    break_count = break_count + 1
