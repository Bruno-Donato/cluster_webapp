import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

pd.set_option('display.float_format', lambda x: '%.2f' % x)


df_usuarios = pd.read_feather('data/df_usuarios.feather')
df_loc = pd.read_feather('data/df_loc.feather')
df_clusters = pd.read_feather('data/df_clusters.feather')
df_mkt = pd.read_feather('data/df_mkt.feather')
df_turno_pedido = pd.read_feather('data/df_turno_pedido.feather')
df_mais_pedidas = pd.read_feather('data/mais_pedidas.feather')


st.set_page_config(
    page_title="Segmentação Clientes Ifood",
    layout="wide",
)

st.write("<div align='center'><h1><b>Segmentação de Clientes Ifood</b></h1></div>", unsafe_allow_html=True)

st.write("<div align='center'><h2><i>Ciência de Dados & Machine Learning</i></h2></div>", unsafe_allow_html=True)

st.markdown("""<div style='text-align: center;'><hr style='border-top: 5px solid black'></div>""", unsafe_allow_html=True)

st.write("""
         Desafio proposto pela escola Tera no curso de Ciência de Dados & Machine Learning, no qual o objetivo é encontrar grupos de 
         clientes semelhantes utilizando Clusterização, que é um tipo de modelo não supervisionado de machine learning.
         """)

st.write("""
        Com esse tipo de modelo é possível encontrar grupos de clientes que compartilham características similares, e neste contexto 
        é uma ferramenta extremamente importante pois precisamos entender melhor os clientes para poder direcionar melhor os recursos, 
        propagandas e ações e assim otimizar a experiência do cliente.
        """)

st.write("""
         Para isso devemos levantar, e tentar responder as seguintes quetões:
         - Quem é o mais fiel e quem mais compra no ifood? Quem mais gosta de cupom?
         - Quem gosta de entrega grátis? Qual o padrão de consumo?
         - Qual o padrão de comportamento? Quanto os clientes vão gastar? Onde?
         """)

st.write("""
         A análise feita com dados referente ao período de 20/02/2022
         """)

st.markdown("""<div style='text-align: center;'><hr style='border-top: 5px solid black'></div>""", unsafe_allow_html=True)


tab1, tab2 = st.tabs(["__DASHBOARD__", "__MODELOS DE CLUSTERIZAÇÃO__"])

with tab1:
    col1, col2 , col3 = st.columns([2, 3, 1])
    with col1:
        fig = px.bar(df_usuarios, x = 'Usuários', y = 'Total', hover_data= '%', 
                    color = 'Usuários')
        
        fig.update_layout(
            title='Usuários registrados',
            xaxis_title="",
            yaxis_title="Contagem",
            height = 300)
        
        fig.update(layout_showlegend=False)

        col1.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.histogram(df_mkt, x = 'registration_date', range_x=('2010',' 2020'))

        fig2.update_layout(
            title="Data do registro na plataforma",
            xaxis_title="",
            yaxis_title="Contagem",
            height = 300)
        
        col2.plotly_chart(fig2, use_container_width=True)

    with col3:
        st.metric(label = 'Total de Clientes', value = 20.249)
        
        st.metric(label = 'Total de Pedidos', value = 226.269)
        
        st.metric(label = 'Receita', value = 'R$ 13.6 Bi')


    col1, col2, col3 = st.columns([2.5, 2.5, 1])
    with col1:    
        # MUDAR LEGENDA PARA PORTUGUES
        df_status = df_mkt.groupby('ifood_status_last_month').size().to_frame().reset_index().sort_values(0, ascending=False)
        df_status.rename(columns = {0 : 'contagem'}, inplace = True)
        fig3 = px.bar(df_status, x = 'ifood_status_last_month', y = 'contagem', color = 'ifood_status_last_month')
        
        fig3.update_layout(
            title="Status conta no mês anterior",
            xaxis_title="",
            yaxis_title="Contagem",
            height = 300)
        
        fig3.update(layout_showlegend=False)

        col1.plotly_chart(fig3, use_container_width=True)

    with col2:    
        # MUDAR LEGENDA PARA PORTUGUES
        df_status = df_mkt.groupby('ifood_status').size().to_frame().reset_index().sort_values(0, ascending=False)
        df_status.rename(columns = {0 : 'contagem'}, inplace = True)
        fig4 = px.bar(df_status, x = 'ifood_status', y = 'contagem', color = 'ifood_status')
        
        fig4.update_layout(
            title="Status conta atual",
            xaxis_title="",
            yaxis_title="Contagem",
            height = 300)
        
        fig4.update(layout_showlegend=False)

        col2.plotly_chart(fig4, use_container_width=True)

    with col3:
        st.metric(label = 'Valor por compra (média)', value = 'R$ 60')
        
        st.metric(label = 'Taxa de entrega (média)', value = 'R$ 4')
        
        st.metric(label = 'Recencia (média)', value = '2 dias')

    col1, col2 = st.columns([1, 1])
    with col1:
        # MUDAR LEGENDA PARA PORTUGUES
        fig = px.bar(df_turno_pedido, y='order_shift', x = 'count',
                        category_orders={'order_shift': df_turno_pedido['order_shift'][::-1]})
        
        fig.update_layout(
            title="Período do pedido",
            xaxis_title="Contagem",
            yaxis_title="",
            height = 280)

        col1.plotly_chart(fig, use_container_width=True)
        
    with col1:
        fig2 = px.bar(df_mais_pedidas, y='dish_type', x = 'count',
                        category_orders={'dish_type': df_mais_pedidas['dish_type'][::-1]})
        
        fig2.update_layout(
            title="Tipo de prato mais pedidos",
            xaxis_title="Contagem",
            yaxis_title="",
            height = 280)

        col1.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig = px.scatter_mapbox(df_loc, lat='customer_lat', lon='customer_long', hover_name='city')

        fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=3, title = 'Distribuição de Vendas',
                        autosize=True, width=610,height=600, mapbox_center={"lat": -14.2350, "lon": -51.9253})
        
        col2.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns([1, 2])

    option = col1.selectbox(
        'Selecione o modelo de Clusterização',
        ("1 - Kmeans", "2 - Kprototypes", "3 - DBSCAN", "4 - Agglomerative", "5 - Gaussian Mixture"))


    def resumo(item):
        df_total = df_clusters[item].value_counts().to_frame().reset_index()
        
        df_percent = (df_clusters[item].value_counts()/df_clusters.shape[0]*100).to_frame().reset_index()
        
        df_contagem = df_total.merge(df_percent, how = 'inner', on = item)
        df_contagem.columns = [item, 'Total', '%']
        
        df = df_clusters.groupby(item)[['Total Pago', 'Total Taxa de Entrega', 
                                                    'Total Subsidio', 'Frequencia', 'Recencia',
                                                    'Tempo de Vida', 'Total de Pedidos']].mean()

        df.reset_index(inplace = True)
        df_novo = df_contagem.merge(df, how = 'inner', on = item)
        
        df_order_shift = df_clusters.groupby(item)['Período do Pedido'].value_counts().groupby(level=0).head(1).to_frame().reset_index()
        df_device_platform = df_clusters.groupby(item)['Dispositivo'].value_counts().groupby(level=0).head(1).to_frame().reset_index()
        df_dish_type = df_clusters.groupby(item)['Tipo de Comida'].value_counts().groupby(level=0).head(1).to_frame().reset_index()
        df_has_free_delivery = df_clusters.groupby(item)['Entrega Grátis'].value_counts().groupby(level=0).head(1).to_frame().reset_index()
        
        df_resumo = df_order_shift.iloc[:, :2].merge(df_device_platform.iloc[:, :2], how = 'left', on = item)
        df_resumo = df_resumo.merge(df_dish_type.iloc[:, :2], how = 'left', on = item)
        df_resumo = df_resumo.merge(df_has_free_delivery.iloc[:, :2], how = 'left', on = item)
        
        df_completo = df_novo.merge(df_resumo, how = 'inner', on = item)
        df_completo[item] = df_completo[item].apply(lambda x: "{} {}".format('Cluster', x))
        df_completo = df_completo.sort_values(item)
        df_completo.set_index(item, inplace = True)
        df_completo.rename_axis(index=None, inplace = True)  
        
        return df_completo


    if option == "1 - Kmeans":
        st.dataframe(resumo('K-Means'))

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("""
                    __Cluster 0 - Clientes de baixo valor__
                    - 12.640 clientes (91%)
                    - Valor total pago: R$ 462 (média)
                    - Pedidos no período: 7 (média) 
                    - Recencia: 84 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Janta final de semana
                    - Prato mais pedido: Lanche
                    """)

        with col2:
            st.write("""
                    __Cluster 1 - Clientes de alto valor__
                    - 211 clientes (2%)
                    - Valor total pago: R$ 13.120 (média)
                    - Pedidos no período: 240 (média)
                    - Recencia: 5 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Almoço em dias úteis
                    - Prato mais pedido: Comida brasileira
                    """)

        with col3:
            st.write("""
                    __Cluster 2 - Cliente de médio valor__
                    - 1.026 clientes (7%)
                    - Valor total pago: R$ 4.867 (média)
                    - Pedidos no período: 82 (média)
                    - Recencia: 20 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Almoço em dias úteis
                    - Prato mais pedido: Lanche
                    """)
    
    elif option == "2 - Kprototypes":
        st.write(resumo('K-Prototypes'))
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("""
                    __Cluster 0 - Clientes de alto valor__
                    - 173 clientes (1%)
                    - Valor total pago: R$ 15.591 (média)
                    - Pedidos no período: 197 (média) 
                    - Recencia: 6 dias (média)
                    - Sistema mais usado: IOS
                    - Período mais pedido: Almoço dias úteis
                    - Prato mais pedido: Comida brasileira
                    """)

        with col2:
            st.write("""
                    __Cluster 1 - Clientes de baixo valor__
                    - 12.639 clientes (91%)
                    - Valor total pago: R$ 448 (média)
                    - Pedidos no período: 8 (média)
                    - Recencia: 84 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Janta final de semana
                    - Prato mais pedido: Lanche
                    """)

        with col3:
            st.write("""
                    __Cluster 2 - Cliente de médio valor__
                    - 1.065 clientes (8%)
                    - Valor total pago: R$ 4.918 (média)
                    - Pedidos no período: 87 (média)
                    - Recencia: 19 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Almoço em dias úteis
                    - Prato mais pedido: Lanche
                    """)
        
    elif option == "3 - DBSCAN":
        st.write(resumo('DBSCAN'))
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("""
                    __Cluster -1 - Clientes de alto valor__
                    - 1.442 clientes (10%)
                    - Valor total pago: R$ 5.610 (média)
                    - Pedidos no período: 97 (média)
                    - Recencia: 37 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Almoço em dias úteis
                    - Prato mais pedido: Lanche
                    """)
        
        with col2:
            st.write("""
                    __Cluster 0 - Clientes de baixo valor__
                    - 12.415 clientes (89%)
                    - Valor total pago: R$ 439 (média)
                    - Pedidos no período: 6 (média) 
                    - Recencia: 83 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Janta final de semana
                    - Prato mais pedido: Lanche
                    """)

        with col3:
            st.write("""
                    __Cluster 1 - Cliente de médio valor__
                    - 20 clientes (0.1%)
                    - Valor total pago: R$ 3.087 (média)
                    - Pedidos no período: 48 (média)
                    - Recencia: 9 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Janta final de semana
                    - Prato mais pedido: Lanche
                    """)
        
    elif option == "4 - Agglomerative":
        st.write(resumo('Agglomerative'))
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("""
                    __Cluster 0 - Clientes de alto valor__
                    - 374 clientes (3%)
                    - Valor total pago: R$ 10817 (média)
                    - Pedidos no período: 194 (média) 
                    - Recencia: 7 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Almoço em dias úteis
                    - Prato mais pedido: Comida brasileira
                    """)

        with col2:
            st.write("""
                    __Cluster 1 - Clientes de baixo valor__
                    - 12.574 clientes (90%)
                    - Valor total pago: R$ 447 (média)
                    - Pedidos no período: 7 (média)
                    - Recencia: 84 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Janta final de semana
                    - Prato mais pedido: Lanche
                    """)

        with col3:
            st.write("""
                    __Cluster 2 - Cliente de médio valor__
                    - 929 clientes (7%)
                    - Valor total pago: R$ 4.254 (média)
                    - Pedidos no período: 69 (média)
                    - Recencia: 22 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Almoço em dias úteis
                    - Prato mais pedido: Lanche
                    """)
        
    else:
        st.write(resumo('Gaussian Mixture'))
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("""
                    __Cluster 0 - Clientes de baixo valor__
                    - 13.377 clientes (96%)
                    - Valor total pago: R$ 650 (média)
                    - Pedidos no período: 10 (média) 
                    - Recencia: 81 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Janta final de semana
                    - Prato mais pedido: Lanche
                    """)

        with col2:
            st.write("""
                    __Cluster 1 - Clientes de alto valor__
                    - 500 clientes (4%)
                    - Valor total pago: R$ 9.803 (média)
                    - Pedidos no período: 171 (média)
                    - Recencia: 10 dias (média)
                    - Sistema mais usado: ANDROID
                    - Período mais pedido: Almoço em dias úteis
                    - Prato mais pedido: Comida brasileira
                    """)
    
    link = "https://github.com/Bruno-Donato/cluster_desafio_tera/blob/main/desafio_cluster.ipynb"
        text = "Análise Completa - Link"
        markdown = f'<a href="{link}" target="_blank">{text}</a>'
        st.markdown(markdown, unsafe_allow_html=True)