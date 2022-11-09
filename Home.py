import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np


st.title("Убираем фон с картинок")
col1, col2 = st.columns(2)
images = st.sidebar.file_uploader("Загрузить фото", accept_multiple_files =True)
if images:
    for image in images:
        with Image.open(image) as img:
            col1.header("Исходник")
            col1.image(img)

            output = remove(img)
            col2.header("Итог")
            col2.image(output)
