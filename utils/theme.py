import streamlit as st


def apply_theme():
    """
    Applies CropInsight global styling.
    """

    st.markdown(
        """
        <style>

        /* Main background */
        .stApp {
            background-color: #f7f9f7;
        }


        /* Main headings */
        h1, h2, h3 {
            color: #1b5e20;
            font-family: "Arial";
        }


        /* Metric cards */
        div[data-testid="metric-container"] {
            background-color: white;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
        }


        /* Buttons */
        .stButton button {

            background-color: #2e7d32;
            color: white;

            border-radius: 10px;
            border: none;

            padding: 10px 20px;

            font-weight: bold;

        }


        .stButton button:hover {

            background-color: #1b5e20;

        }


        /* Expanders */

        div[data-testid="stExpander"] {

            background-color: white;
            border-radius: 12px;

        }


        /* Information boxes */

        .stAlert {

            border-radius: 12px;

        }


        </style>
        """,
        unsafe_allow_html=True
    )



def page_header(title, subtitle=None):

    st.markdown(
        f"""
        <h1 style="text-align:center;">
        🌱 {title}
        </h1>
        """,
        unsafe_allow_html=True
    )


    if subtitle:

        st.markdown(
            f"""
            <p style="
            text-align:center;
            font-size:18px;
            color:#555;
            ">
            {subtitle}
            </p>
            """,
            unsafe_allow_html=True
        )



def info_card(title, value, icon="🌱"):

    st.markdown(
        f"""
        <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 2px 8px rgba(0,0,0,0.08);
        ">

        <h2>{icon}</h2>

        <h3>{title}</h3>

        <h2 style="color:#2e7d32;">
        {value}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )
