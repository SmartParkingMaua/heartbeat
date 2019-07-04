import sched, time, requests
s = sched.scheduler(time.time, time.sleep)

requests.get("http://willianchan.pythonanywhere.com/estouvivo")

def sendHeartBeat(sc): 
    print("Mandando GET")
    requests.get("http://willianchan.pythonanywhere.com/estouvivo")
    s.enter(60, 1, sendHeartBeat, (sc,))

s.enter(60, 1, sendHeartBeat, (s,))
s.run()
