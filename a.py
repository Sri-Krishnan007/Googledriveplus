import streamlit as st
from PIL import Image, ImageOps, ImageFilter, ImageDraw
import cv2
import numpy as np

# Function to display the uploaded image
def display_image(image):
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Cropping function
def crop_image(image, left, top, right, bottom):
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image

# Resizing function
def resize_image(image, width, height):
    resized_image = image.resize((width, height))
    return resized_image

# Grayscale Filter function
def apply_filter(image):
    img_array = np.array(image)
    gray_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    filtered_image = Image.fromarray(gray_image)
    return filtered_image

# Sepia Filter function
def apply_sepia(image):
    img_array = np.array(image)
    sepia_filter = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
    sepia_image = cv2.transform(img_array, sepia_filter)
    sepia_image = np.clip(sepia_image, 0, 255)
    return Image.fromarray(sepia_image)

# Masking function (Apply circular mask)
def apply_mask(image):
    width, height = image.size
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((width/4, height/4, width*3/4, height*3/4), fill=255)
    masked_image = Image.composite(image, Image.new('RGB', image.size, (0, 0, 0)), mask)
    return masked_image

# Morphing function (Blend two images)
def morph_images(image1, image2, alpha=0.5):
    img1 = np.array(image1)
    img2 = np.array(image2)
    morphed_image = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
    return Image.fromarray(morphed_image)

# Merging function (overlay two images)
def merge_images(image1, image2):
    image2_resized = image2.resize(image1.size)
    merged_image = Image.blend(image1, image2_resized, alpha=0.5)
    return merged_image

# Main function for Streamlit app
def main():
    st.title("GoogleDrivePlus - Image Manipulation App")
    
    uploaded_file1 = st.file_uploader("Choose the first image", type=["jpg", "png", "jpeg"])
    uploaded_file2 = st.file_uploader("Choose the second image (for merging or morphing)", type=["jpg", "png", "jpeg"])
    
    if uploaded_file1 is not None:
        # Open the first image
        image1 = Image.open(uploaded_file1)
        display_image(image1)

        task = st.selectbox("Select an image manipulation function", 
                            ["Crop", "Resize", "Apply Filter", "Mask", "Morphing", "Merging"])
        
        if task == "Crop":
            left = st.slider("Left", 0, image1.width, 0)
            top = st.slider("Top", 0, image1.height, 0)
            right = st.slider("Right", 0, image1.width, image1.width)
            bottom = st.slider("Bottom", 0, image1.height, image1.height)
            if st.button("Crop Image"):
                cropped_image = crop_image(image1, left, top, right, bottom)
                display_image(cropped_image)
        
        elif task == "Resize":
            width = st.slider("Width", 1, 2000, image1.width)
            height = st.slider("Height", 1, 2000, image1.height)
            if st.button("Resize Image"):
                resized_image = resize_image(image1, width, height)
                display_image(resized_image)
        
        elif task == "Apply Filter":
            filter_option = st.selectbox("Choose a filter", ["Grayscale", "Sepia"])
            if filter_option == "Grayscale":
                if st.button("Apply Grayscale Filter"):
                    filtered_image = apply_filter(image1)
                    display_image(filtered_image)
            elif filter_option == "Sepia":
                if st.button("Apply Sepia Filter"):
                    sepia_image = apply_sepia(image1)
                    display_image(sepia_image)

        elif task == "Mask":
            if st.button("Apply Circular Mask"):
                masked_image = apply_mask(image1)
                display_image(masked_image)
        
        elif task == "Morphing":
            if uploaded_file2 is not None:
                image2 = Image.open(uploaded_file2)
                alpha = st.slider("Morphing Alpha", 0.0, 1.0, 0.5)
                if st.button("Morph Images"):
                    morphed_image = morph_images(image1, image2, alpha)
                    display_image(morphed_image)
        
        elif task == "Merging":
            if uploaded_file2 is not None:
                image2 = Image.open(uploaded_file2)
                if st.button("Merge Images"):
                    merged_image = merge_images(image1, image2)
                    display_image(merged_image)

# Run the app
if __name__ == "__main__":
    main()
