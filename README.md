# 🔐 End-to-End Verifiable E-Voting System with Cryptographic Security and Multilingual Receipt Generation

## 📌 Overview

This project implements a secure and transparent **End-to-End Verifiable (E2E-V) Electronic Voting System** using cryptographic techniques. It ensures vote privacy, integrity, and verifiability while also improving accessibility through **multilingual PDF receipt generation**.

---

## 🚀 Features

* 🔐 **Cryptographic Voting**

  * Secure vote encryption using ElGamal
  * Ensures confidentiality of voter choices

* ⛓️ **Blockchain-style Ledger**

  * Hash-chained vote storage
  * Detects tampering via ledger verification

* 🔍 **End-to-End Verifiability**

  * Voters can verify their vote using receipt ID
  * Independent audit support

* 📄 **Multilingual PDF Receipts**

  * Receipts available in:

    * English
    * Hindi
    * Tamil
    * Telugu
    * Malayalam
  * Unicode font rendering using ReportLab

* ⚠️ **Attack Simulation**

  * Simulate malicious changes
  * Detect compromised system state

* 📊 **Vote Tallying**

  * Secure decryption and result computation

---

## 🏗️ Project Structure

e2e-verifiable-voting/
│
├── backend/
│   ├── crypto/              # Key generation & encryption
│   ├── ledger/              # Vote storage & verification
│   ├── tally/               # Vote counting
│   ├── audit/               # Receipt verification & attacks
│   ├── fonts/               # Unicode fonts (for multilingual PDF)
│   ├── generate_receipt_pdf.py
│   └── translations.py
│
├── web/
│   ├── templates/           # HTML UI (Flask)
│   └── app.py               # Flask backend
│
├── scripts/                 # Simulation scripts
├── requirements.txt
├── README.md

---

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/e2e-verifiable-voting.git
cd e2e-verifiable-voting

---

### 2️⃣ Create virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

---

## ▶️ Running the Application

python3 -m web.app

Open in browser:
http://127.0.0.1:5000/

---

## 🌐 Multilingual Support

The system supports multiple Indian languages for voter receipts using Unicode fonts:

| Language  | Code |
| --------- | ---- |
| English   | en   |
| Hindi     | hi   |
| Tamil     | ta   |
| Telugu    | te   |
| Malayalam | ml   |

---

## 🔐 Security Features

* End-to-End Encryption using ElGamal
* Hash chaining for tamper detection
* Ledger verification mechanism
* Secure audit and dispute resolution

---

## 🧪 Testing Features

* Vote casting & verification
* Attack simulation
* Ledger integrity check
* Multilingual PDF generation

---

## 📄 Sample Workflow

1. Cast vote
2. Receive receipt ID
3. Verify vote using receipt ID
4. Download multilingual PDF receipt
5. Audit system integrity

---

## ⚠️ Notes

* PDF files are generated dynamically and not stored permanently
* Fonts are required for multilingual rendering
* Do not remove backend/fonts/ folder

---

## 👨‍💻 Tech Stack

* Python (Flask)
* Cryptography (ElGamal)
* ReportLab (PDF generation)
* HTML/CSS (Frontend)

---

## 🎓 Project Significance

This project demonstrates:

* Secure digital voting systems
* Cryptographic protocol implementation
* Real-world system design
* Accessibility via multilingual support

---

## 📬 Future Enhancements

* 🌍 Full multilingual UI
* 📱 Mobile-friendly interface
* 🔐 QR-based receipt verification
* ☁️ Deployment on cloud

---

## 👤 Authors
Sandrazen S
Abhinav Yarramsetti
Arjjitha S
(B.Tech Computer Science Engineering students from VIT Chennai)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
