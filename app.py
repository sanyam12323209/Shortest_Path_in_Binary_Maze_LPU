# pathfinding_server.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from collections import deque
import time

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

class PathfindingAlgorithm:
    def __init__(self):
        self.directions = [
            [0, 1], [1, 0], [1, 1], [-1, 0], 
            [0, -1], [-1, -1], [-1, 1], [1, -1]
        ]
    
    def bfs_pathfinding(self, grid, start, end):
        """
        BFS pathfinding algorithm that returns step-by-step exploration
        """
        n = len(grid)
        if not grid or not grid[0]:
            return {"success": False, "message": "Invalid grid"}
        
        si, sj = start
        ei, ej = end
        
        # Check if start or end is blocked
        if grid[si][sj] == 1 or grid[ei][ej] == 1:
            return {"success": False, "message": "Start or end is blocked"}
        
        # Initialize BFS
        queue = deque([(si, sj, 1)])
        visited = [[False] * n for _ in range(n)]
        visited[si][sj] = True
        parent = [[None] * n for _ in range(n)]
        
        # Store exploration steps for animation
        exploration_steps = []
        cells_explored = 0
        
        while queue:
            i, j, length = queue.popleft()
            cells_explored += 1
            
            # Add current cell to exploration steps (except start)
            if not (i == si and j == sj):
                exploration_steps.append({"row": i, "col": j, "step": cells_explored})
            
            # Check if we reached the end
            if i == ei and j == ej:
                # Reconstruct path
                path = []
                ci, cj = ei, ej
                while ci != si or cj != sj:
                    if not (ci == ei and cj == ej):  # Don't include end in path highlighting
                        path.append({"row": ci, "col": cj})
                    ci, cj = parent[ci][cj]
                
                path.reverse()  # Reverse to get path from start to end
                
                return {
                    "success": True,
                    "path_length": length,
                    "cells_explored": cells_explored,
                    "exploration_steps": exploration_steps,
                    "final_path": path,
                    "message": "Path found successfully!"
                }
            
            # Explore neighbors
            for dx, dy in self.directions:
                ni, nj = i + dx, j + dy
                
                if (0 <= ni < n and 0 <= nj < n and 
                    not visited[ni][nj] and grid[ni][nj] == 0):
                    
                    queue.append((ni, nj, length + 1))
                    visited[ni][nj] = True
                    parent[ni][nj] = (i, j)
        
        return {
            "success": False,
            "message": "No path found",
            "cells_explored": cells_explored,
            "exploration_steps": exploration_steps
        }

# Initialize pathfinding algorithm
pathfinder = PathfindingAlgorithm()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/find_path', methods=['POST'])
def find_path():
    """API endpoint for pathfinding"""
    try:
        data = request.json
        grid = data.get('grid')
        start = data.get('start')
        end = data.get('end')
        
        if not grid or not start or not end:
            return jsonify({"success": False, "message": "Missing required data"})
        
        # Record start time
        start_time = time.time()
        
        # Run pathfinding algorithm
        result = pathfinder.bfs_pathfinding(grid, start, end)
        
        # Add execution time
        result['execution_time'] = round(time.time() - start_time, 4)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"})

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Python backend is running!"})

if __name__ == '__main__':
    import os
    print("🚀 Starting Pathfinding Server...")
    print("📍 Server will run on: http://localhost:5000")
    print("🔧 Make sure to install requirements: pip install flask flask-cors")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)