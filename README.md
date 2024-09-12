# py-webserver

A basic web server built with python.

## Endpoints

| METHOD | ROUTE              | FUNCTIONALITY                                                         |
| ------ | ------------------ | --------------------------------------------------------------------- |
| GET    | `/`                | 200 HTTP Response                                                     |
| GET    | `/echo/{string}`   | 200 HTTP Response with the string and its length                      |
| GET    | `/files{filename}` | HTTP Response with the file                                           |
| GET    | `/user-agent`      | Reads the user agent header and returns the user-agent and its length |
