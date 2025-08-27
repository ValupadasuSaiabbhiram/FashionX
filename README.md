# 👕 FashionX – AI-Powered Fashion Recommender System  

FashionX is an AI-based **fashion recommender system** that suggests visually similar outfits using deep learning.  
Built with **TensorFlow (ResNet50), Streamlit, and scikit-learn**, it helps users discover clothing items that match their uploaded images.  

---

## 🚀 Features
- 🧠 **Deep Learning Model (ResNet50)** for feature extraction.  
- 📊 **Precomputed Embeddings** (`embeddings.pkl` + `filenames.pkl`) for fast similarity search.  
- 🔍 **Content-Based Filtering** using **Nearest Neighbors (sklearn)**.  
- 🖥️ **Streamlit Web App** for easy interaction.  
- 🐳 **Dockerized** for simple deployment.  
- 📂 **Sample Images & Uploads** to test recommendations.  

---

## 🛠️ Tech Stack
- **Python 3.11**
- **TensorFlow / Keras** (ResNet50, feature extraction)  
- **scikit-learn** (NearestNeighbors)  
- **NumPy, OpenCV, PIL**  
- **Streamlit** (UI)  
- **Docker & Docker Compose**  

---

## 📂 Project Structure
```
├── .dockerignore
├── .gitignore
├── .streamlit/              # Streamlit configuration (config.toml)
├── Dockerfile               # Docker image setup
├── docker-compose.yml       # Docker Compose service
├── app.py                   # Streamlit UI (main frontend)
├── main.py                  # Core recommendation logic
├── test.py                  # Local testing script (OpenCV display)
├── embeddings.pkl           # Precomputed embeddings (large, not tracked in GitHub)
├── filenames.pkl            # Associated filenames (large, not tracked in GitHub)
├── requirements.txt         # Python dependencies
├── sample/                  # Sample images for testing
└── images/                  # Dataset (used to generate embeddings)
```
```yaml
---

## ⚡ Getting Started  

### 🔹 Run Locally (without Docker)  
```bash
# 1. Clone repo
git clone https://github.com/<your-username>/fashionx.git
cd fashionx

# 2. Create virtual env
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Streamlit app
streamlit run app.py
```
👉 Open http://localhost:8501 in your browser.

---

## ⚡ Getting Started  

### 🔹 Run Locally (without Docker)  
```bash
# 1. Clone repo
git clone https://github.com/<your-username>/fashionx.git
cd fashionx

# 2. Create virtual env
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Streamlit app
streamlit run app.py
```
👉 Open http://localhost:8501 in your browser.

## 🔹 Run with Docker
Make sure Docker & Docker Compose are installed.

```bash
# Build & run container
docker compose up --build
```

Open: http://localhost:8501


## 🔹 Generate Embeddings (one-time preprocessing)
Before using the recommender, generate embeddings.pkl and filenames.pkl from your dataset:

```bash
python app.py
```
(where app.py contains your feature extraction loop).

These files are large, so they are not pushed to GitHub (see .gitignore).

## 📖 Usage
- Start the app (streamlit run app.py or via Docker).

- Upload an image (e.g., shirt, dress).

- FashionX finds 5 most similar items from the dataset.

- Browse recommendations directly in the Streamlit UI.


## 🤝 Contributing
Contributions are welcome!

- Fork the repo

- Create a feature branch

- Submit a PR

## 📜 License
- MIT License © 2025 Sai Abbhiram Valupadasu




