# Phishing-Detection-Extension

A browser extension that detects phishing websites using Machine Learning by analyzing multiple URL parameters and domain details. This open-source project aims to enhance user security by providing real-time warnings for suspicious links.

---

## 🚀 Features

- **Machine Learning-Based Detection** – Analyzes 30+ URL parameters to detect phishing websites.   
- **Real-Time Alerts** – Notifies users immediately upon visiting a suspicious website.  
- **Cross-Browser Support** – Compatible with Chrome, Edge, and Firefox.  
- **Open Source & Extensible** – Easily add more phishing indicators or improve the ML model.  

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Browser Extension APIs)  
- **Backend/Model:** Python (Flask/FastAPI for ML integration)  
- **Machine Learning:** Random Forest / Decision Tree models  

---

## 📂 Project Structure

Phishing-Detection-Extension/
│
├── extension/ # Browser extension files (manifest.json, popup.html, scripts)
├── model/ # Machine learning model training and saved files
├── backend/ # API to connect ML model with extension
├── assets/ # Icons, screenshots, and other static files
├── README.md # Documentation
├── LICENSE # MIT License
└── CONTRIBUTING.md # Contribution guidelines


---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/Kayyum0/Phishing-Detection-Extension.git
cd Phishing-Detection-Extension
2. Load Extension in Browser
Open chrome://extensions/

Enable Developer Mode

Click Load unpacked and select the extension/ folder

3. Run Backend (Optional if using API)
cd backend
pip install -r requirements.txt
python app.py
📊 How It Works
Extracts parameters from the current URL (length, subdomains, HTTPS status, etc.)

Evaluates them using a pre-trained ML model (stored locally or served via API).

Performs additional WHOIS checks for domain authenticity.

Shows result: Safe / Suspicious / Phishing in real time.

📸 Screenshots

🤝 Contributing
We welcome contributions from everyone! Please check out CONTRIBUTING.md for guidelines on how to get started.

📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Shaikh Kayyum Ayaz

GitHub: @kayyum0

Email: kayyums150@gmail.com

🌟 Support
If you like this project, consider giving it a star ⭐ on GitHub to show your support!
