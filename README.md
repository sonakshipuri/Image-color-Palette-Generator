# Image-color-Palette-Generator
This web application allows you to easily upload an image and instantly see a color palette of its most prominent colors. It displays these colors as visual swatches along with their corresponding hexadecimal color codes, right in your web browser. 


## Key Features

* **Web-Based Interface:** Access and use the tool directly in your web browser.
* **Simple Image Upload:** Easily select and upload image files from your computer.
* **Instant Color Extraction:** Quickly analyzes the uploaded image to identify key colors.
* **Visual Color Palette:** Presents the extracted colors as clear blocks within your browser.
* **Hex Color Codes:** Shows the exact hexadecimal code for each color (e.g., `#FF0000`).
* **Saves Palette Image:** The generated color palette is also saved as a `.png` image on the server (`static/plots` folder).
* **Choice of Analysis:** Option to extract colors based on frequency or using color clustering.

## How to Use

1.  **Clone this project:**
    ```bash
    git clone [your_repository_url]
    cd [your_project_directory]
    ```

2.  **Install the necessary tools:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Make sure your `requirements.txt` file includes: `Pillow`, `numpy`, `matplotlib`, `scikit-learn`, and `Flask`)*

3.  **Run the web application:**
    ```bash
    python your_app.py  # Replace with the name of your main Flask application file (e.g., app.py)
    ```
    Open your web browser and navigate to the address provided in your terminal (usually `http://127.0.0.1:5000`).

4.  **Upload an Image:** On the website, use the "Choose file" button to select an image from your computer and click "Extract Colors".

5.  **View the Palette:** The extracted color palette will be displayed on the webpage, showing the color swatches and their corresponding hex codes. The palette image will also be saved in the `static/plots` folder on the server.
