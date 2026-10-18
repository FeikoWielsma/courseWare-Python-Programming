import httpx


def example_response(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"title": "Imagine", "duration_s": 183})

transport = httpx.MockTransport(example_response)
with httpx.Client(transport=transport, timeout=10.0) as client:
    response = client.get("https://example.org/now-playing")
    response.raise_for_status()
    print(response.json())
