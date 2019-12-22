import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('best.h5')
model.summary()

def pred(frame):
	pred = model.predict([frame])
	if np.max(pred)*100 > 80: 
		pred = np.argmax(pred)
		print(pred)


def cap():
	cap = cv2.VideoCapture(0)
	while cap.isOpened():
		ret,frame = cap.read()
		frame1 = cv2.resize(frame,(224,224))
		frame1 = np.expand_dims(frame1,axis=0)
		pred(frame1)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

cap()