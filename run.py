from app.router import route_query

if __name__ == "__main__":
    query = input("Enter your query: ")
    result = route_query(query)
    print(result)