# ColdReach SaaS Email Engine 🚀

ColdReach is a high-performance, local Python automation engine that eliminates generic email spam by dynamically parsing structured prospect data into hyper-personalized outreach copy instantly.

## 🛠️ Features
* **100% Local Execution:** Runs completely on your local hardware to protect sensitive client lead data.
* **Robust File Handling:** Utilizes `pathlib` for cross-platform directory resolution and `csv.DictReader` for data mapping.
* **Sleek CLI:** Built-in ANSI terminal rendering with real-time batch deployment tracking.

## 🚀 Tech Stack
* Python 3 (`csv`, `time`, `pathlib`)

## ⚙️ Quick Start
1. Add placeholders (e.g., `{name}`) to `template.txt`.
2. Populate your target leads in `prospects.csv`.
3. Run the engine:
   ```bash
   python generator.py
