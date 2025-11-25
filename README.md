# README

## Prerequisites
- Python 3.8+ and pip
- Node.js and npm (or yarn)
- Optional: Angular CLI (ng) for convenience

---

## Backend (./backend)
1. Create and activate virtualenv
    - macOS / Linux
      ```
      python3 -m venv venv
      source venv/bin/activate
      ```
    - Windows (PowerShell)
      ```
      python -m venv venv
      .\venv\Scripts\Activate.ps1
      ```

2. Install Python dependencies
    ```
    pip install -r backend/requirements.txt
    ```

3. (Optional) Database migrations (Flask-Migrate)
    - Ensure FLASK_APP is set to your app entry (example: backend/app.py or backend/run.py)
      ```
      # macOS / Linux
      export FLASK_APP=backend/app.py
      export FLASK_ENV=development
      # Windows (cmd)
      set FLASK_APP=backend\app.py
      set FLASK_ENV=development
      ```
    - Run migrations
      ```
      flask db init     # only once
      flask db migrate -m "message"
      flask db upgrade
      ```

4. Run the Flask server
    ```
    # from repository root
    cd backend
    flask run --host=0.0.0.0 --port=5000
    ```
    Or explicitly:
    ```
    python -m flask run --host=0.0.0.0 --port=5000
    ```

---

## Frontend (./frontend)
1. Install dependencies
    ```
    cd frontend
    npm install
    ```

2. Start dev server
    ```
    # using npm script that calls ng serve
    npm start

    # or directly with Angular CLI
    ng serve --open --port 4200
    ```
    Frontend dev server default: http://localhost:4200

---

## Notes on endpoints
- Backend base URL (dev): http://localhost:5000
- Common API base: http://localhost:5000/api (check your routes)
- To discover routes:
  - Search backend for @app.route or @bp.route decorators
  - Check files in backend/ (look for blueprints, route modules)

Example:
- GET http://localhost:5000/api/items
- POST http://localhost:5000/api/auth/login
(Replace with actual routes defined in your backend)

---

## Where to find frontend code
- Angular app root: frontend/src/app
  - Components: folders/files ending in `.component.ts` (e.g., src/app/components/...)
  - Services: files ending in `.service.ts` (e.g., src/app/services/...)
- Update service base URLs to point to the backend dev server (e.g., http://localhost:5000 or http://localhost:5000/api)

---

If the project layout differs, substitute the actual backend/frontend folder names and the Flask entry point file when running commands.