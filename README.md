Sure! Here’s a sample `README.md` for your project "GOE (God Of Excel)":

---

# GOE (God Of Excel)

GOE (God Of Excel) is a Python-based application designed to perform various operations on Excel files, including comparing, finding matches, removing duplicates, sorting, counting, summarizing, and more. The application features a user-friendly GUI built with CustomTkinter.

## Features

- **Compare and Find Matching**: Compare two sets of Excel files and find matching entries.
- **Compare and Find Missing**: Identify missing entries when comparing two sets of Excel files.
- **Remove Duplicates**: Remove duplicate entries from Excel files.
- **Sort, Count, Summarize**: Sort data, count entries, and summarize information in Excel files.
- **Criteria-Based Filtering**: Look for lines in Excel files that meet specific criteria.

## Requirements

- Python 3.x
- CustomTkinter
- Pandas
- Tkinter (included with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/lincalibur/GOE.git
    cd GOE
    ```

2. Install the required libraries:
    ```sh
    pip install customtkinter pandas
    ```

## Usage

1. Run the application:
    ```sh
    python goe.py
    ```

2. The GUI will open, allowing you to:
    - Select files for the search bucket and list.
    - Choose the operations you want to perform using the sidebar toggles.
    - Click "Run" to execute the selected operations.

## GUI Layout

- **Sidebar**: Contains toggles for enabling/disabling different features.
- **Main Content Area**: Includes fields for selecting Excel files for the search bucket and list.

## Example

1. Select files for the search bucket and list using the "Browse" buttons.
2. Enable the desired operations by checking the appropriate boxes in the sidebar.
3. Click "Run" to perform the selected operations on the chosen Excel files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Contact

For any inquiries or issues, please contact lincalibur@gmail.com.
