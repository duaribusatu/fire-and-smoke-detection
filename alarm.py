from gtts import gTTS # type: ignore
import os

def trigger_alarm(volume=50):
    alarm_message = "Alert! Fire has been detected. Evacuate to the secure area"
    tts = gTTS(text=alarm_message, lang='en')
    tts.save("fire-alarm.mp3")
    os.system(f"afplay -v {volume} fire-alarm.mp3")

trigger_alarm(volume=35)



    