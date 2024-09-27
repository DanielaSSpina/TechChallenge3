import streamlit as st
import pandas as pd
import numpy as np

st.title('Dados PNAD Covid')
st.subheader('Objetivo do Projeto')
st.markdown ('Este projeto tem como finalidade analisar o comportamento da população durante a pandemia de COVID-19 utilizando o estudo PNAD-COVID-19 disponível no IBGE como base de dados.')
st.markdown('A partir dessa análise, identificaremos indicadores importantes para o planejamento e resposta a possíveis futuros surtos da doença.') 
st.markdown('''Teremos como norteador em nossa busca os seguintes itens relevantes: \n 
•	Características clínicas dos sintomas; \n 
•	Características da população; \n 
•	Características econômicas da sociedade; \n ''')
st.markdown('Utilizaremos 20 perguntas realizadas pelo IBGE, buscando construir uma solução para 3 meses tendo como ferramentas de apoio o Google Cloud para a conexão e tratamento inicial do banco de dados do IBGE e o Power BI para melhor transformação e visualização dos dados.')

st.subheader('Extração dos dados')
st.markdown('A extração de dados foi realizada a partir da base PNAD COVID-19, disponibilizada pelo IBGE e acessada através da plataforma GoogleCloud. Essa ferramenta permitiu o acesso a grandes volumes de dados de forma fácil. Esta base contém informações sobre os impactos da pandemia de COVID-19 no Brasil, abrangendo aspectos demográficos, socioeconômicos e de saúde.')
st.markdown('Os períodos filtrados para a análise abrangem os meses de junho, julho e agosto de 2020, pelos seguintes motivos:')
st.markdown('''**•	Infecções:** \n
Em junho o Brasil já ultrapassava 1 milhão de casos confirmados, com mais de 30 mil novos casos diários em média.
julho foi o mês com o maior número de infecções até então, a média de novos casos diários superava 40 mil.
Em agosto a taxa de crescimento ainda era alta, mas começava a mostrar sinais de desaceleração.''')
st.markdown('''**•	Internações:**\n
Em junho e julho as taxas de ocupação de leitos de UTI variaram bastante entre os estados, mas em muitos locais, a taxa de ocupação ultrapassava 80%, especialmente nas capitais.
Em agosto alguns estados do Norte e Nordeste, que haviam sido os primeiros a ser fortemente afetados, começaram a ver uma diminuição nas internações, enquanto o Sul e Sudeste ainda enfrentavam alta demanda por leitos hospitalares.''')
st.markdown('''**•	Testes:**\n
Em junho o Brasil estava ampliando a capacidade de testagem, porém em muitos estados, o teste era direcionado a pessoas com sintomas graves, e a subnotificação era um problema.
Em julho o número de pessoas testadas ainda era inferior ao ideal para monitorar de forma abrangente a pandemia.
Em agosto começou a aumentar o uso de testes rápidos e RT-PCR, mas a distribuição desigual dos testes dificultava o controle preciso da situação em várias regiões.''')
st.markdown('''**•	Óbitos:** \n
Em junho a taxa de óbitos ultrapassou a marca de 50 mil mortes por COVID-19.
Em julho passou de 90 mil óbitos e chegou a registrar uma média móvel diária de cerca de 1.000 mortes.
Em agostos começa a desaceleração dos óbitos, porém ultrapassou 120 mil mortes até o final do mês.''')

st.subheader('Preparação dos dados')
st.markdown('Para a preparação dos dados foi essencial realizar algumas consultas e transformações para garantir a qualidade e a consistência dos dados, utilizamos para as transformações os dicionários disponibilizados pelo IBGE, utilizando o PowerBI para realizar conexões de código e significado, para dessa forma conseguirmos extrair as informações do estudo.')