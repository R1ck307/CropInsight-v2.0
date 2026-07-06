import streamlit as st
import pandas as pd

from utils.page_setup import setup_page


setup_page()


st.title(
    "📚 CropInsight Knowledge Base"
)


st.subheader(
    "Agricultural information centre for crops, diseases, pests and treatments"
)


# ---------------- LOAD DATA ----------------


@st.cache_data
def load_data(file):

    try:

        return pd.read_csv(file)

    except Exception:

        return pd.DataFrame()



crops = load_data(
    "data/crops.csv"
)


diseases = load_data(
    "data/diseases.csv"
)


pests = load_data(
    "data/pests.csv"
)


fertilizers = load_data(
    "data/fertilizers.csv"
)


treatments = load_data(
    "data/treatments.csv"
)



# ---------------- SEARCH ----------------


st.divider()


search = st.text_input(
    "🔎 Search Knowledge Base"
)



category = st.selectbox(
    "Select Category",
    [
        "Crops",
        "Diseases",
        "Pests",
        "Fertilizers",
        "Treatments"
    ]
)



# ---------------- DISPLAY FUNCTION ----------------


def display_results(data, title):


    st.subheader(
        title
    )


    if data.empty:

        st.warning(
            "No information available."
        )

        return



    result = data



    if search:


        result = data[
            data.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search,
                    case=False,
                    na=False
                )
                .any(),
                axis=1
            )
        ]



    if result.empty:

        st.info(
            "No matching information found."
        )

        return



    for _, item in result.iterrows():


        with st.container():


            st.markdown(
                "---"
            )


            # First column is usually the name

            name = item.iloc[0]


            st.subheader(
                f"🌱 {name}"
            )


            for column, value in item.items():


                if column != item.index[0]:

                    st.write(
                        f"**{column.replace('_',' ').title()}:** {value}"
                    )



# ---------------- CATEGORY ROUTER ----------------



if category == "Crops":

    display_results(
        crops,
        "🌾 Crop Information"
    )



elif category == "Diseases":

    display_results(
        diseases,
        "🦠 Disease Information"
    )



elif category == "Pests":

    display_results(
        pests,
        "🐛 Pest Information"
    )



elif category == "Fertilizers":

    display_results(
        fertilizers,
        "🌿 Fertilizer Information"
    )



elif category == "Treatments":

    display_results(
        treatments,
        "💊 Treatment Information"
    )



# ---------------- FOOTER ----------------


st.divider()


st.caption(
    "CropInsight v2.0 • Agricultural Knowledge Intelligence System"
      )
