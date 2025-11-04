import csv
import psutil
import time
import os
import click
from pathlib import Path
from datetime import datetime

# ---------- Helper functions ----------
def loading_animation():
    click.echo("Loading SysMon CLI...")
    for i in range(1, 11):
        click.echo(f"[{'#' * i}{'.' * (10-i)}] {i*10}%", nl=False)
        click.echo("\r", nl=False)
        time.sleep(0.1)
    click.echo("\n")

def initialize_logs(percpu, logfile=None):
    reports_dir = Path('reports')
    reports_dir.mkdir(exist_ok=True)
    
    timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    if not logfile:
        logfile = f"cpu_log_{timestamp_str}.csv"
    
    log_path = reports_dir / logfile

    if not log_path.exists():
        with open(log_path, 'w', newline='') as f:
            writer = csv.writer(f)
            header = ['Timestamp'] + [f'Core {i}' for i in range(psutil.cpu_count())] if percpu else ['Timestamp', 'Total CPU']
            writer.writerow(header)
    
    return log_path

def monitor_cpu(interval, percpu, log_path):
    try:
        while True:
            cpu = psutil.cpu_percent(interval=0.5, percpu=percpu)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            click.clear()
            click.secho("🌸 SysMon CPU Monitor 🌸", fg='magenta', bold=True)
           # Display
            if percpu:
                # Just log all cores as a list
                click.echo(f"CPU Usage per Core: {cpu}")
            else:
                click.echo(f"Total CPU Usage: {cpu:.1f}%")

            # Log to CSV
            with open(log_path, 'a', newline='') as f:
                writer = csv.writer(f)
                row = [timestamp] + list(cpu) if percpu else [timestamp, cpu]
                writer.writerow(row)

            time.sleep(interval)
    except KeyboardInterrupt:
        click.echo(f"\nExiting CPU monitor. Logs saved to {log_path}")
# --- Click command ---
@click.command()
@click.option('--interval', default=2, type=int, help="Refresh interval in seconds")
@click.option('--percpu', is_flag=True, help="Show per-core CPU information")
def cpu_info(interval, percpu):
    """Monitor CPU usage"""
    loading_animation()
    choice = click.prompt("Do you want to enable logging?",
                          type=click.Choice(['y', 'n']),
                          default='y')
    log_path = None
    if choice == 'y':
        log_path = initialize_logs(percpu)
        click.echo(f"Logging CPU usage to {log_path}")
    monitor_cpu(interval, percpu, log_path)