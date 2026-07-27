"""
Weather Module
Fetches current weather data from Lapland and displays it in a formatted table.
Helps Santa determine if it's safe to fly.
"""

import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from core.api import get_json

# Constants for the weather API
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
LAPLAND_LATITUDE = 66.54
LAPLAND_LONGITUDE = 25.84
WIND_WARNING_THRESHOLD = 20  # km/h
EXTREME_COLD_THRESHOLD = -20  # °C


def run_weather(console: Console) -> None:
    """
    Fetches and displays current weather conditions in Lapland.

    Shows temperature and wind speed in a formatted table.
    Displays warnings or good conditions message based on weather data.

    Args:
        console (Console): Rich Console instance for formatted output
    """
    console.print()
    console.print("[bold cyan]Fetching weather data from Lapland...[/bold cyan]")
    console.print()

    try:
        # Prepare API request parameters
        params = {
            "latitude": LAPLAND_LATITUDE,
            "longitude": LAPLAND_LONGITUDE,
            "current_weather": True
        }

        # Make API request using our helper function
        data = get_json(WEATHER_API_URL, params)

        # Validate that we received the expected data structure
        if "current_weather" not in data:
            console.print("[bold red]Error: weather data is incomplete or unavailable.[/bold red]")
            console.print()
            return

        current_weather = data["current_weather"]

        # Extract required fields with validation
        temperature = current_weather.get("temperature")
        windspeed = current_weather.get("windspeed")

        # Check if both fields are present
        if temperature is None or windspeed is None:
            console.print("[bold red]Error: weather data is incomplete or unavailable.[/bold red]")
            console.print()
            return

        # Create weather data table
        table = Table(
            show_header=True,
            header_style="bold cyan",
            border_style="cyan",
            box=box.ROUNDED,
            padding=(0, 4)
        )
        table.add_column("Parameter", style="white", no_wrap=True)
        table.add_column("Value", style="bold green", no_wrap=True)

        # Add weather data rows with emojis
        table.add_row("Temperature", f"{temperature} °C")
        table.add_row("Wind Speed", f"{windspeed} km/h")

        # Wrap table in a panel
        panel = Panel(
            table,
            title="[bold white]Lapland Weather Station[/bold white]",
            border_style="cyan",
            box=box.ROUNDED,
            padding=(0, 5),
            expand=False
        )

        console.print(panel)

        # Evaluate flight conditions
        console.print()

        # Check for extreme cold
        if temperature < EXTREME_COLD_THRESHOLD:
            console.print("[bold yellow on red] ❄️  EXTREME COLD WARNING  ❄️ [/bold yellow on red]")
            console.print("[dim]Temperature is dangerously low for flight operations.[/dim]")

        # Check for high wind conditions
        elif windspeed > WIND_WARNING_THRESHOLD:
            console.print("[bold yellow on red] ⚠️  TURBULENCE WARNING  ⚠️ [/bold yellow on red]")
            console.print("[dim]Wind speed exceeds safe flight threshold.[/dim]")

        # Conditions are good
        else:
            console.print("[bold green on black] ✅ Conditions look good for takeoff! ✅ [/bold green on black]")
            console.print("[dim]Weather is optimal for flight operations.[/dim]")

        console.print()

    except requests.exceptions.Timeout:
        console.print("[bold red]Network error: unable to reach weather service.[/bold red]")
        console.print("[dim]The request timed out. Please try again.[/dim]")
        console.print()

    except requests.exceptions.ConnectionError:
        console.print("[bold red]Network error: unable to reach weather service.[/bold red]")
        console.print("[dim]Please check your internet connection.[/dim]")
        console.print()

    except requests.exceptions.HTTPError as e:
        console.print("[bold red]Network error: unable to reach weather service.[/bold red]")
        console.print(f"[dim]Server returned error: {e}[/dim]")
        console.print()

    except ValueError:
        console.print("[bold red]Error: received invalid data from weather service.[/bold red]")
        console.print("[dim]The server response was not in the expected format.[/dim]")
        console.print()

    except Exception as e:
        console.print("[bold red]Unexpected error occurred while loading weather data.[/bold red]")
        console.print(f"[dim]{type(e).__name__}: {e}[/dim]")
        console.print()