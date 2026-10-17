import httpx


def example_response(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"host": "db01", "disk_pct": 73})


transport = httpx.MockTransport(example_response)
with httpx.Client(transport=transport, timeout=10.0) as client:
    response = client.get("https://example.org/hosts/db01")
    response.raise_for_status()
    print(response.json())  # {'host': 'db01', 'disk_pct': 73}
