# Auto_Diet

## Project Overview
https://user-images.githubusercontent.com/69214737/224438919-7af39a7b-c4a8-47f8-8db4-c92c849b7020.mp4

**Auto_Diet** is a Django-based web application designed to process user-submitted dietary data, specifically fecal samples, and generate microbiome abundance reports using external bioinformatics tools (Kraken2 and Bracken). The application provides a user-friendly interface for data submission and result visualization.

## Features

- **User Form:** Collects user details (name, age, gender, mobile, email) and a fecal sample file upload.
- **Automated Analysis:** Integrates with Kraken2 and Bracken (via `toolchest_client`) to process the uploaded sample and generate abundance reports.
- **Result Visualization:** Displays processed results to the user.
- **Admin Interface:** Standard Django admin for managing submissions.
- **Media Handling:** Stores uploaded files and results in a dedicated media directory.

## Project Structure

- `Auto_Diet/` – Django project settings and configuration.
- `Tool/` – Main Django app:
  - `models.py` – User and sample data model.
  - `forms.py` – User input form.
  - `views.py` – Web views for home, form, and results.
  - `templates/html_files/` – HTML templates for UI.
  - `urls.py` – App-specific URL routes.
- `Main/` – Data processing scripts:
  - `main.py` – Orchestrates Kraken2/Bracken analysis and CSV conversion.
  - `ReadBracken.py` – Converts Bracken output to CSV.
- `db.sqlite3` – Default database (though settings use PostgreSQL).
- `PATH.txt` – Tracks uploaded file paths for processing.
- `static/` – Static files (CSS, JS, images).

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Auto_Diet
   ```

2. **Install dependencies:**
   - Python 3.8+
   - Django 4.1+
   - pandas
   - toolchest_client
   - django_bootstrap5
   - psycopg2 (for PostgreSQL)

   Create a `requirements.txt` with:
   ```
   Django>=4.1
   pandas
   toolchest_client
   django_bootstrap5
   psycopg2
   ```

   Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   - Update `Auto_Diet/settings.py` with your PostgreSQL credentials.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the app:**
   - Visit `http://127.0.0.1:8000/` in your browser.

## Usage

1. **Home Page:** Overview and navigation.
2. **Submit Form:** Enter user details and upload a fecal sample.
3. **Processing:** The backend runs Kraken2/Bracken and converts results to CSV.
4. **Results:** View the abundance report.

## Media & Static Files

- Uploaded files are stored in `media/`.
- Static files are in `static/`.

## Screenshots

![Home](https://user-images.githubusercontent.com/69214737/222288773-77b2ed8e-d8f7-4f91-8151-6e7f95301885.png)

![user form](https://user-images.githubusercontent.com/69214737/223489142-391fcf7a-eea6-471d-bcbf-fb272e9bea25.png)

![results](https://user-images.githubusercontent.com/69214737/223489158-bea52181-9021-4c62-b44a-51ac68088bd3.png)

## Notes

- Ensure Kraken2/Bracken databases are accessible if running analysis locally.
- The project is set to use PostgreSQL by default; you can switch to SQLite for testing.
- The `toolchest_client` API key is hardcoded in `main.py`—replace with your own for production.
