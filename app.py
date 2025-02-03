from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import httpx
from sympy import isprime
import async_lru

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Custom exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "number": str(request.query_params.get("number", "alphabet")),
            "error": True
        },
    )

@async_lru.alru_cache(maxsize=100)
async def fetch_fun_fact(n: int) -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://numbersapi.com/{n}/math", timeout=5.0)
            response.raise_for_status()
            return response.text
    except httpx.RequestError:
        return "No fun fact available for this number."

def is_prime(n: int) -> bool:
    return isprime(n)

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

def get_parity(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to analyze")):
    
    is_prime_result, is_perfect_result, is_armstrong_result, digit_sum_result, parity_result, fun_fact_result = await asyncio.gather(
        asyncio.to_thread(is_prime, number),
        asyncio.to_thread(is_perfect, number),
        asyncio.to_thread(is_armstrong, number),
        asyncio.to_thread(digit_sum, number),
        asyncio.to_thread(get_parity, number),
        fetch_fun_fact(number),  
    )

    properties = []
    if is_armstrong_result:
        properties.append("armstrong")
    properties.append(parity_result)

    return {
        "number": number,
        "is_prime": is_prime_result,
        "is_perfect": is_perfect_result,
        "properties": properties,
        "digit_sum": digit_sum_result,
        "fun_fact": fun_fact_result,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)