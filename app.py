import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
st.set_page_config(layout='wide')
df= pd.read_csv("india.csv")
list_of_States=list(df['State'].unique())
list_of_States.sort()
list_of_States.insert(0,'Overall India')

st.sidebar.title("India Data ")
selected_state=st.sidebar.selectbox('Select a State',list_of_States)
primary= st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
secondary= st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))
plot=st.sidebar.button('Plot Graph')
if plot:
   st.text("Size represents Primary Parameter")
   st.text("Color represents Secondary Parameter")
   if selected_state== 'Overall India':
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',zoom=4,mapbox_style='carto-positron',size=primary,color=secondary,width=1200,height=900,size_max=35,hover_name='District',color_continuous_scale=px.colors.cyclical.IceFire)

        st.plotly_chart(fig,use_container_width=True)
   else:
       state_df=df[df['State']== selected_state]
       fig1 = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6, mapbox_style='carto-positron', size= primary ,size_max=35,hover_name='District'
                              ,color=secondary, width=100,color_continuous_scale=px.colors.cyclical.IceFire, height=700)

       st.plotly_chart(fig1, use_container_width=True)