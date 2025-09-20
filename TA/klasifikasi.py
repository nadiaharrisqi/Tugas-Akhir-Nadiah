# klasifikasi.py
def klasifikasi_data(input_dict):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler

    # Ubah dictionary ke DataFrame
    input_df = pd.DataFrame(input_dict)

    # Load dan siapkan data pelatihan
    data = pd.read_csv('DATA TALENT SCOUTINGS LENGKAP 2.csv')
    data = data.drop(columns=['NO', 'NAMA'])
    data['JENIS KELAMIN (PA/PI)'] = data['JENIS KELAMIN (PA/PI)'].map({'PA': 0, 'PI': 1})

    X = data.drop(columns='POTENSI')
    y = data['POTENSI']

    # Normalisasi
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    input_scaled = scaler.transform(input_df)

    # KNN
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_scaled, y)

    prediction = knn.predict(input_scaled)

 # Hitung 2 tetangga terdekat
    distances, indices = knn.kneighbors(input_scaled, n_neighbors=3)
    tetangga = []
    for i in range(3):
        index = indices[0][i]
        jarak = distances[0][i]
        data_asli = data.iloc[index].to_dict()
        data_asli = data.iloc[index]
        tetangga.append({
            'POTENSI': data_asli['POTENSI'],
            'JARAK': round(jarak, 4)
        })


    return prediction[0], tetangga