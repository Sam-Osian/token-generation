import streamlit as st
import time
import random

# Define model speeds (Tokens Per Second)
model_speeds = {
    "LLaMA 7B (Q4)": 25,
    "LLaMA 13B (Q4)": 15,
    "LLaMA 32B (QLoRA)": 10,
    "LLaMA 70B (Q8)": 3
}

# Sample output
sample_output = [
    "Sam", "and", "John", "met", "by", "the", "kitchen", "door", ".",
    "Morning", ",", "said", "Sam", ".", "John", "morninged", "back", ".",
    "They", "turned", "to", "Dave", ".", "What", "are", "you", "having", "for", "tea", "?",
    "Biryani", "!", "he", "replied", "with", "a", "grin", ".",
    "Hee", ",", "heeee", "."
]

st.title("💬 Token Generation Speed Simulator")
st.markdown("This app simulates how different LLaMA models stream tokens at various speeds. Choose a model below to see how it might 'talk' in real time.")

# Function to simulate streaming in Streamlit
def simulate_stream(model_name, tps, initial_delay=False):
    if initial_delay:
        time.sleep(0.5)

    stream_placeholder = st.empty()
    full_output = ""

    for i, token in enumerate(sample_output):
        if i > 0 and token not in {".", ",", "!", "?"}:
            full_output += " "
        full_output += token

        stream_placeholder.text_area("Streaming Output", full_output, height=200)

        delay = random.uniform(0.9, 1.1) / tps
        if token in {".", "!", "?"}:
            delay *= 2
        time.sleep(delay)

# Sim buttons for each model
for i, (model_name, tps) in enumerate(model_speeds.items()):
    with st.expander(f"{model_name} — ~{tps} tokens/sec"):
        if st.button(f"Simulate {model_name}", key=f"simulate_{i}"):
            simulate_stream(model_name, tps, initial_delay=True)

# Custom speed simulation
st.markdown("---")
st.subheader("⚙️ Custom Simulation")

custom_tps = st.number_input("Enter custom token generation speed (tokens/sec):", min_value=0.1, max_value=100.0, value=12.0, step=0.5)

if st.button("Simulate Custom Speed"):
    simulate_stream("Custom Model", custom_tps, initial_delay=True)
