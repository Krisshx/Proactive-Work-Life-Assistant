# frontend.py

import streamlit as st
import requests

st.title("Proactive Work-Life Assistant")

goal = st.text_input("Enter your goal (e.g., plan a dinner...)")

if st.button("Submit Goal"):
    res = requests.post("http://localhost:8000/goal", json={"goal": goal})
    if res.status_code == 200:
        parsed = res.json()["parsed_details"]
        st.write("Parsed Details:", parsed)

        loc = "Hyderabad"  # Update location based on parsed details
        cuisine = "Hyderabadi biryani"  # Update cuisine based on parsed details
        places = requests.get(f"http://localhost:8000/restaurants?location={loc}&cuisine={cuisine}")

        if places.status_code == 200:
            st.write("Top Restaurants:")
            for restaurant in places.json().get("restaurants", []):
                st.write(f"{restaurant['name']} - {restaurant['address']}")
        else:
            st.write("Error fetching restaurants.")
    else:
        st.write("Error interpreting goal.")
