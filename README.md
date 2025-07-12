# 🧠 Shortest Path in Binary Maze – Pathfinding Visualizer 🚀

This project is a full-stack pathfinding visualizer built using:

- 💻 Frontend: HTML, CSS, JavaScript
- 🐍 Backend: Python (Flask)
- ☁️ Deployment: Render

Users can visually experiment with a grid-based maze and watch the Python-powered BFS algorithm in action!

---

## 📸 Features

✅ Interactive Grid (customizable size)  
✅ Set Start & End points by clicking  
✅ Place/remove obstacles  
✅ Animate BFS exploration & shortest path  
✅ View path length, cells explored, and backend execution time  
✅ Responsive design with modern UI/UX  
✅ Live deployment on Render

---

## 🧠 How It Works

- The frontend sends the grid, start & end positions to the Flask backend using a POST API call.
- The backend (Python) runs the Breadth-First Search (BFS) algorithm and returns:
  - Explored cells (for animation)
  - Final path (shortest route)
  - Stats like length, execution time
- The frontend then animates the exploration and final path in real-time.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sanyam12323209/Shortest_Path_in_Binary_Maze_LPU.git
cd Shortest_Path_in_Binary_Maze_LPU
