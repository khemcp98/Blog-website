import requests
from flask import Flask, render_template, request

app = Flask(__name__)
response = requests.get('https://api.npoint.io/a6fb38954bedc3f509c0')
data = response.json()


@app.route('/')
@app.route('/index.html')
def homepage():
    return render_template('index.html', posts=data)


@app.route('/contact.html', methods=["POST", "GET"])
def goto_contact():
    if request.method == "POST":
        from smtplib import SMTP

        form_data = request.form
        name = form_data['name']
        email = form_data['email']
        phone = form_data['phone-no']
        query = form_data['msg']
        massage = 'Massage sent successfully'

        to_mail = 'khemvi199844@gmail.com'

        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=to_mail, password='onbdcmoajvkzpsxt')
            connection.sendmail(from_addr=to_mail, to_addrs=to_mail, msg='Subject: Query from blog website \n\n'
                                                                         f'Name: {name}\n'
                                                                         f'Email: {email}\n'
                                                                         f'Phone No: {phone}\n'
                                                                         f'Massage: {query}')

        return render_template('contact.html', text=massage)
    else:
        return render_template('contact.html')


@app.route('/about.html')
def goto_about():
    return render_template('about.html')


@app.route('/post.html/<int:num>')
def goto_post(num):
    post_num = data[num - 1]
    return render_template('post.html', post=post_num)


# @app.route('/form-data', methods=["POST"])
# def details():
#
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone-no']
#     msg = request.form['msg']
#     return f'<h1> massage sent {name} {email} {phone} {msg}</h1>'


if __name__ == "__main__":
    app.run(debug=True)
