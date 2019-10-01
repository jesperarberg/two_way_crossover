#!/usr/bin/python
import subprocess, sys, threading

class cecaudio:
    def __init__(self, callback):
        self.callback = callback
        self.listener = threading.Thread(target=self.monitor)
        self.listener.start()
        
    def monitor(self):
        # this will (most likely) disable the internal tv speakers and send audio on 
        p = subprocess.Popen('cec-client -t a', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            out = p.stdout.readline()
            #print(str(out))
            if out == '' and p.poll() != None:
                break
            if '05:44:41'.encode() in out:
                self.callback('vol_up')
            elif '05:44:42'.encode() in out:
                self.callback('vol_down')
            elif '05:44:43'.encode() in out:
                self.callback('mute')
