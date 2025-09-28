from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# In-memory storage for appointments
appointments = []

# HTML templates with Bootstrap
home_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pediatrician Appointments</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
    <div class="text-center mb-4">
        <h1>Pediatrician Appointment Scheduler</h1>
        <a href="{{ url_for('add_appointment') }}" class="btn btn-primary mt-3">Book Appointment</a>
    </div>
    
    <h3>All Appointments</h3>
    {% if appointments %}
    <table class="table table-striped mt-3">
        <thead class="table-dark">
            <tr>
                <th>Name</th>
                <th>Age (yrs)</th>
                <th>Date</th>
                <th>Time</th>
            </tr>
        </thead>
        <tbody>
        {% for appt in appointments %}
            <tr>
                <td>{{ appt['name'] }}</td>
                <td>{{ appt['age'] }}</td>
                <td>{{ appt['date'] }}</td>
                <td>{{ appt['time'] }}</td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
    {% else %}
        <p class="text-muted">No appointments scheduled yet.</p>
    {% endif %}
</div>
</body>
</html>
"""

add_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Book Appointment</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
    <div class="text-center mb-4">
        <h1>Book Appointment</h1>
    </div>
    <form method="POST" class="card p-4 bg-white shadow-sm">
        <div class="mb-3">
            <label for="name" class="form-label">Child's Name</label>
            <input type="text" class="form-control" id="name" name="name" required>
        </div>
        <div class="mb-3">
            <label for="age" class="form-label">Age (years)</label>
            <input type="number" class="form-control" id="age" name="age" required>
        </div>
        <div class="mb-3">
            <label for="date" class="form-label">Date</label>
            <input type="date" class="form-control" id="date" name="date" required>
        </div>
        <div class="mb-3">
            <label for="time" class="form-label">Time</label>
            <input type="time" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-success">Book Appointment</button>
        <a href="{{ url_for('home') }}" class="btn btn-secondary">Back</a>
    </form>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_page, appointments=appointments)

@app.route('/add', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        appointments.append({
            'name': request.form['name'],
            'age': request.form['age'],
            'date': request.form['date'],
            'time': request.form['time']
        })
        return redirect(url_for('home'))
    return render_template_string(add_page)

if __name__ == '__main__':
    app.run(debug=True)
