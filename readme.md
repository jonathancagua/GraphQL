# GraphQL API with FastAPI and Strawberry

This project demonstrates a simple **GraphQL API** using **FastAPI** and **Strawberry**, modeling a basic library of books and authors.

## Project Structure

```
python-graphql-fastapi/
├── main.py         # FastAPI app with GraphQL endpoint
├── schema.py       # GraphQL schema (Query & Mutation)
└── models.py       # Mock data for books and authors
```

## How to Run

1. **Install dependencies**:

```bash
pip install fastapi uvicorn strawberry-graphql
```

2. **Run the server**:

```bash
uvicorn main:app --reload
```

3. **Open GraphiQL in browser**:

```
http://localhost:8000/graphql
```

Use the GraphiQL interface to run queries and mutations.

### Example Query

```graphql
query {
  books {
    id
    title
    author {
      name
    }
  }
}
```

### Example Mutation

```graphql
mutation {
  createBook(title: "The Silmarillion", authorId: 2) {
    id
    title
    author {
      name
    }
  }
}
```

---

## How to Make a POST Request (Python Example)

You can interact with the API using a `POST` request:

```python
import requests

query = """
query {
  books {
    id
    title
    author {
      name
    }
  }
}
"""

response = requests.post("http://localhost:8000/graphql", json={"query": query})
print(response.json())
```

### Example Response

```json
{
  "data": {
    "books": [
      {
        "id": 1,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": {
          "name": "J.K. Rowling"
        }
      }
    ]
  }
}
```

