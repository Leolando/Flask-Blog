from flaskblog import create_app
from flaskblog import db
app = create_app()
app.app_context().push()
db.create_all()
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
