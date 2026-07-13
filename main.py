import os
import cv2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads,


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       username = request.form.get('username')
       password = request.form.get('password')

     if username == "admin" and password == "1234":
         return redirect(url_for('upload_page'))

     else:
         return "نام کاربری یا رمز عبور اشتباه است! دوباره تلاش کنید"
    return render_template('login.html')


# ۲. صفحه آپلود و پردازش تصویر
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "فایلی ارسال نشده است"

        file = request.files['file']
        if file.filename == '':
            return "هیچ فایلی انتخاب نشده است"

if file:
            # ذخیره فایل اصلی آپلود شده در پوشه static/uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

image = cv2.imread(filepath)
            if image is None:
                return "خطا در خواندن تصویر! لطفاً یک عکس معتبر آپلود کنید."

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
              

           
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  
                

            result_filename = 'result_' + file.filename
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)
            cv2.imwrite(result_path, image)
        
            

            return f"""
            <div styile="text-align: center; font-family: Tahoma; direction: rtl; padding: 50px;">
                <h2>پردازش با موفقیت انجام شد!</h2>
                <p>تعداد چهره های شناسایی شده:<b>{len(faces)}</b></p>
                <p>تصویر با کادر سبز در پوشه پروژه ذخیره شد.</p>
                <br>
                <a href="/upload" style=padding: 10px 20px; background: #007bff; color: white; text-direction: none; border-radius: 5px;">آپلود عکس دیگر</a>

           </div>
           """


           return render_template('index.html)
     if __name__=='__main__':
        app.run(debug=True)
