# app.py
from Introduction import some_intro_function
from image_processing import process_images
from group_members import show_members
from sidebar import sidebar_function

def main():
    # misal kalau pakai Streamlit:
    sidebar_function()
    some_intro_function()
    process_images()
    show_members()

if __name__ == "__main__":
    main()
