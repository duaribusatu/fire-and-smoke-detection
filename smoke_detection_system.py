import cv2
import numpy as np
from keras.models import load_model
from alarm import trigger_alarm

model = load_model("smoke_detection_model.h5")
def detect_fire(frame, threshold=0.1):
    preprocess_frame = cv2.cvtColor(cv2.resize(frame,(48,48)), cv2.COLOR_BGR2GRAY)
    preprocess_frame = np.expand_dims(preprocess_frame, axis=0)
    preprocess_frame = np.expand_dims(preprocess_frame, axis=-1)
    preprocess_frame = preprocess_frame.astype("float32")/255

    prediction = model.predict(preprocess_frame)
    if prediction[0][1] >= threshold:
        return True
    else:
        return False
    
cap = cv2.VideoCapture("/Users/dandi/smoke-test.mp4")
if not cap.isOpened():
    print("Error: could not open video file")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if detect_fire(frame):
        trigger_alarm(volume=35)
        cv2.rectangle(frame, (100,100),(frame.shape[1]-100, frame.shape[0]-100),(0,0,255),2)
        cv2.putText(frame, "Warning, smoke is detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




