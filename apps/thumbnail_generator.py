import cv2
import numpy as np
import streamlit as st


data = {
    "thumbnail_img": np.zeros((720, 1280), np.uint8),
    "title": "",
    "font_scale": 2,
    "x": 50,
    "y": 350,
    "thickness": 3,
}


def download_thumbnail():
    img = st.session_state.data["thumbnail_img"]
    _, encoded_image = cv2.imencode(".jpg", img)
    image_bytes = encoded_image.tobytes()
    return image_bytes


def update_font_scale(direction):
    if direction == "increase":
        st.session_state.data["font_scale"] += 0.1
    else:
        st.session_state.data["font_scale"] -= 0.1

    on_title_change()


if "data" not in st.session_state:
    st.session_state["data"] = data


def on_title_change():
    updated_image = cv2.putText(
        np.zeros((720, 1280), np.uint8),
        st.session_state.title,
        (st.session_state.data["x"], st.session_state.data["y"]),
        cv2.FONT_HERSHEY_PLAIN,
        st.session_state.data["font_scale"],
        (255, 255, 255),
        st.session_state.data["thickness"],
    )
    st.session_state.data["thumbnail_img"] = updated_image


st.title("Youtube Thumbnail Generator")
title = st.text_input("Enter Video Title", on_change=on_title_change, key="title")
st.image(st.session_state.data["thumbnail_img"])
st.button("Increase Font Size", on_click=update_font_scale, args=("increase",))
st.button("Decrease Font Size", on_click=update_font_scale, args=("decrease",))
st.download_button(
    "Download Thumbnail",
    download_thumbnail(),
    file_name="thumbnail.jpg",
)
