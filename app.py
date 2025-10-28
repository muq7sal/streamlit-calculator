import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Digital Calculator", page_icon="🧮", layout="centered")

st.markdown("""
<style>
.calculator {
    max-width: 300px;
    margin: auto;
    padding: 20px;
    border-radius: 20px;
    background: #1E1E1E;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
    color: white;
}
.display {
    background: #333;
    padding: 15px;
    border-radius: 10px;
    text-align: right;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
    word-wrap: break-word;
}
.button {
    background: #444;
    border: none;
    color: white;
    font-size: 20px;
    width: 100%;
    padding: 15px;
    border-radius: 10px;
    cursor: pointer;
}
.button:hover {
    background: #666;
}
.clear {
    background: #D32F2F;
}
.equals {
    background: #1976D2;
}
</style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("🧮 Digital Calculator")
st.write("A fully interactive calculator built with Streamlit")

# --- Session State for Display ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Display Screen ---
st.markdown(f"<div class='calculator'><div class='display'>{st.session_state.expression}</div>", unsafe_allow_html=True)

# --- Button Layout ---
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# --- Button Logic ---
for row in buttons:
    cols = st.columns(len(row))
    for i, char in enumerate(row):
        if cols[i].button(char, key=f"{char}_{i}", use_container_width=True):
            if char == "C":
                st.session_state.expression = ""
            elif char == "=":
                try:
                    st.session_state.expression = str(eval(st.session_state.expression))
                except Exception:
                    st.session_state.expression = "Error"
            else:
                st.session_state.expression += char

# --- Close Container ---
st.markdown("</div>", unsafe_allow_html=True)


