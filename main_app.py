import streamlit as st
from PIL import Image

st.title("アプリ")
st.caption("これはテストアプリです。")

st.subheader("自己紹介")
st.text("私は半蔵門です。\n"
        "良ければ一緒にプログラミングを学びましょう")

image = Image.open("./data/test1.png")
st.image(image, width=200)