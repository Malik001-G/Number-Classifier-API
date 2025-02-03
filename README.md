

# Number Classifier API

This is a public API built with FastAPI that provides basic classification of numbers along with fetching fun facts.

### Setup Instructions

- **Clone the repository**
  ```bash
  git clone https://github.com/your-username/Number-Classifier-API
  ```

- **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

- **Run the application**
  ```bash
  uvicorn main:app --reload
  ```

## API Documentation
- [API Docs](https://number-classifier-api.vercel.app/docs)

### Endpoint

- **URL**: `https://number-classifier-api.vercel.app`
- **Method**: `GET`

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
