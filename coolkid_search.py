# -*- coding: utf-8 -*-
"""coolkid_search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sOZJ-wZIHtoowY_Wy89tZFvI68uYA8j1
"""

import streamlit as st
import pandas as pd

def load_data():
    return [
        {"name": "Sushi Delight", "cuisine": "Japanese", "rating": 4.5, "location": "Downtown", "promo": "10% off with Visa"},
        {"name": "Steak House", "cuisine": "Western", "rating": 4.8, "location": "Uptown", "promo": "Free dessert with Mastercard"},
        {"name": "Spicy Thai", "cuisine": "Thai", "rating": 4.3, "location": "Chinatown", "promo": "15% off with SCB"},
        {"name": "Pasta Haven", "cuisine": "Italian", "rating": 4.7, "location": "City Center", "promo": "Buy 1 Get 1 Free with KBank"},
        {"name": "Burger Bliss", "cuisine": "American", "rating": 4.6, "location": "Mall Area", "promo": "5% cashback with Citi"}
    ]

def main():
    st.title("🍽️ Restaurant Search Results")

# Load Data
    df = pd.DataFrame(load_data())

# Search Bar
    search_query = st.text_input("Search for a restaurant or cuisine:")

# Filter results
    if search_query:
        filtered_df = df[df.apply(lambda row: search_query.lower() in row.to_string().lower(), axis=1)]
    else:
        filtered_df = df

    # Display results
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            with st.container():
                st.subheader(row["name"])
                st.write(f"**Cuisine:** {row['cuisine']}")
                st.write(f"**Rating:** ⭐ {row['rating']}")
                st.write(f"**Location:** {row['location']}")
                st.write(f"**Promo:** 🎉 {row['promo']}")
                st.markdown("---")
    else:
        st.warning("No results found. Try a different search.")

if __name__ == "__main__":
    main()