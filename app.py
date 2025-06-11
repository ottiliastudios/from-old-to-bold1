import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

st.set_page_config(page_title="From Old to Bold")

st.title("💍 From Old to Bold")
st.write("Lade ein Bild deines alten Schmucks hoch. Unsere KI schätzt das Gewicht und schlägt dir passende neue Designs vor.")

# Dummy-Vorhersage
def dummy_predict(img):
    return 15.0  # Fixes Gewicht für Demo

uploaded_file = st.file_uploader("📤 Schmuckbild hochladen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Hochgeladenes Bild", use_column_width=True)
    predicted_weight = dummy_predict(image)
    st.success(f"📏 Geschätztes Gewicht: **{predicted_weight:.2f} g**")

    # Designs laden
    df = pd.read_csv("designs.csv")
    tolerance = 1.0  # ±1g Toleranz
    matched = df[np.abs(df["weight"] - predicted_weight) <= tolerance]

    st.subheader("✨ Passende neue Designs")
    if not matched.empty:
        for _, row in matched.iterrows():
            st.image(os.path.join("images", row["filename"]), caption=f"{row['name']} – {row['weight']} g", use_column_width=True)
    else:
        st.write("Keine passenden Designs gefunden.")
