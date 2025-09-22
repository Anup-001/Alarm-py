from flask import Flask,request,jsonify
import time
from datetime import datetime
import winsound
import threading

app=Flask(__name__)

alarm_status={"status":"Idle"}

def get_current_time():
    return datetime.now().strftime("%H:%M")

def alarm_logic(alarm_time):
    alarm_status["status"]=f"Alarm set for {alarm_time}. Waiting..."
    while True:
        current_time=get_current_time()
        if current_time==alarm_time:
            alarm_status["status"]="Wake up! man..."
            winsound.Beep(3000, 3000) 
            break
        time.sleep(3) 
        
@app.route('/set_alarm',methods=['POST'])
def set_alarm():
    alarm_time=request.json.get('alarm_time')
    thread=threading.Thread(target=alarm_logic,args=(alarm_time,))
    thread.start()
    return jsonify({"message":f"Alarm set for {alarm_time}"}),200

@app.route('/status',methods=['GET'])
def get_status():
    return jsonify({"status":alarm_status["status"]})

if __name__=='__main__':
    app.run(debug=True)