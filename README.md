# Python Server Monitoring Dashboard

A beginner-friendly Python project that monitors server resource usage and displays health information on a web dashboard.

## Features

- Monitor CPU usage.
- Monitor memory (RAM) usage.
- Monitor disk usage.
- Check server health using configurable thresholds.
- Display health status: HEALTHY or WARNING.
- Store monitoring history in an SQLite database.
- View recent monitoring results in a Flask dashboard.

## Technologies Used

- Python
- Flask
- psutil
- SQLite
- HTML and CSS
- Git and GitHub

## Project Structure

```text
python-server-monitor/
├── app.py
├── monitor.py
├── view_history.py
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    └── dashboard.html
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/python-server-monitor.git
cd python-server-monitor
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## How to Run

### Start server monitoring

```bash
python monitor.py
```

This checks CPU, memory, and disk usage, then saves the results to the SQLite database.

### View monitoring history

```bash
python view_history.py
```

### Start the web dashboard

```bash
python app.py
```

Open this address in your browser:

http://127.0.0.1:5000

## Health Check Thresholds

| Resource | Warning threshold |
|---|---:|
| CPU usage | Above 80% |
| Memory usage | Above 72% |
| Disk usage | Above 81% |

These thresholds can be adjusted in `monitor.py`.

## Future Improvements

- Automatic background monitoring.
- Dashboard auto-refresh.
- Docker containerization.
- CI/CD pipeline integration.
- Deployment to a cloud server.

## Author

Piyarul Sekh

## License

This project is open source and available for learning and educational purposes.