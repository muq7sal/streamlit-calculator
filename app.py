import streamlit as st
import math

# --- Page Configuration ---
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# --- Custom CSS for Beautiful UI ---
st.markdown("""
<style>
.calculator-container {
    max-width: 360px;
    margin: auto;
    background: linear-gradient(145deg, #202020, #2c2c2c);
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.6);
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
}
.display {
    background: #111;
    padding: 15px;
    border-radius: 10px;
    text-align: right;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 15px;
    overflow-x: auto;
}
.stButton>button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 12px;
    background: #333;
    color: white;
    font-size: 20px;
    transition: 0.2s;
}
.stButton>button:hover {
    background: #555;
}
.clear-btn>button {
    background: #d32f2f;
}
.equals-btn>button {
    background: #1976d2;
}
.func-btn>button {
    background: #0288d1;
}
</style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h2 style='text-align:center;'>🧮 Scientific Calculator</h2>", unsafe_allow_html=True)

# --- Session State ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Display Screen ---
st.markdown("<div class='calculator-container'>", unsafe_allow_html=True)
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



