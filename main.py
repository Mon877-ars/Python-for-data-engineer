
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="REMOVED_PASSWORD170105",  # sesuaikan password mysql kamu
        database="belajar_flask"
    )

# Halaman utama - tampilkan semua data
@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', mahasiswa=data)

# Halaman tambah data
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)",
                       (nama, nim, jurusan))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('tambah.html')

# Hapus data
@app.route('/hapus/<int:id>')
def hapus(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)",
                       (nama, nim, jurusan))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('tambah.html')