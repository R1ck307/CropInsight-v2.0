import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <h1 style="
            text-align:center;
            color:#2e7d32;
            ">
            🌱 CropInsight
            </h1>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            """
            <p style="
            text-align:center;
            ">
            Smart Agricultural<br>
            Decision Support System
            </p>
            """,
            unsafe_allow_html=True
        )


        st.divider()


        st.markdown(
            """
            ### 🚀 Modules

            🌱 Crop Diagnosis  
            📸 Image Scanner  
            🌦 Weather Intelligence  
            🤖 AI Assistant  
            📊 Analytics  
            🌾 Farm Management  

            """
        )


        st.divider()


        st.caption(
            "CropInsight v2.0"
        )

        st.caption(
            "Nationals Edition"
        )
