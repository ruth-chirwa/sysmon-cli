# sysmon-cli

A **real-time system monitoring CLI tool** that provides insights into your computer’s performance and resource usage. Track CPU, memory, disk, network, GPU, processes, and more directly from your terminal.

---

## Features

- **CPU Usage**
  - Real-time CPU usage monitoring.
  - Per-core breakdown.
  
- **Memory (RAM) Usage**
  - Total, used, and available memory.
  - Highlights top memory-consuming processes.

- **Disk Usage**
  - Monitors read/write speeds and storage usage.
  - Shows disk usage per process.

- **Network Activity**
  - Tracks upload/download speeds.
  - Shows active connections and bandwidth consumption.

- **Processes**
  - Lists all running applications and background tasks.
  - Shows per-process CPU and memory usage.

- **GPU Usage** *(optional)*
  - Monitors graphics load.
  - Useful for gaming, rendering, or AI workloads.

- **System Temperature & Hardware Health**
  - Monitors CPU/GPU temperatures.
  - Tracks fan speeds and battery health.

- **Performance Graphs**
  - Visual charts in the terminal or via plots.
  - Trend monitoring over time.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/sysmon-cli.git
cd sysmon-cli
pip install -r requirements.txt
