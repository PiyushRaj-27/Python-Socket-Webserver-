# Python Webserver using Sockets

This is a simple Python webserver built using sockets and threading. The server handles HTTP requests, parses them, and serves HTML files along with their associated CSS resources. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Handles basic HTTP GET requests.
- Serves static HTML files from the `pages` directory.
- Links and serves CSS files associated with the HTML pages.
- Multithreaded to handle multiple client requests simultaneously.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/PiyushRaj-27/Python-Socket-Webserver-
    cd python-webserver
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Start the server:**

    ```bash
    python main.py
    ```

2. **Access the server:**

    Open your web browser and navigate to `http://localhost:8002`.

## Adding HTML and CSS Pages

To add new HTML and CSS pages to your webserver, follow these steps:

1. **Add HTML Pages:**
   
   - Place your HTML files in the `pages` directory.
   - Update the `urls` dictionary in `urlMapper/urlMapped.py` to map your URL paths to the corresponding HTML files. For example:
     
     ```python
     urls = {
         "/" : "home.html",
         "/contact" : "contact.html",
         "/newpage" : "newpage.html"  # Add your new page here
     }
     ```

2. **Add CSS Files:**

   - Place your CSS files in the `styles` directory.
   - Ensure your HTML files link to the CSS files correctly. For example, in your HTML file:
     
     ```html
     <link rel="stylesheet" type="text/css" href="style.css">
     ```

   - The `htmlParser.py` script will automatically link the CSS files found in the HTML files.

3. **Add a Default Not Found (404) Page:**

   - Create an HTML file for your "Not Found" page (e.g., `nf.html`) and place it in the `pages` directory.
   - Update the `DEFAULT_NOT_FOUND` variable in `urlMapper/urlMapped.py` to point to your custom "Not Found" page. For example:
     
     ```python
     DEFAULT_NOT_FOUND = "nf.html"  # Your custom 404 page
     ```

4. **Restart the Server:**

   After adding your new HTML and CSS files, updating the URL mappings, and setting the custom "Not Found" page, restart the server to apply the changes.

    ```bash
    python main.py
    ```

Now, your new HTML and CSS pages should be accessible from the webserver.





## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, feel free to open an issue or create a pull request.

1. **Fork the repository**
2. **Create a new branch:**

    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes and commit them:**

    ```bash
    git commit -m "Add some feature"
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature/your-feature-name
    ```

5. **Open a pull request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


