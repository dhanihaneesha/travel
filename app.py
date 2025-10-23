from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# sample data for travel destinations
DESTINATIONS = [
    {"id": 1, "name": "Paris", "country": "France", "rating": 4.9,
     "summary": "City of lights and romance."},
    {"id": 2, "name": "Tokyo", "country": "Japan", "rating": 4.8,
     "summary": "High-tech city with rich tradition."},
    {"id": 3, "name": "Bali", "country": "Indonesia", "rating": 4.9,
     "summary": "Tropical beaches and rice terraces."},
    {"id": 4, "name": "New York", "country": "USA", "rating": 4.7,
     "summary": "The Big Apple — museums, food, nightlife."}
]

@app.route('/')
def index():
    """Homepage: list of destinations and search form"""
    q = request.args.get('q', '').lower()
    if q:
        filtered = [d for d in DESTINATIONS if q in d['name'].lower() or q in d['country'].lower()]
    else:
        filtered = DESTINATIONS
    return render_template('index.html', destinations=filtered, query=q)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/api/destinations')
def api_list():
    return jsonify(DESTINATIONS)

@app.route('/api/destinations/<int:id>')
def api_get(id):
    d = next((x for x in DESTINATIONS if x['id']==id), None)
    if not d:
        return jsonify({"error": "not found"}), 404
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
