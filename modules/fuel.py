"""
Fuel Module
Searches for cocktail recipes and displays ingredients and instructions.
Helps Santa find his favorite "fuel" for the long Christmas journey.
"""

import requests
from rich.console import Console
from rich.panel import Panel
from rich import box
from typing import Optional
from core.api import get_json

# Constants for the cocktail API
COCKTAIL_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/search.php"


def get_cocktail_data(cocktail_name: str) -> Optional[dict]:
    """
    Fetches cocktail data from TheCocktailDB API.

    Args:
        cocktail_name (str): Name of the cocktail to search for

    Returns:
        Optional[dict]: Cocktail data dictionary or None if not found

    Raises:
        Various requests exceptions for network errors
    """
    params = {"s": cocktail_name}
    data = get_json(COCKTAIL_API_URL, params)

    # Check if any drinks were found
    if not data.get("drinks") or data["drinks"] is None:
        return None

    # Return the first cocktail found
    return data["drinks"][0]


def collect_ingredients(cocktail: dict) -> list:
    """
    Collects all non-empty ingredients from a cocktail dictionary.

    TheCocktailDB returns ingredients in fields strIngredient1 through strIngredient15.
    This function dynamically collects all that are present.

    Args:
        cocktail (dict): Cocktail data dictionary

    Returns:
        list: List of ingredient names (non-empty strings)
    """
    ingredients = []

    # Loop through all 15 possible ingredient slots
    for i in range(1, 16):
        ingredient_key = f"strIngredient{i}"
        ingredient = cocktail.get(ingredient_key)

        # Only add if ingredient exists and is not empty
        if ingredient and isinstance(ingredient, str) and ingredient.strip():
            ingredients.append(ingredient.strip())

    return ingredients


def format_cocktail_display(cocktail: dict, ingredients: list) -> str:
    """
    Formats cocktail information for display.

    Args:
        cocktail (dict): Cocktail data dictionary
        ingredients (list): List of ingredient names

    Returns:
        str: Formatted string with cocktail information
    """
    # Get cocktail name
    name = cocktail.get("strDrink", "Unknown")

    # Get instructions
    instructions = cocktail.get("strInstructions", "No instructions available.")

    # Format ingredients list with bullet points
    ingredients_text = "\n".join([f"  • {ingredient}" for ingredient in ingredients])

    # Get ingredient count
    ingredient_count = len(ingredients)

    # Build the display text
    display_text = f"[bold yellow]Cocktail:[/bold yellow] [white]{name}[/white]\n\n"
    display_text += f"[bold yellow]Ingredients:[/bold yellow]\n"
    display_text += f"[white]{ingredients_text}[/white]\n\n"
    display_text += f"[bold yellow]Ingredients found:[/bold yellow] [cyan]{ingredient_count}[/cyan]\n\n"
    display_text += f"[bold yellow]Instructions:[/bold yellow]\n[white]{instructions}[/white]"

    return display_text


def run_fuel(console: Console) -> None:
    """
    Interactive cocktail search module.

    Prompts user for a cocktail name, searches TheCocktailDB,
    and displays the recipe with ingredients and instructions.
    Allows repeated searches without exiting the module.

    Args:
        console (Console): Rich Console instance for formatted output
    """
    console.print()

    while True:
        # Prompt user for cocktail name
        console.print("[bold yellow]Enter cocktail name to search:[/bold yellow] ", end="")
        cocktail_name = input().strip()

        # Validate input
        if not cocktail_name:
            console.print("[bold red]Error: Please enter a cocktail name.[/bold red]")
            console.print()
            continue

        console.print()
        console.print(f"[bold yellow]Searching for '{cocktail_name}'...[/bold yellow]")
        console.print()

        try:
            # Fetch cocktail data
            cocktail = get_cocktail_data(cocktail_name)

            # Check if cocktail was found
            if cocktail is None:
                console.print("[bold red]No cocktail found for your search.[/bold red]")
                console.print("[dim]Try a different name or check spelling.[/dim]")
                console.print()
            else:
                # Validate required fields
                if not cocktail.get("strDrink"):
                    console.print("[bold red]Error: cocktail data is incomplete or unavailable.[/bold red]")
                    console.print()
                else:
                    # Collect ingredients
                    ingredients = collect_ingredients(cocktail)

                    # Check if we have any ingredients
                    if not ingredients:
                        console.print("[bold red]Error: no ingredients found for this cocktail.[/bold red]")
                        console.print()
                    else:
                        # Format and display cocktail information
                        display_text = format_cocktail_display(cocktail, ingredients)

                        panel = Panel(
                            display_text,
                            title="[bold yellow]Santa's Fuel[/bold yellow]",
                            border_style="yellow",
                            box=box.ROUNDED,
                            padding=(1, 4),
                            expand=False
                        )

                        console.print(panel)
                        console.print()

        except requests.exceptions.Timeout:
            console.print("[bold red]Network error: unable to reach cocktail service.[/bold red]")
            console.print("[dim]The request timed out. Please try again.[/dim]")
            console.print()

        except requests.exceptions.ConnectionError:
            console.print("[bold red]Network error: unable to reach cocktail service.[/bold red]")
            console.print("[dim]Please check your internet connection.[/dim]")
            console.print()

        except requests.exceptions.HTTPError as e:
            console.print("[bold red]Network error: unable to reach cocktail service.[/bold red]")
            console.print(f"[dim]Server returned error: {e}[/dim]")
            console.print()

        except ValueError:
            console.print("[bold red]Error: received invalid data from cocktail service.[/bold red]")
            console.print("[dim]The server response was not in the expected format.[/dim]")
            console.print()

        except Exception as e:
            console.print("[bold red]Unexpected error occurred while loading cocktail data.[/bold red]")
            console.print(f"[dim]{type(e).__name__}: {e}[/dim]")
            console.print()

        # Ask if user wants to search again
        console.print("[bold cyan]Do you want to search again? (y/n):[/bold cyan] ", end="")
        choice = input().strip().lower()
        console.print()

        if choice != 'y' and choice != 'yes':
            break