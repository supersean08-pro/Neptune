import time

# Constants
NEPTUNE_GRAVITY = 11.15  # m/s^2
NEPTUNE_TEMPERATURE = -218  # Celsius
NEPTUNE_WIND_SPEED = 2000   # km/h

# Function to simulate loading
def slow_print(text, delay=0.03):
    """
    Prints text character by character with a delay to simulate a typewriter effect.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# View descriptions from different perspectives
def view_description():
    """
    Allows the user to view Neptune from different perspectives.
    """
    print("\nWhere would you like to view Neptune from?")
    print("1. Surface of Neptune")
    print("2. From Neptune’s upper atmosphere")
    print("3. From its moon, Triton")
    print("4. From orbit around Neptune")
    
    while True:
        choice = input("Enter your choice (1–4): ")
        if choice in ["1", "2", "3", "4"]:
            break
        print("Invalid selection. Please enter a number between 1 and 4.")
    
    descriptions = {
        "1": "The 'surface' is not solid — you'd float in thick methane clouds, seeing swirling blue storms and constant winds at supersonic speeds.",
        "2": "From the upper atmosphere, you'd see deep blues and purples, feeling pressure like 1,000 Earth atmospheres as you descend.",
        "3": "Triton, Neptune’s moon, offers a frozen view of the planet, with Neptune’s stormy beauty dominating the sky in deep blue.",
        "4": "From orbit, Neptune appears calm, large, and distant — its faint ring system visible as a shimmering halo."
    }

    print()
    slow_print(descriptions[choice])

# Calculate weight on Neptune
def weight_calculator():
    """
    Calculates the user's weight on Neptune based on their mass.
    """
    try:
        mass = float(input("\nEnter your mass in kg: "))
        weight = mass * NEPTUNE_GRAVITY
        print(f"Your weight on Neptune would be approximately {weight:.2f} Newtons.")
        print("This is calculated using the formula W = M x G")
        print(f"Where M = {mass} kg and G = {NEPTUNE_GRAVITY} m/s²")
    except ValueError:
        print("Invalid input. Please enter a number.")

# What it would feel like
def neptune_feeling():
    """
    Describes what it would feel like to stand on Neptune.
    """
    print("\nImagine standing on Neptune...")
    slow_print("You wouldn’t really stand — there’s no solid surface. You’d sink into icy gases.")
    slow_print(f"Temperatures reach {NEPTUNE_TEMPERATURE}°C. Winds roar at over {NEPTUNE_WIND_SPEED} km/h — the fastest in the solar system.")
    slow_print("The blue hues surround you, and methane clouds shimmer in eerie silence.")

# Main menu
def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        print("\n🌌 Welcome to the 'Experience Neptune' Program 🌌")
        print("Choose an option:")
        print("1. View Neptune from different perspectives")
        print("2. Calculate your weight on Neptune")
        print("3. What would it feel like?")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ")

        if choice == "1":
            view_description()
        elif choice == "2":
            weight_calculator()
        elif choice == "3":
            neptune_feeling()
        elif choice == "4":
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Goodbye, space explorer!")
                break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main_menu()