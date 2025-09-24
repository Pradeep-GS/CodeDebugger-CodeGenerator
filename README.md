# Code Debugger AI

A web application to debug code using OpenAI API. Users can input code in multiple programming languages and give corrected code. 
Built with **Python Flask backend** and **React frontend** using **TailwindCSS**.

---

## Features
- Detect syntax, runtime, and logical errors
- Output corrected code
- Modern UI with TailwindCSS

---

## Prerequisites
- Python 3.8+
- Node.js 18+ and npm
- OpenAI API key

---

## Setup Instructions

### Backend (Flask + OpenAI API)
1. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```
2. Install dependencies:
```bash
pip install flask flask-cors openai python-dotenv
```
3. Create a `.env` file in the backend directory with your OpenAI API key:
```
API_KEY=sk-your_openai_api_key_here
```
4. Run the backend server:
```bash
python server.py
```
The backend will run at `http://127.0.0.1:5000`.

### Frontend (React + TailwindCSS)
1. Go to the frontend folder:
```bash
cd frontend
```
2. Install dependencies:
```bash
npm install
```
3. Install TailwindCSS and initialize:
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```
4. Configure `tailwind.config.js`:
```javascript
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: { extend: {} },
  plugins: [],
}
```
5. Add Tailwind directives to `src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```
6. Start the React development server:
```bash
npm start
```
The frontend will run at `http://localhost:3000`.

---

## Usage
- Open the frontend in your browser.
- Paste your code and select the programming language.
- Click **Debug** to get explanation and fixed code in structured JSON format.
