# -- coding: utf-8 --
import streamlit as st
import os

st.title("🦋 Welcome to Telugu Recipe App!")
st.subheader("తెలుగు వంటకాలు యాప్‌కు స్వాగతం!")

# Function to load text files
def load_text_files(folder_path):
    data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data[filename] = f.read()
    return data

# Load all files from the 'data' folder
dataset_folder = "data"
dataset = load_text_files(dataset_folder)

# User input
user_input = st.text_input(
    "Type a keyword(e.g., biryani) from the following options: "
    "[Mutter Rice, Tahari, Khichdi with Kheema, Chicken Shawarma, Qurbani ka Meetha, "
    "Sheer Khurma, Fruit Custard, Kunafa, Kaddu ki Kheer, Hyderabadi Mandi, Malai Kofta, "
    "Chicken 65, Fish Fry, Shahi Paneer, Chicken Shami Kebab, Mixed Vegetable Curry, "
    "Chicken Pickle, Mango Pickle, Tomato Pickle, Biryani]:"
).strip()

if user_input:
    found = False
    for file_name, content in dataset.items():
        # Search in file name and file content (case-insensitive)
        if user_input.lower() in file_name.lower() or user_input.lower() in content.lower():
            st.write(f"*Match found in {file_name}:*")
            st.text(content)
            found = True

    if not found:
        st.warning("No match found in dataset.")
