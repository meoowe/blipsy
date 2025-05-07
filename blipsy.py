from time import sleep, time
from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text
import typer
import keyboard

paused: bool = False
current_pause_duration: float = 0.0

console = Console() # Use Rich's pretty printing and terminal bell
typerapp = typer.Typer() # For commands such as 'blipsy run'

# Character Definitions
blipsy_left = """
 ,_/\\____/\\_,
( o      o  )
| -  ^  -   |          
 \\_||___||_/ 
   ||   ||    
"""

blipsy_right = """ 
 ,_/\\____/\\_,
(   o     o )
|  -  ^  -  |
 \\_||___||_/
   ||   ||  
"""

def format_time(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def run_timer(label: str, seconds: int, no_art: bool, pause_hotkey: str):
    start = time()
    end = start + seconds
    flip = False
    progress = Progress( # Makes a progress bar
        TextColumn(f"[bold magenta]{label}"), # e.g Focus Time ------------ Remaining 00:06:09
        BarColumn(),
        TextColumn("[green]Remaining:"),
        TimeRemainingColumn(),
    )
    task = progress.add_task("timer", total=seconds)

    with Live(console=console, refresh_per_second=10, transient=True) as live: # Uses rich.live to prevent flash on each clear
        while time() < end:
            if not paused:
                elapsed = time() - start
                progress.update(task, completed=elapsed)
                table = Table(show_header=False, box=None) # Live just prefers tables. (If it works, it works)
                if not no_art: table.add_row(blipsy_left if flip else blipsy_right) 
                table.add_row(progress.get_renderable())
                live.update(table)
                flip = not flip
                sleep(0.5)
            if paused:
                live.update(
                    Text().append("The timer is paused. ", style="yellow")
                    .append("Press ", style="yellow")
                    .append(pause_hotkey, style="code yellow")
                    .append(" to continue.", style="yellow")
                )

    console.bell() # Ring the terminal bell sound when the timer is finished

def toggle_pause():
    global paused
    paused = not paused


def blipsy_pomodoro(
    pause_hotkey: str,
    no_art: bool = False,
    cycles: int = 4,
    focus_duration: int = 25 * 60,
    short_break: int = 5 * 60,
    long_break: int = 15 * 60,
    focus_message: str = "Focus Time",
    short_break_message: str = "Short Break",
    long_break_message: str = "Long Break",
):
    for cycle in range(1, cycles + 1):
        run_timer(f"{focus_message} (Cycle {cycle}/{cycles})", focus_duration, no_art, pause_hotkey)

        if cycle < cycles:
            run_timer(short_break_message, short_break, no_art, pause_hotkey)
        else:
            run_timer(long_break_message, long_break, no_art, pause_hotkey)

    console.print("""
🎉 ,_/\\____/\\_,
🎉( ^   o   ^  )
🎉| PARTY TIME |
🎉 \\___n__n___/
""" if not no_art else "", style="bold magenta")
    console.print("\n✅ All cycles complete! Take a victory nap 💤", style="bold green")

@typerapp.command()
def run(
    cycles: int = 4, 
    focus_secs: int = 1500, 
    short_break_secs: int = 300, 
    long_break_secs: int = 900, 
    focus_message: str = "Focus Time",
    short_break_message: str = "Go Relax",
    long_break_message: str = "Have a nice break",
    art: bool = True,
    pause_hotkey: str = "ctrl+shift+p"
):
    """Starts the pomodoro timer with usual focus and break lengths."""
    keyboard.add_hotkey(pause_hotkey, toggle_pause)
    blipsy_pomodoro(
        pause_hotkey=pause_hotkey,
        cycles=cycles,
        focus_duration=focus_secs,
        short_break=short_break_secs,
        long_break=long_break_secs,
        focus_message=focus_message,
        short_break_message=short_break_message,
        long_break_message=long_break_message,
        no_art = not art,
    )

@typerapp.command()
def demo():
    """Quick demo with short durations."""
    run(
        cycles=2,
        focus_secs=10,
        short_break_secs=5,
        long_break_secs=8,
        focus_message="Demo Focus",
        short_break_message="Quick Chill",
        long_break_message="Demo Nap"
    )

if __name__ == "__main__":
    typerapp()
