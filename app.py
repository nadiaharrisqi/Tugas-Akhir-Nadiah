from flask import Flask, render_template, request
from klasifikasi import klasifikasi_data
from evaluasi import evaluasi_model

app = Flask(__name__)

# Halaman Beranda
@app.route('/')
def home():
    return render_template('home.html')

# Halaman Klasifikasi - Form
@app.route('/klasifikasi', methods=['GET', 'POST'])
def klasifikasi():
    if request.method == 'POST':
        try:
            nama = request.form['nama']
            jk = 0 if request.form['jk'] == 'PA' else 1
            jk_label = 'Putra' if jk == 0 else 'Putri'
            usia = int(request.form['usia'])
            tinggi = int(request.form['tinggi_badan'])
            berat = int(request.form['berat_badan'])
            lengan = int(request.form['rentang_tangan'])
            td = int(request.form['tinggi_duduk'])
            lompat = int(request.form['lompat'])
            tenis = int(request.form['tenis'])
            polo = int(request.form['polo_air'])
            lari = int(request.form['kelincahan'])
            waktu = float(request.form['lari_25m'])
            shuttle = int(request.form['shuttle_run'])

            input_data = {
                    'JENIS KELAMIN (PA/PI)': [jk], 
                    'USIA': [usia], 
                    'TINGGI BADAN (CM)': [tinggi], 
                    'BERAT BADAN (KG)': [berat], 
                    'TINGGI DUDUK (CM)': [td], 
                    'RENTANG TANGAN (CM)': [lengan], 
                    'LEMPAR & TANGKAP TENIS': [tenis], 
                    'LEMPAR POLO AIR': [polo], 
                    'LOMPAT TEGAK (CM)': [lompat], 
                    'LARI KELINCAHAN': [lari], 
                    'LARI 25 M (DETIK)': [waktu], 
                    'SUTTLE RUN': [shuttle]
            }
            
            hasil, tetangga = klasifikasi_data(input_data)
            return render_template('hasil2.html', nama=nama, jk=jk_label, hasil=hasil, tetangga=tetangga)

        except Exception as e:
                return f"Terjadi kesalahan pada klasifikasi : {e}"

    return render_template('klasifikasi.html')

# Halaman Evaluasi
@app.route('/evaluasi', methods=['GET', 'POST'])
def evaluasi():
    if request.method == 'POST':
        try:
            nilai_k = int(request.form['nilaiK'])
            nilai_cv = int(request.form['KFold'])

            hasil = evaluasi_model(nilai_k, nilai_cv)
            return render_template('hasil1.html', hasil=hasil)
        
        except Exception as e:
            return f"Terjadi kesalahan saat evaluasi: {e}"
    
    return render_template('evaluasi.html')


# Jalankan server Flask
if __name__ == '__main__':
    app.run(debug=True)
