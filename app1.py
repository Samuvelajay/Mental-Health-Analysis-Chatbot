from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import joblib


app=Flask(__name__)

model=joblib.load(r"C:\Users\MICRO\Desktop\sam\mental_health_chatbot\mental_health_model.pkl")
label_encoder=joblib.load(r"C:\Users\MICRO\Desktop\sam\mental_health_chatbot\label_encoder.pkl")


def init_db():
    conn=sqlite3.connect("chatbot.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS ChatHistory
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone TEXT,
                    message TEXT,
                    prediction TEXT);''')
    conn.close()
    
def predict_mental_health(statement):
    prediction=model.predict([statement])[0]
    label=label_encoder.inverse_transform([prediction])[0]
    return label
 
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        return redirect(url_for("chatbot", name=name, phone=phone))
    return render_template("index.html")
   

@app.route("/chatbot/<name>/<phone>", methods=["GET", "POST"])
def chatbot(name, phone):
    prediction = None
    message = None
    if request.method == "POST":
        message = request.form["message"]
        prediction = predict_mental_health(message)

        
        conn = sqlite3.connect("chatbot.db")
        conn.execute("INSERT INTO ChatHistory (name, phone, message, prediction) VALUES (?, ?, ?, ?)",
                     (name, phone, message, prediction))
        conn.commit()
        conn.close()

    return render_template("chatbot.html", name=name, phone=phone, message=message, prediction=prediction)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

        
        
    