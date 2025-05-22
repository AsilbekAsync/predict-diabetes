# 🩺 Qandli diabetni bashorat qilish — Mashina o‘rganish asosida

Ushbu loyiha turli sog‘liq ko‘rsatkichlari (glukoza, qon bosimi, tana massasi indeksi va h.k.) asosida insonda qandli diabet bor yoki yo‘qligini bashorat qilish uchun mashina o‘rganish (ML) modelidan foydalanadi. Barcha bosqichlar — ma’lumotni tayyorlash, modellashtirish, baholash va saqlashdan iborat.

---

## 📁 Loyiha tuzilmasi

```
root/
│
├── data/
│   └── data.csv              # Kirish ma’lumotlar to‘plami (CSV formatda)
│
├── models/
│   ├── model.joblib          # Treningdan o‘tgan model
│   ├── scaler.joblib         # StandardScaler obyekti
│   └── imputer.joblib        # KNNImputer obyekti
│
├── accurancy.py              # Aniqlilikni hisoblash
├── api.py                    # Flask ilova
├── brain.py                  # Flask ilova uchun
├── save_model.py             # Modelni saqlash
└── README.md                 # Ushbu hujjat
```

---

## 🚀 Foydalanish bo‘yicha yo‘riqnoma

### 1. Kerakli kutubxonalarni o‘rnating

```bash
pip install pandas numpy scikit-learn imbalanced-learn joblib
```

### 2. Ma’lumotlar faylini joylashtiring

`data/data.csv` faylini quyidagi ustunlar bilan joylashtiring:

```
Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome
```

- `Outcome` — maqsad ustuni (1 = diabet, 0 = sog‘lom)

### 3. Skriptni ishga tushiring

```bash
python api.py
```

Bu skript quyidagilarni amalga oshiradi:

- 0 qiymatlarni `NaN`ga almashtirib, `KNNImputer` yordamida to‘ldiradi
- Ma’lumotlarni `StandardScaler` yordamida masshtablantiradi
- `SMOTE` yordamida ma’lumotlar sinf balansini tiklaydi
- `RandomForestClassifier` modeli bilan o‘qitadi
- Modelni saqlaydi va to‘liq ma’lumotlar to‘plami bo‘yicha aniqlikni chiqaradi

---

## 📊 Model tafsilotlari

- **Imputer**: `KNNImputer` — 0 qiymatlarni statistik yo‘l bilan to‘ldirish
- **Scaler**: `StandardScaler` — ma’lumotni normalizatsiya qilish
- **Model**: `RandomForestClassifier` — kuchli klassifikatsiya algoritmi
- **Balanslash**: `SMOTE` — kam sonli sinf namunasini ko‘paytirish

---

## ✅ Natija

Skript ishga tushgach, natijada quyidagicha aniqlik chiqariladi:

```
Accuracy: 99.60%
```

Yuqoridagi obyektlar `model/` papkasiga saqlanadi:

- `model.joblib`
- `scaler.joblib`
- `imputer.joblib`

---

## 📌 Litsenziya

Ushbu loyiha ta’limiy va tadqiqot maqsadida foydalanish uchun taqdim etilgan.

---

## 🙋 Muallif

Muallif: Kamoliddinov Asilbek. Taklif va mulohazalar uchun bog‘laning.
