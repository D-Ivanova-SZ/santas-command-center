"""
Santa's Command Center - Main Application
A festive console application that displays real-time data from various systems
to help Santa manage his Christmas operations.

Modules:
- Weather: Checks flight conditions in Lapland
- Spirit: Boosts elf morale with jokes
- Fuel: Finds Santa's favorite cocktail recipes
"""

from rich.console import Console
from rich.panel import Panel
from rich import box
from modules.weather import run_weather
from modules.spirit import run_spirit
from modules.fuel import run_fuel


def display_welcome(console: Console) -> None:
    """
    Displays a festive welcome message with ASCII art.

    Args:
        console (Console): Rich Console instance for formatted output
    """
    ascii_art = """
        [bold green]        *
       /|\\
      /*|O\\
     /*/|\\*\\
    /X/O|*\\X\\
   /*/X/|\\X\\*\\
  /O/*/X|*\\O\\X\\
 /*/O/X/|\\X\\O\\*\\
/X/O/*/X|O\\X\\*\\O\\
       |||
    [/bold green]
    """

    title = "[bold red]Santa's Command Center[/bold red]"
    subtitle = "[dim]North Pole Operations Dashboard[/dim]"

    welcome_panel = Panel(
        f"{ascii_art}\n{title}\n{subtitle}",
        border_style="bright_red",
        box=box.DOUBLE,
        padding=(1, 4),
        expand=False
    )

    console.print()
    console.print(welcome_panel)
    console.print()


def display_menu(console: Console) -> None:
    """
    Displays the main menu with available options.

    Args:
        console (Console): Rich Console instance for formatted output
    """
    menu_text = """[bold cyan]1.[/bold cyan] [white]Weather Station[/white] - Check Lapland flight conditions
[bold green]2.[/bold green] [white]Elf Morale Booster[/white] - Get a joke to boost spirits
[bold yellow]3.[/bold yellow] [white]Santa's Fuel[/white] - Search for cocktail recipes
[bold red]Q.[/bold red] [white]Quit[/white] - Exit the application
"""

    menu_panel = Panel(
        menu_text,
        title="[bold green]Santa's Command Center[/bold green]",
        border_style="bright_white",
        box=box.ROUNDED,
        padding=(1, 5),
        expand=False
    )

    console.print(menu_panel)
    console.print()


def main() -> None:
    """
    Main application loop.

    Displays menu, handles user input, and executes selected modules.
    Continues until user chooses to quit.
    """
    # Create console instance
    console = Console()

    # Display welcome message
    display_welcome(console)

    # Main application loop
    while True:
        # Display menu
        display_menu(console)

        # Get user choice
        console.print("[bold white]Choose an option:[/bold white] ", end="")
        choice = input().strip().upper()

        # Handle user choice
        if choice == '1':
            run_weather(console)

        elif choice == '2':
            run_spirit(console)

        elif choice == '3':
            run_fuel(console)

        elif choice == 'Q':
            console.print()
            console.print("[bold green]Goodbye! Happy holidays![/bold green] ", style="bold")
            console.print()
            break

        else:
            console.print()
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")
            console.print()


if __name__ == "__main__":
    main()