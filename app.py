import streamlit as st


homepage = st.Page("./homepage.py", title="Streamlit Apps")

thumbnail_generator = st.Page(
    "./apps/thumbnail_generator.py",
    title="Generate Thumbnail",
)


pg = st.navigation([homepage, thumbnail_generator])
pg.run()
