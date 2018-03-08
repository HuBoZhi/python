#-*- coding:utf-8 -*-
import os,time
Time = {
        "hour": 22,
        "minute":50
    }
u_time = Time
u_h = int(u_time["hour"])
u_m = int(u_time["minute"])
w_time = time.strftime('%H:%M:%S')
w_h = int(w_time[0:2])
w_m = int(w_time[3:5])
tt = (u_h + (u_m / 60.0) - w_h - (w_m / 60.0)) * 3600
os.system('shutdown -s -t %d' % tt)