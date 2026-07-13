import unittest
from main import app

class FlaskTest(unittest.TestCase):

    # تست ۱: بررسی باز شدن صفحه ورود
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'login', response.data.lower())

# تست ۲: بررسی باز شدن صفحه آپلود (بعد از لاگین فرضی

f test_upload_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/upload')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()




