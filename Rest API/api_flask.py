from unittest import result
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/prime/<int:n>")
def prime(n):
    flag = False
    if n>1:
        for i in range(2,n//2+1):
            if n%i == 0:
                flag = True
                break
        
        if flag: 
            result = {
                    "Number" : n,
                    "Is Prime" : False,                    
                }
        else:
            result = {
                    "Number" : n,
                    "Is Prime" : True,                    
                }
    else:
        result = {
                    "Number" : n,
                    "Is Prime" : False,                    
                }
        
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)