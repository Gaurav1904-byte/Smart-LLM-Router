def needs_escalation(response: str) -> bool:
    words = response.split()

    if len(words) < 25:
        return True

    if "Explain" in response[:15]:
        return True

    if response.strip().endswith("recommendations"):
        return True

    return False