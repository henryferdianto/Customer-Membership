# Customer Membership Prediction System

> **TL;DR** — Machine learning system untuk memprediksi tingkat membership pelanggan (Platinum/Gold/Silver) berdasarkan pengeluaran dan pendapatan bulanan menggunakan Euclidean Distance.

---

## 🔬 Business Question

Bagaimana menentukan tingkat membership yang tepat untuk pelanggan baru berdasarkan karakteristik finansial mereka?

**Tujuan:**
- Memprediksi membership yang sesuai berdasarkan monthly expense dan monthly income
- Memberikan diskon yang tepat sesuai tingkat membership
- Mengotomatisasi proses klasiikasi pelanggan

---

## 📊 Dataset & Preprocessing

| Aspek | Detail |
|---|---|
| **Sumber** | Data internal PacCommerce (dummy data) |
| **Fitur** | Monthly Expense (juta), Monthly Income (juta) |
| **Target** | Membership Level (Platinum/Gold/Silver) |
| **Metode** | Euclidean Distance |

### Membership Parameters

| Level | Min Expense (juta) | Min Income (juta) | Discount |
|---|---|---|---|
| Platinum | 8 | 15 | 15% |
| Gold | 6 | 10 | 10% |
| Silver | 5 | 7 | 8% |

---

## 🧮 Metodologi

```
1. Hitung Euclidean Distance antara (expense, income) user
   dengan setiap centroid membership

2. Pilih membership dengan distance terkecil

3. Output: Predicted membership level
```

### Formula

```
distance = √((expense - centroid_expense)² + (income - centroid_income)²)
```

---

## 💡 Key Findings

1. **Threshold清晰**: Batas expense/income untuk setiap membership sangat jelas
2. **Euclidean Distance efektif** untuk klasiikasi berbasis proximity
3. **Discount calculation** otomatis berdasarkan membership

---

## 🚀 Cara Menjalankan

```bash
# Clone repo
git clone https://github.com/henryferdianto/Customer-Membership.git
cd Customer-Membership

# Install dependencies
pip install tabulate

# Jalankan program
python "Customer membership.py"
```

---

## ⚠️ Limitations

- Data masih dummy (hanya 3 user)
- Algoritma masih sederhana — belum menggunakan ML sophisticated
- Belum ada validasi dataset besar

---

## 🛠️ Tech Stack

- Python
- tabulate (tabel output)
- math (Euclidean Distance)

---

## 📜 License

MIT License — lihat [LICENSE](LICENSE).