from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Налаштування розміру сітки
GRID_SIZE = 30
pixels = [["#FFFFFF" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_grid', methods=['GET'])
def get_grid():
    return jsonify(pixels)

@app.route('/update_pixels', methods=['POST'])
def update_pixels():
    data = request.get_json()
    updates = data.get('updates', [])
    
    for update in updates:
        x, y, color = update['x'], update['y'], update['color']
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            pixels[y][x] = color
        else:
            return jsonify({"status": "error", "message": "Invalid coordinates"}), 400 #Помилка
    
    return jsonify({"status": "success"}) #Працює

if __name__ == '__main__':
    app.run(debug=True)