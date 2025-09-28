
<img src="./mini-project/images/1_kKrBYYaPTaSTOlOIfsC-6w11.png">
<br><br><br>

# Password Generator Python Project

## Introduction
This is a simple Python-based Password Generator application built with Streamlit. It allows users to generate secure passwords of different types, evaluate their strength, generate QR codes for easy sharing (e.g., to mobile devices), and save generated passwords to a file. The app is designed for ease of use and can be run locally or deployed.

The source code includes two main files:
- `password_generator.py`: Contains the core logic for generating passwords, checking strength, and saving to file.
- `dashboard.py`: The Streamlit frontend for user interaction.

## Features
- **Password Types**: Generate three types of passwords:
  - **Random Password**: Customizable length (8-100 characters), with options to include numbers and symbols.
  - **Memorable Password**: Combines random words (2-10 words) from a vocabulary list, with customizable separator (e.g., '-') and capitalization.
  - **Pin Code**: Numeric PIN with adjustable length (4-32 digits).
- **Password Strength Evaluation**: Assesses the strength as Weak, Medium, or Strong based on length, character variety (lowercase, uppercase, digits, symbols), and displays a progress bar.
- **QR Code Generation**: Creates a QR code for the password, which can be scanned to paste on another device (e.g., phone).
- **Download QR Image**: Option to download the QR code as a PNG file.
- **Copy Password**: The generated password is displayed in a code block for easy copying.
- **Customization Options**:
  - Adjust length or number of words.
  - Toggle inclusion of numbers/symbols (for Random Password).
  - Capitalize words (for Memorable Password).
  - Custom separator for Memorable Password.
- **Save to File**: Automatically saves each generated password with a timestamp to `passwords.txt` for persistent storage.
- **User-Friendly Interface**: Built with Streamlit for a web-based UI, no advanced setup required.

Note: The vocabulary for Memorable Passwords uses NLTK's word corpus. Users cannot directly add custom words in the current version, but the code can be extended for that.

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```

2. **Install Dependencies**:
   Install the required Python packages using pip. It's recommended to use a virtual environment.
   ```
   pip install streamlit nltk qrcode pillow
   ```
   - **streamlit**: For the web interface.
   - **nltk**: For word vocabulary in Memorable Passwords (run `nltk.download('words')` in Python if needed).
   - **qrcode**: For generating QR codes.
   - **pillow**: For image processing (required by qrcode).

   Additional built-in modules used: random, string, re, datetime.

3. **Download NLTK Data** (if not already done):
   Open a Python shell and run:
   ```python
   import nltk
   nltk.download('words')
   ```

## Usage
1. **Run the Application**:
   ```
   streamlit run src/dashboard.py
   ```
   This will launch the app in your default web browser (usually at http://localhost:8501).

2. **Generate a Password**:
   - Select the password type (Random, Memorable, or Pin).
   - Adjust settings (length, include numbers/symbols, number of words, separator, capitalize).
   - Click "Generate Password" to create one.
   - View the password, its strength, and QR code.
   - Download the QR image if needed.
   - The password is automatically saved to `passwords.txt` with a timestamp.

3. **Example Output**:
   - Generated passwords are displayed and can be copied from the code block.
   - Strength is shown with a label (e.g., "Medium") and progress bar.
   - QR code can be scanned or downloaded.

4. **Saved Passwords**:
   - Check `passwords.txt` in the project directory for a log of all generated passwords, e.g.:
     ```
     [2025-09-28 22:13:45] 123456
     [2025-09-28 22:13:50] Abc$123xyz
     ```

## Requirements
- Python 3.8+ (tested on 3.12).
- Operating System: Windows, macOS, or Linux.
- No internet required after installation (except for initial NLTK download).

## Contributing
Feel free to fork the repository and submit pull requests for improvements, such as:
- Adding custom vocabulary input.
- Enhancing security (e.g., encrypted storage).
- More password types or themes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [Streamlit](https://streamlit.io/) for the UI.
- Uses [NLTK](https://www.nltk.org/) for word generation.
- QR code generation via [qrcode](https://pypi.org/project/qrcode/).

If you encounter issues, open an issue on GitHub!
