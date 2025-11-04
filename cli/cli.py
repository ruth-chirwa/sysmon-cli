from os import name
from .commands.cpu import cpu_info, monitor_cpu, initialize_logs, loading_animation
import click
import time

@click.group()
def cli():
    """🌸 SysMon CLI 🌸 - Monitor your system like a boss!"""
    click.secho("""
╔════════════════════════════╗
║  🌸 Welcome to SysMon CLI 🌸  ║
╚════════════════════════════╝
""", fg='magenta', bold=True)
    loading_animation()


# Registering the cpu_info command
cli.add_command(cpu_info)

if __name__ == "__main__":
    cli()