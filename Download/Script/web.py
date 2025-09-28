from flask import Flask, render_template_string

app = Flask(__name__)

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
      <meta charset="UTF-8">
      <title>الصفحة الرئيسية</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">

      <nav class="navbar navbar-dark bg-dark">
        <div class="container">
          <a class="navbar-brand" href="/">موقعي</a>
          <a class="nav-link text-white" href="/contact">تواصل</a>
        </div>
      </nav>

      <div class="container text-center mt-5">
        <h1 class="display-4">مرحبا بك في موقعي Flask 🎉</h1>
        <p class="lead">هذا مثال بسيط على موقع باستخدام Flask و Bootstrap</p>
        <a href="/contact" class="btn btn-primary btn-lg mt-3">اذهب لصفحة التواصل</a>
      </div>

    </body>
    </html>
    """)

# صفحة التواصل
@app.route("/contact")
def contact():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
      <meta charset="UTF-8">
      <title>تواصل معنا</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">

      <nav class="navbar navbar-dark bg-dark">
        <div class="container">
          <a class="navbar-brand" href="/">موقعي</a>
          <a class="nav-link text-white" href="/contact">تواصل</a>
        </div>
      </nav>

      <div class="container mt-5">
        <h2 class="mb-4">📩 تواصل معنا</h2>
        <form>
          <div class="mb-3">
            <label class="form-label">الاسم</label>
            <input type="text" class="form-control" placeholder="اكتب اسمك">
          </div>
          <div class="mb-3">
            <label class="form-label">البريد الإلكتروني</label>
            <input type="email" class="form-control" placeholder="example@email.com">
          </div>
          <div class="mb-3">
            <label class="form-label">رسالتك</label>
            <textarea class="form-control" rows="4" placeholder="اكتب رسالتك هنا"></textarea>
          </div>
          <button type="submit" class="btn btn-success">إرسال</button>
        </form>
      </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)