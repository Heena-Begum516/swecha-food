# 🦋 Telugu Recipe App

A simple and user-friendly **Streamlit** application to search and view Telugu recipes stored as text files in a local dataset.

---

## Features
- Search recipes by keywords in recipe names or contents.
- Supports recipes written in Telugu using UTF-8 encoding.
- Dynamic loading of `.txt` recipe files from the `data` folder.
- Easy-to-use web interface built with Streamlit.
- Can be run locally or deployed on Streamlit Cloud.

---

## Project Structure

swecha-food/

├── data/ # Folder containing recipe text files (.txt)

│ ├── biryani.txt

│ ├── chicken65.txt

│ └── ...

├── app.py # Main Streamlit application

├── requirements.txt # Python dependencies

├── README.md # Project documentation (this file)

├── CONTRIBUTING.md # Contribution guidelines

├── CHANGELOG.md # Version history

├── LICENSE # License file

└── REPORT.md # Full project report


---

## Installation and Setup

1. **Clone the repository:**

    git clone https://github.com/Heena-Begum516/swecha-food.git
    cd swecha-food

2. **Create and activate a virtual environment**

    python -m venv venv
   
    Windows:
    venv\Scripts\activate
   
    Mac/Linux:
    source venv/bin/activate

4. **Install dependencies**

    pip install -r requirements.txt

6. **Run the app**

    streamlit run app.py
   Open the URL provided (usually http://localhost:8501) in your browser.
   
---

## Usage

- Add your recipe text files into the data folder (ensure they are UTF-8 encoded).

- In the app, enter a keyword (for example, Biryani) in the search box.

- Matching recipes will be displayed with their content.

---

### Deployment

You can deploy this app easily on Streamlit Cloud:

1. Push your project to a GitHub repository.
2. Go to Streamlit Cloud and sign in.
3. Create a new app by connecting your GitHub repo.
4. Set branch to main and file path to app.py.
5. Deploy and share the live URL.

---

### Contributing

Contributions are welcome! Please see CONTRIBUTING.md for guidelines.

---

### License

This project is licensed under the MIT License.

---

### Author

Swecha Food Team

Contact: ayesha.h33n4@gmail.com
