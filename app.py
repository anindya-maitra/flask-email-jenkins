from flask import Flask

app=Flask(__name__)

def greet_user():
    user_name = input("What is your name? ")
    greeting = f"Hello, {user_name}!"
    print(greeting)
    return greeting

@app.route('/')
def hello():
    return "hello world"

if __name__ == '__main__':
   app.run(port=12345)
