# Stage 1: the Python app

Goal: a working portfolio site served by a small Python API, with tests.

## What was built, file by file

### `app/data.py`: the content
All your text (name, skills, jobs, projects) lives here as plain Python lists and dicts.
**This is the first file to edit.** Replace the placeholders with your real info.

Why separate it? The HTML stays a "template" with empty boxes, and the data comes from the API.
Later you could move this data into a database without touching the page.

### `app/main.py`: the API
FastAPI turns Python functions into web endpoints:

```python
@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
```

`@app.get("/health")` means "when someone requests `GET /health`, run this function and send back what it returns as JSON".

- `/` returns `index.html`.
- `/static/...` serves the CSS and JS files (`app.mount(...)`).
- `/api/...` return the content from `data.py` as JSON.
- `/health` is tiny on purpose. In Stage 4 Kubernetes will call it every few seconds to check the app is alive and restart it if not.

### `app/static/index.html`: the page
Plain HTML with empty containers (`<div id="projects-list">`). No framework, so there is nothing hidden from you.

### `app/static/script.js`: frontend talks to backend
When the page loads, it calls `fetch("/api/projects")` etc., gets JSON back, and builds the cards.
It creates elements with `document.createElement` and `textContent` instead of pasting HTML strings, so text from the API can never inject code into the page (an XSS defence worth mentioning in interviews).
It also calls `/health` and shows the green "online" dot in the "How this site is built" section.

### `app/static/style.css`: the dark neon theme
All colours are variables at the top (`--green`, `--purple`, `--bg`). Change them there and the whole site follows.
The "glow" is just `text-shadow` / `box-shadow` with the same colour, blurred.
The page works on phones (`@media (max-width: 640px)`) and turns animations off for people who ask their OS for reduced motion.

### `tests/test_main.py`: tests
`TestClient` calls the API in memory, no server needed. Each test checks one endpoint returns what we expect.
In Stage 5, GitHub Actions will run these on every push and refuse to deploy if one fails.

### `requirements.txt` vs `requirements-dev.txt`
`requirements.txt` is what the app needs to **run** (goes into the Docker image in Stage 2).
`requirements-dev.txt` adds what you need to **develop** (pytest). Keeping them separate keeps the production image small.

## Try it on your server

```bash
sudo apt install -y python3-venv          # once
cd portfolio
python3 -m venv .venv                      # an isolated Python just for this project
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest                                     # should say 4 passed
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

From your PC, open `http://<server-ip>:8000`. Find the IP with `ip a` on the server.
If it does not load, the firewall may block the port: `sudo ufw allow 8000/tcp` (only if `ufw status` says active).
Stop the server with `Ctrl+C`.

Also open `http://<server-ip>:8000/docs`: FastAPI generates interactive API documentation for free.

## Exercises (do these yourself, then commit)
1. Put your real name, title, jobs and links in `app/data.py`.
2. Add a new endpoint `GET /api/certifications` and a test for it.
3. Change `--purple` in `style.css` to another colour and see the whole site change.
4. Break a test on purpose (change `"ok"` to `"okay"` in `main.py`), run `pytest`, read the error, fix it.

## How to commit it to GitHub
```bash
git init
git add .
git commit -m "feat: portfolio site with FastAPI backend"
git branch -M main
git remote add origin git@github.com:<your-username>/portfolio.git
git push -u origin main
```

## Interview questions this stage prepares you for
- What is the difference between the frontend and the backend here?
- What is a REST endpoint? What does `GET` mean?
- Why have a `/health` endpoint?
- Why use a virtual environment?
- How do you stop user content from injecting scripts into a page?

**Next: Stage 2, put this app in a Docker container.**
