

# Number Classifier API

This is a public API built with FastAPI that provides basic classification of numbers along with fetching fun facts.

### Setup Instructions

- **Clone the repository**
  ```bash
  git clone https://github.com/Malik001-G/Number-Classifier-API
  ```

- **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

- **Run the application**
  ```bash
  uvicorn app:app --reload
  ```

## API Documentation
- [API Docs](https://numclassifyapi.vercel.app/docs)

### Endpoint

- **URL**: `https://numclassifyapi.vercel.app/api/classify-number`
- **Method**: `GET`



### Back link 
- https://hng.tech/hire/python-developers

### Request Example

To classify a number, use this URL format:

```bash
GET /api/classify-number?number=28
```

### Response Format

```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["perfect", "even"],
  "digit_sum": 10,
  "fun_fact": "28 is a perfect number."
}
```

#### Error Response (Invalid Input)

If an invalid value is provided for the number, the API will return a 400 status code with a custom error message:

```json
{
  "number": "alphabet",
  "error": true
}
