# app/utils/eye_tracking.py
from pygaze import EyeTracker
from pygaze.display import Display
from pygaze.logfile import Logfile
import time

class EyeTrackingManager:
    def __init__(self, user_id):
        self.display = Display()
        self.tracker = EyeTracker(self.display)
        self.log = Logfile(filename=f"eye_tracking_{user_id}_{int(time.time())}")
        self.is_tracking = False
        
    def start_tracking(self):
        self.tracker.start_recording()
        self.is_tracking = True
        
    def stop_tracking(self):
        if self.is_tracking:
            self.tracker.stop_recording()
            self.is_tracking = False
            
    def log_gaze_with_event(self, event_type, question_id=None):
        if self.is_tracking:
            gaze = self.tracker.sample()
            timestamp = time.time()
            self.log.write([timestamp, gaze, event_type, question_id])