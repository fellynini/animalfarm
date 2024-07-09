from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

def insert_user(Animaltype, Animalid, Animalproduct):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO animalfarm (Animaltype, Animalid, Animalproduct) VALUES (%s, %s, %s)"
        cursor.execute(query, (Animaltype, Animalid, Animalproduct))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

@app.route('/', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        Animaltype = request.form['Animaltype']
        Animalid = request.form['Animalid']
        Animalproduct = request.form['Animalproduct']
        
        if insert_user(Animaltype, Animalid, Animalproduct):
            return redirect(url_for('success'))
        else:
            return "Failed to insert animalsfarm"
    else:
        return render_template('farm.html')

@app.route('/success')
def success():
    return "User successfully added"

db_config = {
    'user': 'root',
    'password': 'felister39941908',
    'database': 'animalfarm',
    'host': '12.7.0.0.1'
}

if __name__ == '__main__':
    app.run(debug=True)
                


         
