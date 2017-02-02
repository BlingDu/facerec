from flask import Flask
from flask import render_template, redirect
import cv2
import time
import facerec
import datetime


app = Flask(__name__)


@app.route('/')
def index():
	title = "home"
	header = "face recognition"
	content = "write something"
	date = datetime.datetime.today()
	return render_template('index.html', title=title, header=header,\
		content=content, date=date)


@app.route('/login')
def login():
	frame = facerec.take_pic()
	crop = facerec.crop_face(frame)
	face_test = facerec.compare_faces(crop)
	if face_test >= 0.9:
		return redirect('/')
#cv2.imwrite('test.jpg', frame)
	return "fail"


@app.route('/register')
def register():
	frame = facerec.take_pic()
	cv2.imwrite('base.jpg', frame)
	return "registered"


if __name__ == '__main__':
	app.run(debug=True)