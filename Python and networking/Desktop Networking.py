import psutil
import time
import os
import pandas as pd

update_delay = 15

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

io = psutil.net_io_counters(pernic=True)

while True:
    # Sleep for the update delay
    time.sleep(update_delay)

    # Get updated network IO stats
    io_1 = psutil.net_io_counters(pernic=True)
    data = []
    
    # Iterate through each network interface
    for iface, iface_io in io.items():  
        upload_speed = io_1[iface].bytes_sent - iface_io.bytes_sent
        download_speed = io_1[iface].bytes_recv - iface_io.bytes_recv
        
        data.append({
            "iface": iface,
            "Download": get_size(io_1[iface].bytes_recv),
            "Upload": get_size(io_1[iface].bytes_sent),
            "Upload Speed": f"{get_size(upload_speed / update_delay)}/s",
            "Download Speed": f"{get_size(download_speed / update_delay)}/s",
        })
    
    io = io_1  

    df = pd.DataFrame(data)
    df.sort_values("Download", inplace=True, ascending=False)

    os.system("cls") if "nt" in os.name else os.system("clear")

    print(df.to_string())
