from website import app


@app.route('/')
def index():
    return current_app.send_static_file('index.html')


