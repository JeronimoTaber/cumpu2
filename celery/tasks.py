from celery import Celery

app = Celery('tasks', backend='redis://localhost',broker='redis://localhost:6379')

@app.task
def suma(x, y):
    return x + y

@app.task
def resta(x, y):
    return x - ya

@app.task
def mult(x, y):
    return x * y

@app.task
def pot(x, y):
    return pow(x,y)

@app.task
def div(x, y):
    if y != 0:
        return x/y
    return 0
