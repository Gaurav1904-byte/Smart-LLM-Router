from llama_cpp import Llama
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

print("Loading small model...")
small_model = Llama(
    model_path=os.path.join(MODEL_DIR, "tiny.gguf"),
    n_ctx=1024,
    n_threads=4,
    n_batch=256,
    verbose=False
)
print("Small model loaded.")

print("Loading large model...")
large_model = Llama(
    model_path=os.path.join(MODEL_DIR, "mistral.gguf"),
    n_ctx=1024,
    n_threads=4,
    n_batch=256,
    verbose=False
)
print("Large model loaded.")


def run_small(query: str):
    start = time.time()
    output = small_model(query, max_tokens=100, temperature=0.7)
    latency = time.time() - start
    return {
        "response": output["choices"][0]["text"].strip(),
        "latency": latency
    }


def run_large(query: str):
    start = time.time()
    output = large_model(query, max_tokens=150, temperature=0.7)
    latency = time.time() - start
    return {
        "response": output["choices"][0]["text"].strip(),
        "latency": latency
    }