import json
import subprocess
output=subprocess.getoutput("kubectl get hpa | awk '{print $1}'")
hpa_output=subprocess.getoutput("kubectl get hpa | awk '{print $3}' | cut -d/ -f1")
max_pod=subprocess.getoutput("kubectl get hpa | awk '{print $5}'")
replica=subprocess.getoutput("kubectl get hpa | awk '{print $6}'")
A=output.split()
B=hpa_output.split()
hpa_services=B[1:len(B)]
services_names=A[1:len(A)]
hpa=[]
flag=0
#file_output=''
max_pod , replica =max_pod.split() , replica.split()
max_pod ,replica =max_pod[1:len(B)] , replica[1:len(B)]
max_pod=[int(i) for i in max_pod]
replica=[int(i) for i in replica]
with open('/home/rishabh.tripathi/hpa_alert/config.json', 'r') as f:
    data = f.read()
hpa_threshold = 65
alert_HPA = json.loads(data)['alert_HPA']
for i in hpa_services:
    a=i
    a=a.replace("%","")
    a=int(a)
    hpa.append(a)
for i in range(0,len(services_names)):
    if(max_pod[i]==replica[i]):
        if(hpa[i]>hpa_threshold):
            flag=1
            alert_HPA[i]+=1
for i in range(0, len(alert_HPA)):
    if(alert_HPA[i] >= 6 and hpa[i]>hpa_threshold):
        print(services_names[i] + " is running on " + " maximum pod " + str(max_pod[i]) + " with CPU "+ str(hpa[i]) + "%")
#        file_output=str(services_names[i] + " is running on " + " maximum pod " + str(max_pod[i]) + " with CPU "+ str(hpa[i]) + "%")        
    elif hpa[i] <= hpa_threshold:
        alert_HPA[i] = 0
output_dict = {"alert_HPA": alert_HPA}
with open('/home/rishabh.tripathi/hpa_alert/config.json', 'w') as f:
    json.dump(output_dict, f)

