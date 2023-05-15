import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python3", "/home/rishabh.tripathi/hpa_alert/HPAalert.py"], stdout=output);
