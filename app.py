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
    st.subheader(f"Streaming from **{model_name}** (~{tps} tokens/sec)")

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


# Generate a button for each model
for i, (model_name, tps) in enumerate(model_speeds.items()):
    with st.expander(f"{model_name} — ~{tps} tokens/sec"):
        st.markdown(f"""
        **Model:** {model_name}  
        **Estimated Token Generation Speed:** ~{tps} tokens per second  
        """)
        if st.button(f"Simulate {model_name}", key=f"simulate_{i}"):
            simulate_stream(model_name, tps, initial_delay=True)
