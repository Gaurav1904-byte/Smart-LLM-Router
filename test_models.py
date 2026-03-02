from app.models import run_small, run_large

print("\nTesting SMALL model:")
small_output = run_small("What is artificial intelligence?")
print(small_output)

print("\nTesting LARGE model:")
large_output = run_large("Explain gradient descent mathematically.")
print(large_output)