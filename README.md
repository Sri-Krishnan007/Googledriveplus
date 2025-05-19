# Googledriveplus

Googledriveplus is a Python-based image manipulation web application built with Streamlit. It allows users to upload images and perform a variety of editing operations, including cropping, resizing, filtering (grayscale/sepia), masking, morphing, and merging images.

## Features

- **Image Upload**: Upload one or two images in JPG, PNG, or JPEG format.
- **Crop**: Select and crop a region of your image.
- **Resize**: Change the dimensions of your image.
- **Filters**: Apply grayscale or sepia filters to your images.
- **Mask**: Apply a circular mask to highlight the center of your image.
- **Morphing**: Smoothly blend two images using adjustable alpha.
- **Merging**: Overlay and blend two images.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sri-Krishnan007/Googledriveplus.git
   cd Googledriveplus
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit pillow opencv-python numpy
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run a.py
   ```

2. **Open your browser** and go to the local URL provided by Streamlit (usually http://localhost:8501/).

3. **Upload images** and select your desired operation from the sidebar menu.

## Example Workflow

- Upload an image.
- Choose an operation (crop, resize, filter, mask, morph, or merge).
- Adjust sliders or select options as needed.
- View results instantly within the app.

## File Structure

- `a.py` — Main application file containing all image manipulation logic and Streamlit UI.

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License.

---

Let me know if you want to add author info, sample screenshots, or any other customization!
