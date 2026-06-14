from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>首页</h1><p>这是我的第一个 Flask 网站。</p>"


@app.route("/about")
def about():
    return "<h1>关于我</h1><p>我是电子信息专业研究生，正在学习 Python、AI 和多模态。</p>"


@app.route("/project")
def project():
    return "<h1>我的项目</h1><p>学生成绩管理系统 V2.1</p>"


@app.route("/contact")
def contact():
    return "<h1>联系方式</h1><p>GitHub: lijiatu3427-maker</p>"

if __name__ == "__main__":
    app.run(debug=True)