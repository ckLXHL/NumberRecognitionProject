from app import create_app, db

app = create_app('testing')
app_ctx = app.app_context()
app_ctx.push()

test_app = app.test_client()

def tearDown():
    app_ctx.pop()