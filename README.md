# Image To PDF
## Description
This application creates a PDF file from PNG or JPG files.

## How to Use

1. Create a virtual environment using `venv`:
   ```
   $ python -m venv venv
   ```
2. Activate the virtual environment:
    On Windows:
    ```
    $ venv\Scripts\activate
    ```
    On macOS and Linux:
    ```
    $ source venv/bin/activate
    ```
3. Install the required packages using `pip install -e .`:
   ```
   $ pip install -e .
   ``` 
4. Launch the application:
    ```
    $ python main.py
    ```
5. Click on `Select Images` and add the images you want to convert.

6. By clicking `Convert to PDF`, a PDF file will be created in the data directory.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.