import streamlit as st
from plotly.offline import plot
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import statsmodels.api as sm

st.set_page_config(layout="wide")
st.title("Pourquoi Plotly est génial")

st.write("##")
st.subheader("Installation : ")
_, c, _ = st.columns((0.5,1,0.5))
with c:
        st.code(language="python", body="pip install plotly")
        st.code(language="python",
                body="""
from plotly.offline import plot
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go""")

st.write("##")

# Courbe simple
# Ajout de texte + flêches

st.subheader("Courbe simple")
_, c, _ = st.columns((0.5,1,0.5))
with c:
        st.code(language="python",
            body="""
x = np.linspace(-5, 5, 100)
y = 1/(1+np.exp(-x))

fig = go.Figure()
fig.add_scatter(x=x,y=y,mode='lines',
                name='sigmoid',
                marker=dict(color='green'))
fig.add_annotation(x=0, y=0.5,
                   text='point en x=0',
                   showarrow=True,
                   arrowhead=1,
                   arrowsize=1,
                   arrowwidth=2,
                   arrowcolor='black',
                   bgcolor="orange",
                   borderwidth=1,
                   yshift=10)
plot(fig)
        """)

        st.write("##")

        x = np.linspace(-5, 5, 100)
        y = 1 / (1 + np.exp(-x))

        fig = go.Figure()
        fig.add_scatter(x=x, y=y, mode='lines',
                        name='sigmoid',
                        marker=dict(color='green'))
        fig.add_annotation(x=0, y=0.5,
                           text='point en x=0',
                           showarrow=True,
                           arrowhead=1,
                           arrowsize=1,
                           arrowwidth=2,
                           arrowcolor='black',
                           bgcolor="orange",
                           borderwidth=1,
                           yshift=10)
        fig.update_layout(
            font=dict(size=10),
            width=1000, height=750,
            margin=dict(l=40, r=40, b=40, t=40),
        )
        st.plotly_chart(fig)
        st.write("##")
st.write("---")

# 3D

st.subheader("3D graphiques")
_, c, _ = st.columns((0.5,1,0.5))
with c:
        st.code(language="python",
            body="""
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species', size='petal_length', size_max=18,symbol='species', opacity=1)
plot(fig)
        """)

        st.write("##")
        df = px.data.iris()
        fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
                            color='species', size='petal_length', size_max=18, symbol='species', opacity=1)
        fig.update_layout(
            font=dict(size=10),
            autosize=False,
            width=1000, height=750,
            margin=dict(l=40, r=40, b=40, t=40),
        )
        st.plotly_chart(fig)
        st.write("##")
st.write("---")

# Slider

st.subheader("Slider")
_, c, _ = st.columns((0.5,1,0.4))
with c:
        st.code(language="python",
            body="""
df = px.data.gapminder()
df_fr=df[df['country']=='France']
df_us=df[df['country']=='United States']
df = pd.concat([df_fr, df_us])

fig = px.scatter(df,
        y="gdpPercap",
        x="year",
        color="country",
        title="évolution pib france et USA",
        range_x=[1952,2007],
        range_y=[df['gdpPercap'].min(), df['gdpPercap'].max()],
        animation_frame="year")
plot(fig)
        """)

        st.write("##")

        df = px.data.gapminder()
        df_fr = df[df['country'] == 'France']
        df_us = df[df['country'] == 'United States']
        df = pd.concat([df_fr, df_us])

        fig = px.scatter(df,
                         y="gdpPercap",
                         x="year",
                         color="country",
                         title="évolution pib france et USA",
                         range_x=[1952, 2007],
                         range_y=[df['gdpPercap'].min(), df['gdpPercap'].max()],
                         animation_frame="year")
        fig.update_layout(
            font=dict(size=10),
            width=1000, height=750,
            margin=dict(l=40, r=40, b=40, t=40),
        )
        st.plotly_chart(fig)
        st.write("##")
st.write("---")


# Marges statistiques

st.subheader("Marges statistiques")
_, c, _ = st.columns((0.5,1,0.4))
with c:
        st.code(language="python",
            body="""
df = px.data.iris()
fig = px.scatter(df, x="sepal_length", # données
                 color="species", # couleur par expèce
                 marginal_x='box', # marge en boxplot
                 marginal_y='violin', # marge en violon
                 trendline="ols" # courbe de tendances
                 )
plot(fig)
        """)

        st.write("##")

        df = px.data.iris()
        fig = px.scatter(df, x="sepal_length",  # données
                         color="species",  # couleur par expèce
                         marginal_x='box',  # marge en boxplot
                         marginal_y='violin',  # marge en violon
                         trendline="ols"  # courbe de tendances
                         )
        fig.update_layout(
            font=dict(size=10),
            width=1000, height=750,
            margin=dict(l=40, r=40, b=40, t=40),
        )
        st.plotly_chart(fig)
        st.write("##")
st.write("---")


# Plages de valeurs et courbes

st.subheader("Plages de valeurs et courbes")
_, c, _ = st.columns((0.5,1,0.4))
with c:
        st.code(language="python",
            body="""
df = px.data.stocks(indexed=True)
fig = px.line(df, facet_col="company",
              facet_col_wrap=2 # nombre de figure par ligne
              )
fig.add_hline( # ou vline pour verticale avec x=...
              y=1, line_dash="dot",
              annotation_text="1er janvier 2018",
              annotation_position="bottom right")

fig.add_vrect( # ou hrect pour horizontal
              x0="2018-09-24", x1="2018-12-18",
              col=2, # numéro de la colonne (les figures de droites)
              annotation_text="24/09 au 18/12 2018",
              annotation_position="top left",
              fillcolor="red", opacity=0.2, line_width=0.1)

fig.add_hrect( # ou hrect pour horizontal
              y0=1.1, y1=1.7,
              col=1, # numéro de la colonne (les figures de droites)
              annotation_text="1.1 à 1.7",
              annotation_position="top right",
              fillcolor="blue", opacity=0.15, line_width=0.4)

plot(fig)
        """)

        st.write("##")

        df = px.data.stocks(indexed=True)
        fig = px.line(df, facet_col="company",
                      facet_col_wrap=2  # nombre de figure par ligne
                      )
        fig.add_hline(  # ou vline pour verticale avec x=...
            y=1, line_dash="dot",
            annotation_text="1er janvier 2018",
            annotation_position="bottom right")

        fig.add_vrect(  # ou hrect pour horizontal
            x0="2018-09-24", x1="2018-12-18",
            col=2,  # numéro de la colonne (les figures de droites)
            annotation_text="24/09 au 18/12 2018",
            annotation_position="top left",
            fillcolor="red", opacity=0.2, line_width=0.1)

        fig.add_hrect(  # ou hrect pour horizontal
            y0=1.1, y1=1.7,
            col=1,  # numéro de la colonne (les figures de droites)
            annotation_text="1.1 à 1.7",
            annotation_position="top right",
            fillcolor="blue", opacity=0.15, line_width=0.4)

        fig.update_layout(
            font=dict(size=10),
            width=1000, height=750,
            margin=dict(l=40, r=40, b=40, t=40),
        )
        st.plotly_chart(fig)
        st.write("##")
st.write("---")