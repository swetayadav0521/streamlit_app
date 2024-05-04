import pandas as pd
#import pandas_profiling
import streamlit as st
import altair as alt

#from streamlit_pandas_profiling import st_profile_report

data = pd.read_csv('onlinefoods.csv')
st.write("Online Food Data")
st.write(data)
#pr = data.profile_report()

#st_profile_report(pr)

st.write("Charts")
st.write("Altair Chart")
x_axis = str(st.text_input("Select the x-axis data from above table"))
y_axis = str(st.text_input("Select the y-axis data from above table"))
if x_axis:
    st.write(f"{x_axis}, {y_axis}")
# c = alt.Chart(data).mark_circle().encode(x="Age", y="Gender", size="Occupation", color="Age", tooltip=["Age", "Gender", "Occupation"])
# st.write(c)
if x_axis != "":
    st.write(type(x_axis))
    c = alt.Chart(data).mark_circle().encode(x=f"{x_axis}", y=f"{y_axis}", size=data.size, color=data.size, tooltip=[f"{x_axis}", f"{y_axis}", data.size])
    st.write(c)

st.write("Bar Chart")
st.bar_chart(data, y=["Age", "Gender"])

chart = alt.Chart(data).mark_circle().encode(x='Age', y={'field': 'Gender', 'field': 'latitude'}, color='Gender').interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
    
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)

