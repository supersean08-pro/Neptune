# Converting Neptune Console App to a Flask Web App

This guide will help you turn your console-based Neptune program into a beginner-friendly Flask web application, following your project roadmap.

---

## Step-by-Step Outline: Making a Basic Flask App

### 1. Set Up Your Environment
- **Install Flask:**  
  Open a terminal and run:
  ```
  pip install flask
  ```
- **Create Project Structure:**  
  Organize your files like this:
  ```
  Neptune-main/
    Neptune-main/
      app.py
      templates/
        (your HTML files will go here)
      static/
        (your CSS/JS files will go here)
  ```

### 2. Create a Basic Flask App
- **app.py:**  
  Start with a minimal Flask app:
  ```python
  from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')
  def home():
      return render_template('index.html')

  if __name__ == '__main__':
      app.run(debug=True)
  ```
- **templates/index.html:**  
  Create a simple HTML file:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>Neptune Experience</title>
  </head>
  <body>
      <h1>Welcome to Neptune!</h1>
  </body>
  </html>
  ```
- **Test:**  
  Run `python app.py` and visit `http://127.0.0.1:5000/` in your browser to see your page.

### 3. Convert Features to Flask Routes
- For each feature in your console app (view descriptions, weight calculator, Neptune feeling), create a new route and corresponding HTML template.
  - Example:
    ```python
    @app.route('/weight')
    def weight():
        return render_template('weight.html')
    ```
- Move the logic from your Python functions into the Flask route handlers, using forms to collect user input.

### 4. Build HTML Templates with Jinja
- Use Jinja templating in your HTML to display dynamic content (e.g., show results after a user submits a form).
- Example:
  ```html
  <form method="post">
      <input type="number" name="mass" placeholder="Enter your mass in kg">
      <button type="submit">Calculate</button>
  </form>
  {% if weight %}
      <p>Your weight on Neptune: {{ weight }} N</p>
  {% endif %}
  ```

### 5. Add Static Files (CSS/JS)
- Place your CSS and JavaScript files in the `static/` folder.
- Link them in your HTML using:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```

### 6. Test and Refine
- Try each feature in your browser.
- Make sure navigation works and results display as expected.

### 7. Update Documentation
- Add instructions to your README on how to run the Flask app.

---

**Tip:**  
Start simple! Get the main menu and one feature working in Flask before moving everything else. If you need a code example for any specific step, just ask!
