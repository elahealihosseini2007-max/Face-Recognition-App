from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ۱. صفحه ورود (Login)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        return redirect(url_for('upload_page'))
    return render_template('login.html')

# ۲. صفحه آپلود و پردازش تصویر
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # اینجا در آینده کدهای پردازش تصویر و تشخیص چهره اضافه می‌شود
        return "تصویر با موفقیت دریافت و پردازش شد!"
    return render_template('index.html')

if __name__ == '__main__':
    
    app.run(debug=True)
