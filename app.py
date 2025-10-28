import streamlit as st
import math

# ---- Page Config ----
st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")

# ---- App Title ----
st.title("🧮 Advanced Calculator")
st.caption("A smart calculator built using Streamlit with theme toggle and history log")

# ---- Sidebar Theme Toggle ----
theme = st.sidebar.radio("🌗 Choose Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown(
        """
        <style>
        body {background-color: #111; color: #EEE;}
        .stButton>button {background-color: #222; color: white;}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---- Session State for History ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- Input Fields ----
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number:", value=0.0)
with col2:
    num2 = st.number_input("Enter second number:", value=0.0)

# ---- Operation Selection ----
operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division", "Power (xⁿ)", "Modulus (%)", "Square Root (√x)"]
)

# ---- Calculation Logic ----
result = None
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error (Divide by Zero)"
        elif operation == "Power (xⁿ)":
            result = math.pow(num1, num2)
        elif operation == "Modulus (%)":
            result = num1 % num2 if num2 != 0 else "Error (Divide by Zero)"
        elif operation == "Square Root (√x)":
            result = math.sqrt(num1)
        
        # Save to history
        st.session_state.history.append(f"{operation}: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# ---- Display Result ----
if result is not None:
    st.success(f"✅ Result: {result}")

# ---- History Log ----
st.subheader("🧾 Calculation History")
if len(st.session_state.history) > 0:
    for i, entry in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.write(f"{i}. {entry}")
else:
    st.info("No calculations yet!")

# ---- Clear History ----
if st.button("🧹 Clear History"):
    st.session_state.history.clear()
    st.success("History cleared!")

