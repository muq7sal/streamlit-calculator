import streamlit as st
import math

# --- Page Configuration ---
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# --- Hide Streamlit UI Elements (Sidebar, Menu, Footer) ---
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- Light Theme + One-Line Display CSS ---
st.markdown("""
<style>
.calculator-container {
    max-width: 380px;
    margin: auto;
    background: #f9f9f9;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', sans-serif;
}
.display {
    background: #ffffff;
    border: 1px solid #ddd;
    padding: 10px 15px;
    border-radius: 10px;
    text-align: right;
    font-size: 26px;
    font-weight: 600;
    margin-bottom: 10px;
    color: #222;
    white-space: nowrap;
    overflow-x: auto;
    overflow-y: hidden;
    height: 55px;
}
.stButton>button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 10px;
    background: #e0e0e0;
    color: #111;
    font-size: 20px;
    transition: 0.2s;
    font-weight: 500;
}
.stButton>button:hover {
    background: #d6d6d6;
}
.equals-btn>button {
    background: #4CAF50;
    color: white;
}
.clear-btn>button {
    background: #e53935;
    color: white;
}
.func-btn>button {
    background: #1976D2;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h2 style='text-align:center; color:#333;'>🧮 Scientific Calculator</h2>", unsafe_allow_html=True)

# --- Session State ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Calculator Container ---
st.markdown("<div class='calculator-container'>", unsafe_allow_html=True)

# --- Display Screen (One Line Only) ---
st.markdown(f"<div class='display'>{st.session_state.expression}</div>", unsafe_allow_html=True)

# --- Button Layout ---
buttons = [
    ["7", "8", "9", "/", "sqrt"],
    ["4", "5", "6", "*", "pow"],
    ["1", "2", "3", "-", "log"],
    ["0", ".", "=", "+", "C"],
    ["sin", "cos", "tan"]
]

# --- Button Actions ---
for row in buttons:
    cols = st.columns(len(row))
    for i, char in enumerate(row):
        btn_class = ""
        if char in ["sin", "cos", "tan", "log", "sqrt", "pow"]:
            btn_class = "func-btn"
        elif char == "=":
            btn_class = "equals-btn"
        elif char == "C":
            btn_class = "clear-btn"

        if cols[i].button(char, key=f"{char}_{i}", use_container_width=True):
            if char == "C":
                st.session_state.expression = ""
            elif char == "=":
                try:
                    expr = st.session_state.expression
                    expr = expr.replace("sqrt", "math.sqrt")
                    expr = expr.replace("sin", "math.sin")
                    expr = expr.replace("cos", "math.cos")
                    expr = expr.replace("tan", "math.tan")
                    expr = expr.replace("log", "math.log10")
                    expr = expr.replace("pow", "math.pow")
                    st.session_state.expression = str(eval(expr))
                except Exception:
                    st.session_state.expression = "Error"
            else:
                st.session_state.expression += char

st.markdown("</div>", unsafe_allow_html=True)




