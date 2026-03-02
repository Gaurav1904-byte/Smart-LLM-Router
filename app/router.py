from app.complexity import estimate_complexity
from app.models import run_small, run_large
from app.fallback import needs_escalation
from app.cost import log_query
from app.config import LOG_FILE

import logging
import re
from datetime import datetime

# ----------------------------
# Logging Configuration
# ----------------------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

THRESHOLD = 0.5  # Increased threshold to reduce unnecessary large model usage


# ----------------------------
# Tool: Simple Calculator
# ----------------------------
def is_simple_math(query: str) -> bool:
    pattern = r"^\s*\d+\s*[\+\-\*/]\s*\d+\s*$"
    return bool(re.match(pattern, query.strip()))


def safe_calculate(query: str) -> str:
    try:
        return str(eval(query))
    except:
        return "Invalid mathematical expression."


# ----------------------------
# Main Routing Function
# ----------------------------
def route_query(query: str):

    # -----------------------------------
    # 1️⃣ Deterministic Tool Override
    # -----------------------------------
    if is_simple_math(query):
        result_value = safe_calculate(query)

        print("\n==============================")
        print(f"Time: {datetime.now()}")
        print(f"Query: {query}")
        print("Model Used: calculator")
        print("Latency: 0.00 sec")
        print("==============================\n")

        logging.info(
            f"Query='{query}' | Model=calculator | Latency=0.00s"
        )

        log_query({
            "query": query,
            "complexity_score": 0.0,
            "model_used": "calculator",
            "latency": 0.0
        })

        return {
            "query": query,
            "complexity_score": 0.0,
            "model_used": "calculator",
            "response": result_value,
            "latency": 0.0
        }

    # -----------------------------------
    # 2️⃣ Complexity Estimation
    # -----------------------------------
    complexity_score = estimate_complexity(query)

    # -----------------------------------
    # 3️⃣ Initial Routing
    # -----------------------------------
    if complexity_score < THRESHOLD:
        model_used = "small"
        result = run_small(query)

        # -----------------------------------
        # 4️⃣ Fallback Escalation
        # -----------------------------------
        if needs_escalation(result["response"]):
            model_used = "large (fallback)"
            result = run_large(query)

    else:
        model_used = "large"
        result = run_large(query)

    # -----------------------------------
    # 5️⃣ Console Log (Readable)
    # -----------------------------------
    print("\n==============================")
    print(f"Time: {datetime.now()}")
    print(f"Query: {query}")
    print(f"Complexity Score: {complexity_score:.3f}")
    print(f"Model Used: {model_used}")
    print(f"Latency: {result['latency']:.2f} sec")
    print("==============================\n")

    # -----------------------------------
    # 6️⃣ File Log
    # -----------------------------------
    logging.info(
        f"Query='{query}' | "
        f"Complexity={complexity_score:.3f} | "
        f"Model={model_used} | "
        f"Latency={result['latency']:.2f}s"
    )

    # -----------------------------------
    # 7️⃣ Database Log
    # -----------------------------------
    log_query({
        "query": query,
        "complexity_score": complexity_score,
        "model_used": model_used,
        "latency": result["latency"]
    })

    # -----------------------------------
    # 8️⃣ Final Response
    # -----------------------------------
    return {
        "query": query,
        "complexity_score": complexity_score,
        "model_used": model_used,
        "response": result["response"],
        "latency": result["latency"]
    }