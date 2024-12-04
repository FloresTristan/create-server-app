import os


def create_app_routes(project_name):
    app_py_content = """from flask import Flask
from AppConfig import AppConfig

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    if AppConfig().getIsDevEnvironment():
        print(
            "\\033[92m_______________________"
            f"{AppConfig().getEnvironment().upper()}_______________________\\033[0m"
        )
    if AppConfig().getIsProductionEnvironment():
        print(
            "\\033[91m_______________________"
            f"{AppConfig().getEnvironment().upper()}_______________________\\033[0m"
        )

    if AppConfig().getisLocalEnvironment():
        # dev
        app.run(debug=False, host='0.0.0.0', port=5000)
    else:
        # production
        app.run(host='0.0.0.0', port=8080)
"""
    with open(os.path.join(project_name, 'app.py'), 'w') as f:
        f.write(app_py_content)
