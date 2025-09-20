# evaluasi.py
def evaluasi_model(k, kfold):
    import pandas as pd
    from sklearn.model_selection import cross_val_predict
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import cross_val_predict, cross_val_score


    data = pd.read_csv('DATA TALENT SCOUTINGS LENGKAP 2.csv')
    data = data.drop(columns=['NO', 'NAMA'])

    data['JENIS KELAMIN (PA/PI)'] = data['JENIS KELAMIN (PA/PI)'].map({'PA': 0, 'PI': 1})
    X = data.drop(columns='POTENSI')
    y = data['POTENSI']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KNeighborsClassifier(n_neighbors=k)
    y_pred = cross_val_predict(model, X_scaled, y, cv=kfold)
    scores = cross_val_score(model, X_scaled, y, cv=kfold)

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    y_pred_encoded = le.transform(y_pred)

    report = classification_report(y_encoded, y_pred_encoded, output_dict=True)
    matrix = confusion_matrix(y_encoded, y_pred_encoded)
    auc = roc_auc_score(y_encoded, y_pred_encoded)

    return {
        'accuracy': round(report['accuracy'] * 100, 2),
        'precision': round(report['weighted avg']['precision'] * 100, 2),
        'recall': round(report['weighted avg']['recall'] * 100, 2),
        'f1': round(report['weighted avg']['f1-score'] * 100, 2),
        'auc': round(auc * 100, 2),
        'confusion_matrix': matrix.tolist(),
        'scores_per_fold': [round(s * 100, 2) for s in scores],
        'report_dict': report,
        'k': k,
        'cv': kfold
    }
