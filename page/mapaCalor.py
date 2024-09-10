import streamlit as st
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch, VerticalPitch
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import pandas as pd

def arrumarValoresX(x):
    return (((x * 100)/30)*100)/100
    
def arrumarValoresY(y):
    return (((y * 100)/18)*63)/100

def mapaDeCalor(df):
    valoresX = arrumarValoresX(df['X'])
    valoresY = arrumarValoresY(df['Y'])
    

    fig, ax = plt.subplots()

    pitch = VerticalPitch(pitch_type='custom',
                    pitch_color='#008000',
                    line_color='black',
                    axis=True,
                    pitch_length= 105,
                    pitch_width=68,
                    line_zorder=2,
                    linewidth=1)
                          
    pitch.draw(constrained_layout=False, 
               ax=ax)
    colors = ['#008000', '#69b500', '#faeb00', '#f00000'] 
    cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

    kde = sns.kdeplot(
        x=valoresY,
        y=valoresX,
        fill=True,
        alpha=1,
        levels= 100,
        cmap=cmap,
        ax=ax,
        bw_adjust=0.58

        
    )

    titleFont = {
            'family': 'sans-serif',
            'weight': 'normal',
            'size': 11,
        }
    plt.title(F'Mapa de Calor / {len(valoresX)} Ações', fontdict=titleFont)
    
    ax.set_ylim(0, 105)
    ax.set_xlim(68, 0) 
    return st.pyplot(fig, use_container_width=True)
