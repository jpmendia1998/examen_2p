import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    df = pd.read_excel('recursos/Volve production data-1.xlsx', sheet_name='Daily Production Data')
    df['DATEPRD'] = pd.to_datetime(df['DATEPRD'])
    return df

df = load_data()

st.title('Historial de producción del Campo Volve')
st.write("""
    El campo Volve ha sido una fuente importante de producción de petróleo y gas durante los últimos años. 
    Esta aplicación permite explorar la producción de estos recursos mediante gráficos y análisis de datos históricos.
""")


st.image('recursos/volve.ppm', caption='Campo Volve', use_column_width=True)


menu = st.sidebar.selectbox("Selecciona una opción", ['Home', 'Data', 'Plots'])

if menu == 'Home':
    st.write("Bienvenido al historial de producción del Campo Volve. Aquí podrás explorar los datos y visualizar gráficos interactivos.")

elif menu == 'Data':
    st.write("### Datos de Producción")
    st.write("Aquí puedes ver los datos históricos de producción de petróleo y gas para el Campo Volve.")
    st.dataframe(df)
#graficas
elif menu == 'Plots':
    st.write("### Gráficos de Producción")


    st.write("#### Volumen de Petróleo vs Tiempo (Años) para todos los pozos")
    fig1 = px.line(df, x='DATEPRD', y='BORE_OIL_VOL', title='Volumen de Petróleo vs Año')
    st.plotly_chart(fig1)


    st.write("#### Volumen de Gas vs Tiempo (Años) para todos los pozos")
    fig2 = px.line(df, x='DATEPRD', y='BORE_GAS_VOL', title='Volumen de Gas vs Año')
    st.plotly_chart(fig2)


    st.write("#### Volumen de Petróleo y Gas vs Tiempo (Años)")
    fig3 = px.line(df, x='DATEPRD', y=['BORE_OIL_VOL', 'BORE_GAS_VOL'], title='Volumen de Petróleo y Gas vs Año')
    st.plotly_chart(fig3)


    st.write("#### Totales de Producción por Pozo")
    df_totals = df.groupby('WELL_BORE_CODE')[['BORE_OIL_VOL', 'BORE_GAS_VOL', 'BORE_WAT_VOL']].sum().reset_index()
    fig4 = px.bar(df_totals, x='WELL_BORE_CODE', y=['BORE_OIL_VOL', 'BORE_GAS_VOL', 'BORE_WAT_VOL'], title='Totales de Producción por Pozo')
    st.plotly_chart(fig4)

with open("requirements.txst","w") as f:
    f.write("streamlit\n")
    f.write("Pandas\n")
    f.write("plotly\n")
    f.write("plotly_express\n")
