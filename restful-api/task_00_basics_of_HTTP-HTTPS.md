# Basics of HTTP/HTTPS

## 1. Differentiating HTTP and HTTPS

### What's a protocol?

A **protocol** is a set of rules that explain:
- How to formulate a message
- In what order to send it
- How the other party should respond
- And how to interpret the response

Without a protocol, two machines cannot “understand” each other.

---
### HTTP

HTTP is the protocol used to **exchange data on the web**.

**HTTP** stands for **HyperText Transfer Protocol**:
- **HyperText**: originally, the web mainly carried linked text documents (web pages)
- **Transfer**: data is transferred from one point to another
- **Protocol**: communication rules

HTTP is used on the internet to allow clients and servers to exchange data:
- **send a request** from the client to the server (request)
- and **receive an answer** (response)

However, HTTP messages are transmitted in plain text over the network.

Therefore, anyone who intercepts them can read:
- The requested URL
- The data being transmitted (including API calls)...

And sometimes, even sensitive information such as:
- Passwords
- Personal data...

**In a nutshell, with HTTP:**
`client → readable message → server`

---

### *Capture of an HTTP request with Wireshark*
![HTTP capture](images/http.png)

---
### HTTPS

HTTPS works in the same way as HTTP, but with an additional layer of security via the TLS protocol (formerly SSL).

**HTTPS = HTTP + TLS**

This provides three essential features:
- **Encryption**: content cannot be read if intercepted (cannot be read without the decryption keys)
- **Integrity**: data cannot be modified discreetly in transit (without being detected)
- **Authentication**: the browser verifies that it is communicating with the correct server (this verification is based on a digital certificate)

Adding a security protocol to HTTP ensures that the data transmitted is protected, that it is not directed to a fake site, and that it cannot be modified during transport without being detected.
HTTPS protects transport, not the overall security of the site.

**In a nutshell, with HTTPS:**
`client → encrypted message → server`

---

### *Capture of an HTTPS request with Wireshark*
![HTTPS capture](images/https.png)

---

## 2. Depiction of the structure of an HTTP request and response

### HTTP request structure
- Method
- Path
- HTTP version
- Headers
- Optional body

Example request:
```
GET /users HTTP/1.1
Host: example.com
```

---

### HTTP response structure
- HTTP version
- Status code
- Headers
- Optional body

Example response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```

---

## 3. Common HTTP methods and status codes

### 3.1. Main HTTP methods

**GET - Retrieve data**

Retrieves a resource without modifying it.

Example:
- `GET /users` → returns the list of users
- `GET /users/12` → returns user with ID 12

Typical use case: fetching data from an API or loading a web page.

---

**POST - Create a resource**

Sends data to create a new resource.

Example:
```
POST /users
{"name": "Alice"}
```
→ creates a new user.

Expected effect:
- A new resource is created.
- The server often returns 201 Created.

Typical use case: creating a new user, order, or database entry.

---

**PUT - Replace a resource (full update)**

Replaces an existing resource entirely.

In practice, many APIs use PUT similarly to PATCH, but in theory PUT replaces the whole resource.

Example:
```
PUT /users/12
{"name": "Alice", "age": 30}
```
→ replaces the existing user data.

Typical use case: replacing all data of an existing resource.

---

**PATCH - Partial update**

Updates only part of an existing resource.

Example:
```
PATCH /users/12
{"age": 31}
```
→ modifies only one field.

Typical use case: updating a specific attribute of a resource.

---

**DELETE - Remove a resource**

Deletes a resource completely.

Example:
- `DELETE /users/12` → removes the user.

Typical use case: deleting an entry or resource.

---

### 3.2. Main HTTP status codes

**Purpose of status codes**

When a client (browser, application, Python script, etc.) sends a request to a server or API, the server always responds with an HTTP status code.

This code summarizes what happened, even before reading the response body.

Without status codes, the client would not know:
- if the request succeeded,
- if the resource does not exist,
- if authentication is required,
- if the server failed,
- or if the request should be retried later.

Status codes allow:
- browsers to display correct messages,
- applications to react properly,
- scripts to handle errors,
- APIs to communicate their state clearly.

---

**Structure of an HTTP status code**

An HTTP status code contains three digits and conveys a message.

Examples:
- 200 OK
- 404 Not Found
- 500 Internal Server Error

The first digit indicates the category of the response.

---

**Success responses (2xx)**

| Code | Message    | Meaning                                   |
| ---- | ---------- | ----------------------------------------- |
| 200  | OK         | The request succeeded                     |
| 201  | Created    | A new resource was successfully created   |
| 204  | No Content | Request succeeded but nothing is returned |


---

**Redirection responses (3xx)**

| Code | Message           | Meaning                                            |
| ---- | ----------------- | -------------------------------------------------- |
| 301  | Moved Permanently | Resource has permanently moved                     |
| 302  | Found             | Resource temporarily available at another location |
Browsers usually follow the new location automatically.

---

**Client error responses (4xx)**

| Code | Message           | Meaning                              |
| ---- | ----------------- | ------------------------------------ |
| 400  | Bad Request       | Request is malformed or invalid      |
| 401  | Unauthorized      | Authentication is required or failed |
| 403  | Forbidden         | Access is denied                     |
| 404  | Not Found         | Resource does not exist              |
| 429  | Too Many Requests | Client sent too many requests        |

---

**Server error responses (5xx)**

| Code | Message               | Meaning                               |
| ---- | --------------------- | ------------------------------------- |
| 500  | Internal Server Error | Generic server error                  |
| 502  | Bad Gateway           | Invalid response from upstream server |
| 503  | Service Unavailable   | Server temporarily unavailable        |
| 504  | Gateway Timeout       | Server response took too long         |
