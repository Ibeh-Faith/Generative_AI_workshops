import streamlit as st
import pandas as pd

# Setting up the page configuration
st.set_page_config(
    page_title="Data Mart",
)


st.title("Data Mart")

# Define header
st.write("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
        <h3 style="margin: 0;">Raw Data</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align: left; font-size: 0.75rem;">
Disclaimer: The raw data would be pre-processed before uploading to the database.
The pre-processing operations include data cleaning and data transformation.
</p>
""", unsafe_allow_html=True)

# Define sidebar
st.sidebar.header("Choose file to upload")
file_upload = st.sidebar.file_uploader("The file format should be CSV", type=["csv"])
if file_upload is not None:
    loan_data = pd.read_csv(file_upload)
    st.sidebar.success("Data uploaded successfully!")
else:
    st.sidebar.warning("Please upload the data.")

if file_upload is not None:
    st.write("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
        </div>
    """, unsafe_allow_html=True)
    loan_data_style = loan_data.head().style \
        .set_table_attributes('class="dataframe"') \
        .set_properties(**{'background-color': '#F6F1E5',
                            'color': 'black',
                            'border': '1px solid black'}) \
        .set_table_styles([{'selector': 'th', 'props': [('background-color', '#967E76'),
                                                        ('color', '#F6F1E5'),
                                                        ('font-weight', 'bold'),
                                                        ('padding', '5px 10px'),
                                                        ('border', '1px solid #967E76'),
                                                        ('text-align', 'center'),
                                                        ('vertical-align', 'middle'),
                                                        ('white-space', 'nowrap'),
                                                        ('overflow', 'hidden'),
                                                        ('text-overflow', 'ellipsis')]},
                           {'selector': 'td', 'props': [('padding', '5px 10px'),
                                                        ('border', '1px solid black')]}])

    # Set the precision of numeric columns
    numeric_cols = loan_data.select_dtypes(include=[float, int]).columns
    loan_data_style_float_format = loan_data_style.format({col: "{:.2f}" for col in numeric_cols})

    # Display the table
    st.table(loan_data_style_float_format)
    st.write ("Data is fed to our Generative model")

converted_data = loan_data.to_dict(orient='list')

# Run the Streamlit app
if __name__ == '__main__':
    st.markdown("""<style>footer{visibility:hidden;}</style>""", unsafe_allow_html=True)

    st.write("""
        <hr style="margin-top: 3rem; margin-bottom: 1rem;">
        <p style="text-align: center; font-size: 0.75rem;">&copy; Copyright Analytics India Magazine.</p>
    """, unsafe_allow_html=True) 