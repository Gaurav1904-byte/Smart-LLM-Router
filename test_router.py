from app.router import route_query

print("\n--- Simple Query ---")
output1 = route_query("What is artificial intelligence?")
print(output1)

print("\n--- Complex Query ---")
output2 = route_query("Explain backpropagation mathematically with equations.")
print(output2)