### 🏍️ Bike Price Prediction Web App
This project is a Flask-based machine learning web application that predicts the price of a used bike based on key features such as mileage, engine size, engine power, brand, and fuel type. It uses a pre-trained Scikit-learn pipeline (bike_price_pipeline.pkl) for making predictions.

### 🚀 Features

- Predicts used bike prices based on user input
- Uses a trained ML pipeline for accurate price estimation
- Flask backend with REST API (/predict)
- Easy to deploy on Render, Heroku, or any Flask-compatible hosting
- Lightweight and simple to run locally

### 🧠 Model Details
The model (bike_price_pipeline.pkl) is a pre-trained machine learning pipeline built with Scikit-learn.
It uses regression algorithms on processed bike data to predict the logarithm of the price, which is then exponentiated back to get the real price.

### 📂 Project Structure
├── app.py                    # Flask app entry point

├── bike_price_pipeline.pkl   # Pre-trained ML model

├── requirements.txt          # Dependencies list

└── templates/
    └── index.html            # Frontend (to be added if not present)

### ⚙️ Installation & Setup
#### 1️⃣ Clone the repository
git clone https://github.com/Amritesh03/bike-price-prediction.git
cd bike-price-prediction

#### 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate     # For Linux/Mac
venv\Scripts\activate        # For Windows

#### 3️⃣ Install dependencies
pip install -r requirements.txt

#### 4️⃣ Run the Flask app
python app.py


The app will start running at:
➡️ http://127.0.0.1:5000/

### 📡 API Endpoint
#### POST /predict
#### Request Body (JSON):

{
  "mileage_k": 25000,
  "service_count": 3,
  "engine_size": 150,
  "engine_power": 13.5,
  "brand": "Yamaha",
  "fuel_type": "Petrol",
  "bike_type": "Sports"
}

#### Response:
{
  "predicted_price": 75200.45
}

### 🧾 Requirements

All dependencies are listed in requirements.txt
flask
flask_cors
pandas
numpy
seaborn
matplotlib
scikit-learn

### 🌐 Deployment

You can deploy this Flask app easily on:
- Render (recommended)
- Heroku
- Vercel (with API route setup)
- AWS EC2 / Google Cloud / Azure

Make sure to set:
PORT=5000

### ✨ Future Enhancements
- Add a frontend UI (HTML form for user inputs)
- Add brand & type dropdowns dynamically
- Integrate model retraining pipeline
- Enable file-based data prediction (CSV upload)

### 👨‍💻 Author
**Amritesh Dubey**
📧 dwivediamritesh37@gmail.com
🔗 www.linkedin.com/in/amritesh-kumar-dwivedi-381896292
📧 [your-email@example.com
]
🔗 LinkedIn Profile
