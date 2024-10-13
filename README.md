# Random Password Generator

A simple GUI application that generates random passwords of specified lengths using Python's Tkinter library.

## Features

- Generates secure random passwords with a mix of uppercase, lowercase, digits, and special characters.
- Allows users to specify the desired password length.
- Copies the generated password to the clipboard for easy use.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `pyperclip` library

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your machine.
3. Install the `pyperclip` library if you haven't already:

   ```bash
   pip install pyperclip
   ```

4. Run the script using the command:

   ```bash
   python random_password_generator.py
   ```

## Usage

1. Launch the application.
2. Use the spinbox to select the desired password length (between 8 and 32 characters).
3. Click the "GENERATE PASSWORD" button to create a random password.
4. The generated password will be displayed in the entry field.
5. Click the "COPY TO CLIPBOARD" button to copy the password for use elsewhere.

## Example

- **Password Length**: `12`
- **Generated Password**: `A3@bZ8!qLr1#`

## Code Overview

The core functionality of the application is handled by the `Generator` function, which:

- Combines characters from different categories (uppercase, lowercase, digits, punctuation) to create a secure password.
- Updates the GUI with the generated password.
- The `Copy_password` function allows users to copy the generated password to their clipboard.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

## Acknowledgements

- Thanks to the Python and Tkinter communities for providing resources and documentation.
