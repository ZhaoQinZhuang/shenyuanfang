from flask import Flask, render_template, request, Blueprint

app = Flask(__name__)

# 创建蓝图对象
main_bp = Blueprint('main', __name__)
dazhansai_bp = Blueprint('dazhansai', __name__, url_prefix='/dazhansai')
doudouriji_bp = Blueprint('doudouriji', __name__, url_prefix='/doudouriji')

# 使用蓝图对象定义主页路由
@main_bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        return name + " " + password

@main_bp.route("/xiaoshuo.html", methods=['GET', 'POST'])
def xiaoshuo():
    if request.method == 'GET':
        return render_template('xiaoshuo.html')

@main_bp.route("/caidan.html", methods=['GET', 'POST'])
def caidan():
    if request.method == 'GET':
        return render_template('caidan.html')

@main_bp.route("/huanying.html", methods=['GET', 'POST'])
def huanying():
    if request.method == 'GET':
        return render_template('huanying.html')

@main_bp.route("/choujiang.html", methods=['GET', 'POST'])
def choujiang():
    if request.method == 'GET':
        return render_template('choujiang.html')

# 使用蓝图对象定义dazhansai相关路由
@dazhansai_bp.route('/<path>.html', methods=['GET', 'POST'])
def dazhansai_route(path):
    if request.method == 'GET':
        return render_template('dazhansai/' + path + '.html')\

@doudouriji_bp.route('/<path>.html', methods=['GET', 'POST'])
def doudouriji_route(path):
    if request.method == 'GET':
        return render_template('doudouriji/' + path + '.html')

# 在主应用中注册蓝图
app.register_blueprint(main_bp)
app.register_blueprint(dazhansai_bp)
app.register_blueprint(doudouriji_bp)

if __name__ == '__main__':
    app.run()