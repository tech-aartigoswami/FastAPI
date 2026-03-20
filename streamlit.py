import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("User Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Create User", "Get All Users", "Get User By ID", "Update User", "Delete User"]
)

# ---------------- CREATE USER ---------------- #

if menu == "Create User":

    st.subheader("Create User")

    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1)

    if st.button("Create User"):

        payload = {
            "name": name,
            "email": email,
            "age": age
        }

        response = requests.post(f"{BASE_URL}/create-user", json=payload)

        if response.status_code == 200:
            st.success("User Created Successfully")
            st.json(response.json())
        else:
            st.error("Error creating user")


# ---------------- GET ALL USERS ---------------- #

elif menu == "Get All Users":

    st.subheader("All Users")

    if st.button("Fetch Users"):

        response = requests.get(f"{BASE_URL}/get-all-users")

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error fetching users")


# ---------------- GET USER BY ID ---------------- #

elif menu == "Get User By ID":

    st.subheader("Get User By ID")

    user_id = st.number_input("User ID", min_value=1)

    if st.button("Fetch User"):

        response = requests.get(f"{BASE_URL}/get-users-by-id/{user_id}")

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("User not found")


# ---------------- UPDATE USER ---------------- #

elif menu == "Update User":

    st.subheader("Update User")

    user_id = st.number_input("User ID", min_value=1)

    name = st.text_input("New Name")
    email = st.text_input("New Email")
    age = st.number_input("New Age", min_value=1)

    if st.button("Update User"):

        payload = {
            "name": name,
            "email": email,
            "age": age
        }

        response = requests.put(f"{BASE_URL}/update-user/{user_id}", json=payload)

        if response.status_code == 200:
            st.success("User Updated Successfully")
            st.json(response.json())
        else:
            st.error("Error updating user")


# ---------------- DELETE USER ---------------- #

elif menu == "Delete User":

    st.subheader("Delete User")

    user_id = st.number_input("User ID", min_value=1)

    if st.button("Delete User"):

        response = requests.delete(f"{BASE_URL}/delete-users-by-id/{user_id}")

        if response.status_code == 200:
            st.success("User Deleted Successfully")
        else:
            st.error("Error deleting user")