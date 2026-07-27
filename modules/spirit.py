"""
Spirit Module
Fetches a random joke from an API and displays it to boost elf morale.
Helps keep the elves happy and motivated during the holiday season.
"""

import requests
from rich.console import Console
from rich.panel import Panel
from rich import box
from core.api import get_json

# Constants for the joke API
JOKE_API_URL = "https://official-joke-api.appspot.com/jokes/random"


def run_spirit(console: Console) -> None:
    """
    Fetches and displays a random joke to boost elf morale.

    Retrieves a joke with setup and punchline from the Official Joke API
    and displays it in a formatted panel.

    Args:
        console (Console): Rich Console instance for formatted output
    """
    console.print()  # Empty line for spacing
    console.print("[bold green]Fetching a joke to boost elf morale...[/bold green]")
    console.print()

    try:
        # Make API request to get a random joke
        data = get_json(JOKE_API_URL)

        # Extract joke components with validation
        setup = data.get("setup")
        punchline = data.get("punchline")

        # Validate that both parts are present and are strings
        if not setup or not isinstance(setup, str):
            console.print("[bold red]Error: joke data is incomplete or unavailable.[/bold red]")
            console.print()
            return

        if not punchline or not isinstance(punchline, str):
            console.print("[bold red]Error: joke data is incomplete or unavailable.[/bold red]")
            console.print()
            return

        # Format the joke with clear separation between setup and punchline
        joke_text = f"[bold white]{setup}[/bold white]\n\n[bold yellow]{punchline}[/bold yellow]"

        # Create panel with the joke
        panel = Panel(
            joke_text,
            title="[bold green]Elf Morale Booster[/bold green]",
            border_style="green",
            box=box.ROUNDED,
            padding=(1, 5),
            expand=False
        )

        console.print(panel)
        console.print()

    except requests.exceptions.Timeout:
        console.print("[bold red]Network error: unable to reach joke service.[/bold red]")
        console.print("[dim]The request timed out. Please try again.[/dim]")
        console.print()

    except requests.exceptions.ConnectionError:
        console.print("[bold red]Network error: unable to reach joke service.[/bold red]")
        console.print("[dim]Please check your internet connection.[/dim]")
        console.print()

    except requests.exceptions.HTTPError as e:
        console.print("[bold red]Network error: unable to reach joke service.[/bold red]")
        console.print(f"[dim]Server returned error: {e}[/dim]")
        console.print()

    except ValueError:
        console.print("[bold red]Error: received invalid data from joke service.[/bold red]")
        console.print("[dim]The server response was not in the expected format.[/dim]")
        console.print()

    except Exception as e:
        console.print("[bold red]Unexpected error occurred while loading joke.[/bold red]")
        console.print(f"[dim]{type(e).__name__}: {e}[/dim]")
        console.print()