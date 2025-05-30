# Python Webserver

A minimal web server implemented in Python, designed to demonstrate basic HTTP request handling and routing.

## Features

- Basic routing with multiple endpoints
- String echoing with length calculation
- File retrieval
- User-Agent header parsing

## Endpoints

| Method | Route               | Description                                                                 |
|--------|---------------------|-----------------------------------------------------------------------------|
| GET    | `/`                 | Returns a `200 OK` HTTP response indicating the server is running.          |
| GET    | `/echo/{string}`    | Returns the input string along with its length.                             |
| GET    | `/files/{filename}` | Serves the requested file if it exists on the server.                       |
| GET    | `/user-agent`       | Returns the value of the `User-Agent` header and its character length.      |

## Requirements

- Python 3.x

## Running the Server

```bash
python server.py
```

The server will start on `http://localhost:4221`.
