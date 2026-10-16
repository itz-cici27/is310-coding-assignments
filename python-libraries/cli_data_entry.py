import csv
from datetime import date, datetime
from pathlib import Path
 
from rich.console import Console
from rich.prompt import Confirm, IntPrompt, Prompt
from rich.table import Table
 
console = Console()
 
DATA_FILE = Path(__file__).parent / "social_media_diary.csv"
 
FIELDS = [
    "date",
    "platform",
    "minutes",
    "time_of_day",
    "purpose",
    "interrupted_studying",
    "notes",
]
 
PLATFORMS = ["Instagram", "TikTok", "YouTube", "Snapchat", "X", "Reddit", "Discord", "Other"]
TIMES_OF_DAY = ["Morning", "Afternoon", "Evening", "Late night"]
PURPOSES = ["School", "Social", "Entertainment", "News", "Other"]
 
EXAMPLE_ENTRIES = [
    {
        "date": "2026-10-12",
        "platform": "TikTok",
        "minutes": "45",
        "time_of_day": "Late night",
        "purpose": "Entertainment",
        "interrupted_studying": "Yes",
        "notes": "Meant to watch one video before bed",
    },
    {
        "date": "2026-10-12",
        "platform": "Discord",
        "minutes": "30",
        "time_of_day": "Evening",
        "purpose": "School",
        "interrupted_studying": "No",
        "notes": "Group project call",
    },
    {
        "date": "2026-10-13",
        "platform": "Instagram",
        "minutes": "20",
        "time_of_day": "Afternoon",
        "purpose": "Social",
        "interrupted_studying": "Yes",
        "notes": "Checked messages between classes",
    },
]
 
 
def build_table(entries, title):
    table = Table(title=title)
    table.add_column("Date", style="cyan", no_wrap=True)
    table.add_column("Platform", style="magenta")
    table.add_column("Minutes", justify="right")
    table.add_column("Time of day")
    table.add_column("Purpose")
    table.add_column("Interrupted studying?")
    table.add_column("Notes", style="dim")
 
    for entry in entries:
        table.add_row(
            entry["date"],
            entry["platform"],
            entry["minutes"],
            entry["time_of_day"],
            entry["purpose"],
            entry["interrupted_studying"],
            entry["notes"],
        )
    return table
 
 
def ask_date():
    today = date.today().isoformat()
    while True:
        answer = Prompt.ask("Date (YYYY-MM-DD)", default=today)
        try:
            datetime.strptime(answer, "%Y-%m-%d")
            return answer
        except ValueError:
            console.print("[red]Please use the format YYYY-MM-DD, for example 2026-10-14.[/red]")
 
 
def ask_minutes():
    while True:
        minutes = IntPrompt.ask("Minutes spent")
        if minutes > 0:
            return str(minutes)
        console.print("[red]Minutes must be greater than 0.[/red]")
 
 
def collect_entry():
    entry = {}
    entry["date"] = ask_date()
    entry["platform"] = Prompt.ask("Platform", choices=PLATFORMS, case_sensitive=False)
    entry["minutes"] = ask_minutes()
    entry["time_of_day"] = Prompt.ask("Time of day", choices=TIMES_OF_DAY, case_sensitive=False)
    entry["purpose"] = Prompt.ask("Main purpose", choices=PURPOSES, case_sensitive=False)
    interrupted = Confirm.ask("Did this interrupt studying or schoolwork?")
    entry["interrupted_studying"] = "Yes" if interrupted else "No"
    entry["notes"] = Prompt.ask("Notes (optional, press Enter to skip)", default="", show_default=False).strip()
    return entry
 
 
def save_entry(entry):
    is_new_file = not DATA_FILE.exists()
    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if is_new_file:
            writer.writeheader()
        writer.writerow(entry)
 
 
def main():
    console.print("\n[bold cyan]Social Media Use Diary[/bold cyan]")
    console.print(
        "Log each time you used a social media app today. "
        "Here are a few example entries to show what one looks like:\n"
    )
    console.print(build_table(EXAMPLE_ENTRIES, "Example entries"))
 
    saved_entries = []
 
    while True:
        console.print(f"\n[bold cyan]New entry #{len(saved_entries) + 1}[/bold cyan]")
        entry = collect_entry()
 
        console.print()
        console.print(build_table([entry], "Please review your entry"))
 
        if Confirm.ask("Is this entry correct?"):
            save_entry(entry)
            saved_entries.append(entry)
            console.print("[green]Entry saved.[/green]")
        else:
            console.print("[yellow]No problem, let's re-enter it.[/yellow]")
            continue
 
        if not Confirm.ask("\nAdd another entry?"):
            break
 
    console.print()
    console.print(build_table(saved_entries, "Entries saved this session"))
    count = len(saved_entries)
    label = "entry" if count == 1 else "entries"
    console.print(f"\n[bold green]Saved {count} {label} to:[/bold green] {DATA_FILE.resolve()}")
 
 
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Stopped. Any entries you already confirmed are still saved.[/yellow]")
 