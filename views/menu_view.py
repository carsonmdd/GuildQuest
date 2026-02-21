from abc import ABC, abstractmethod

class MenuView(ABC):
    """
    Abstract base class implementing the Template Method pattern for menu navigation.
    """
    def run(self):
        """The template method defining the skeleton of the menu loop."""
        while True:
            self.display_header()
            self.display_items()
            self.display_options()
            
            choice = input(">> ").lower()
            if choice == 'b':
                break
            
            if not self.handle_choice(choice):
                print("Invalid choice. Please try again.")

    @abstractmethod
    def display_header(self):
        """Hook for displaying the menu title."""
        pass

    @abstractmethod
    def display_items(self):
        """Hook for displaying the list of entities (campaigns, characters, etc.)."""
        pass

    @abstractmethod
    def display_options(self):
        """Hook for displaying available command options."""
        pass

    @abstractmethod
    def handle_choice(self, choice: str) -> bool:
        """
        Hook for processing user input.
        Returns True if the choice was valid/handled, False otherwise.
        """
        pass
