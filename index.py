from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
# url映射的函数，要传参则在上述route（路由）中添加参数申明
def index():
    if request.method == 'GET':
        # 想要html文件被该函数访问到，首先要创建一个templates文件，将html文件放入其中
        # 该文件夹需要被标记为模板文件夹，且模板语言设置为jinja2
        return render_template('index.html')
    # 此处欲发送post请求，需要在对应html文件的form表单中设置method为post
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        return name + " " + password
@app.route("/小说.html", methods=['GET', 'POST'])
def xiaoshuo():
    if request.method == 'GET':
        return render_template('xiaoshuo.html')
@app.route("/菜单.html", methods=['GET', 'POST'])
def caidan():
    if request.method == 'GET':
        return render_template('caidan.html')
@app.route("/欢迎.html", methods=['GET', 'POST'])
def huanying():
    if request.method == 'GET':
        return render_template('huanying.html')
@app.route("/抽奖.html", methods=['GET', 'POST'])
def choujiang():
    if request.method == 'GET':
        return render_template('choujiang.html')
@app.route('/大战赛/目录.html', methods=['GET', 'POST'])
def mulu():
    if request.method == 'GET':
        return render_template('dazhansai/目录.html')
@app.route('/大战赛/第一部.html', methods=['GET', 'POST'])
def mulu1():
    if request.method == 'GET':
        return render_template('dazhansai/第一部.html')
@app.route('/大战赛/第二部.html', methods=['GET', 'POST'])
def mulu2():
    if request.method == 'GET':
        return render_template('dazhansai/第二部.html')
if __name__ == '__main__':
    app.run()
