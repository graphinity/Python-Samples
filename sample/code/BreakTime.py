'''
Created on Apr 18, 2016

@author: karya
'''
import webbrowser
import time

total_breaks = 3
break_count = 0

print("Started waiting at :" + time.ctime())
while (break_count < total_breaks):
    time.sleep(3)
    webbrowser.open_new("https://www.youtube.com/watch?v=NTHz9ephYTw")
    break_count = break_count + 1
    
print("End program at :" + time.ctime())