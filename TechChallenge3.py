import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

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
st.markdown('''Para a preparação dos dados foi essencial realizar algumas consultas e transformações para garantir a qualidade e a consistência dos dados, utilizamos para as transformações os dicionários disponibilizados pelo IBGE, utilizando o Power BI criamos uma query para unificar as bases do Excel com o gabarito das respostas e consolidamos em formato de banco de dados. \n 
Após toda transformação nós consultamos essa base como apoio para transformar os micros dados que estavam em formato numeral.''')
st.subheader('Análise interativa - Painel')
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMDdiMGMzMzEtMmMzYS00Njk1LTg3OTQtNDI3YjI2NjU0ZGFiIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9&pageName=0070333d34b73a58a60f"
st.markdown(
    f"<div style='display: flex; justify-content: center;'><iframe src='{power_bi_url}' width='800' height='800' frameborder='0' allowFullScreen='true'></iframe></div>",
    unsafe_allow_html=True
)
st.markdown('''O painel apresentado acima oferece uma visão interativa dos dados, permitindo que os usuários explorem informações de forma dinâmica e visual. \n
Os gráficos e visualizações permitem uma interpretação intuitiva, facilitando a análise por diferentes segmentos e variáveis.
Além do painel acima, preparamos uma análise descritiva que destaca pontos importantes, proporcionando o entendimento sobre os dados obtidos.''')

st.subheader('Análise primária')
st.markdown('•	**Amostra da população**')
st.markdown('''Nos três meses selecionados, possuímos 2.650.459 pessoas respondendo o a pesquisa, sendo 48% homens e 52% mulheres.\n
Dentre essa amostra, 49% dos respondentes são pardos, 42% são brancos, 8% são pretos, 1% são amarelos e indigenas e menos de 1% não informou como se classifica. \n
A maior parte dos respondentes estão nos estados: Minas Gerais, São Paulo e Rio de Janeiro \n
75% dos respondentes informaram não se enquadrar na pergunta "frenquenta escola", 31% deles não possui o fundamental completo, 23% possuí o ensino médio completo e 11% possuí superior completo.   ''')
st.markdown('•	**Amostra econômica**')
st.markdown('''76% dos respondentes informam ser autonomos, ou seja não tem carteira assinada, 14% possuem carteira de trabalho assinada, 6% não possuem carteira de trabalho assinada e 4% são servidores públicos.\n
Somente 3% dos respondentes informaram ter trabalhado de home office.\n
76% dos respondentes não possuem plano de saúde, 23% possuem plano de saúde e menos de 1% não respondeu a pergunta.\n
Dentre os respondentes 6% trabalham no setor de agricultura/pecuária e 5% no comércio atacado/varejo.''')
st.markdown('•	**Sintomas**')
st.markdown('''Dentre todas as perguntas, selecionamos cinco dos principais sintomas da covid-19, sendo eles:\n
•	Febre: Somente 1% dos respondentes teve este sintoma.\n
•	Dor de garganta: Somente 2% dos respondentes teve esse sintoma.\n
•	Dificuldade para respirar: Somente 1% dos respondentes teve este sintoma.\n
•	Nariz entupido: Somente 2% dos respondentes teve esse sintoma.\n
•	Perda de olfato/paladar: Somente 1% dos respondentes teve este sintoma.\n
Trouxemos também três perguntas a respeito do comportamento das pessoas que apresentaram sintomas:\n
•	Foi a um hospital do SUS: Menos de 1% foi ao hospital do SUS.\n
•	Ficou internado:Menos de 1% foi ao hospital do SUS.\n
•	Tomou remédio por orientação médica:Menos de 1% foi ao hospital do SUS.\n
Para finalizar, também trouxemos duas perguntas vinculadas a teste de covid-19:\n
•	Fez teste via coleta sanguínea: 2% fizeram teste via coleta sanguínea.\n
•	Qual foi o resultado do teste: Dentre estes que fizeram teste, 28% testaram positivo para covid.''')
st.subheader('Análise foco - gênero')
st.markdown('•	**Homens**')
st.markdown('''Dentre os homens respondentes, 49% são pardos, 41% são brancos, 8% são pretos, 9% são amarelos ou indígenas.\n
            28% dos homens que tiveram teste positivo para covid possuem o ensino médio completo.\n
            A maior parte dos homens que positivaram para covid moram no Maranhão e são pardos.
            66% dos homens que positivaram não possuem plano de saúde.
            23% dos homens que positivaram possuem carteira assinada e 9% são servidores públicos.
            Dos homens que positivaram 7% apresentaram febre, 5% apresentaram dor de garganta, dificuldade para respirar, nariz entupido e perda de olfato/paladar.
            ''')
st.markdown('•	**Mulheres**')
st.markdown('''Dentre as mulheres respondentes, 48% são pardos, 43% são brancos, 8% são pretos, 1% são amarelos ou indígenas.
            
            28% das mulheres que tiveram teste positivo para covid possuem o ensino médio completo.
            A maior parte das mulheres que positivaram para covid moram no Maranhão e são pardas.
            67% das mulheres que positivaram não possuem plano de saúde.
            19% dos mulheres que positivaram possuem carteira assinada e 11% são servidoras públicas.
            Das mulheres que positivaram 7% apresentaram febre e perda de olfato/paladar, 6% apresentaram dor de garganta, 5% dificuldade para respirar e nariz entupido.
            ''')
st.subheader('Conclusão')
st.markdown('A dos dados nos ajuda a entender a urgência na ação para apoiar a população que se encontram em situação de vulnerabilidade social.Caso presenciemos outra pandemia será crucial que haja esforço para auxiliar a população sem fonte de renda, pois muitas demissões e recisões de contrato ocorreram neste período, pois a ausência de rendo além de agravar a desigualdade social, precariza ainda mais cuidados básicos como acesso a alimentação, testes, medicamentos e itens básicos de higiene, que são fundamentais para evitar a proliferação de vírus.Para isso será necessário uma análise ágil e em tempo real do mercado para que políticas de assistência sejam eficazes, garantindo que haja recursos para quem precisar, temos como exemplo programas de auxílio emergencial, distribuição de alimentos e acesso a serviços de saúde que ocorreram durante a pandemia de covid-19, porém esses tiveram um longo período de discussão, tendo problemas em cadastros e demora na liberação dos benefícios.')
st.markdown('Além do que já ocorreu, é importante refletir sobre ações de preparo para futuras pandemias, abaixo algumas sugestões:')
st.markdown('''•	**Reforço na saúde:**
Em âmbito de saúde, existem três pilares principais para prevenir impactos de uma nova pandemia.
            
            1 - Capacidade Hospitalar: Expansão e modernização os sistemas de saúde pública, com mais leitos de UTI, ventiladores e pessoal médico capacitado, pois a superlotação foi um grande problema durante a COVID-19. /n
            2 - Prevenção e Diagnóstico Rápido e tecnológico: Fortalecer e modernizar os mecanismos de monitoramento de sintomas para detectar de forma mais ágil a possibilidade de surtos no sistema público e privado, maior agilidade na disponibilização de testagem em massa e disseminação de informação para conter a disseminação.
            3 - Distribuição de Equipamentos de Proteção: Garantir que hospitais, profissionais de saúde e a população tenham acesso imediato a EPIs (máscaras, luvas, álcool, etc.)''')
st.markdown('''•	**Vacinação e Educação:** 
            
            1 - Vacinação: Desenvolver uma infraestrutura para a pesquisa, produção e distribuição de vacinas, para que o processo de vacinação em massa seja mais eficiente.
            2 - Educação em Saúde Pública: Disponibilizar programas de educação com comunicação clara e objetiva, para garantir que não haja desinformação a nenhum nível e também que a população entenda a importância de práticas como distanciamento social, uso de máscaras e qualquer outra medida necessária.''')
st.markdown('''•	**Apoio Econômico e Proteção Social:**
            
            1 - Auxílio Econômico Rápido: Desenvolver mecanismos para implementar rapidamente medidas de auxílio financeiro em caso de crise, sem burocracia excessiva, sendo assim mais ágil e abrangente.
            2 - Incentivo ao Emprego Formal: Fortalecer políticas que incentivem a formalização do trabalho, garantindo maior proteção social a trabalhadores informais, que foram os mais afetados economicamente.''')
st.markdown('''•	**Digitalização e Infraestrutura Tecnológica:**
            
            1 - Digitalização: Expansão de serviços governamentais online, como sistemas de cadastramento e pagamento de benefícios sociais, permitindo acesso rápido e seguro, evitando filas e aglomerações.
            2 - Tecnologias para Educação e Trabalho Remoto: Melhorar a infraestrutura digital para que mais pessoas possam trabalhar e estudar remotamente durante períodos de crise, minimizando os impactos econômicos e sociais''')
st.markdown('''•	**Investimento em Ciência, Pesquisa e Educação:**
           
            1 - Pesquisa, Desenvolvimento e Educação: Aumentar o investimento na educação para formarmos cada vez mais cientistas e médicos, assim como reforçar o financiamento para pesquisas nas áreas de saúde, vacinas e tratamento de doenças infecciosas, para que o país tenha capacidade de resposta científica rápida em novas pandemias.
            2 - Capacitação de Profissionais: Expandir a formação de cientistas, médicos e profissionais da saúde, além de apoiar colaborações entre universidades, governo e setor privado para encontrar soluções inovadoras.''')
st.markdown('Todas essas ações citadas acima, são meios de diminuir a desigualdade social, desinformação e vulnerabilidade tecnológica, afim de termos um mapeamento rápido e deixar toda a linha de decisão ciente antes da doença estar já em estado avançado em toda a população.')
st.subheader('Bibliografia')
st.markdown('''1 - Lições e legados do auxílio emergencial para o fortalecimento da proteção social - https://brasil.un.org/pt-br/170560-artigo-li%C3%A7%C3%B5es-e-legados-do-aux%C3%ADlio-emergencial-para-o-fortalecimento-da-prote%C3%A7%C3%A3o-social
            
2 - Auxílio emergêncial aprovado pelo congresso - https://www12.senado.leg.br/noticias/materias/2020/12/30/aprovado-pelo-congresso-auxilio-emergencial-deu-dignidade-a-cidadaos-durante-a-pandemia
            
3 - Lições e legados do auxílio emergencial - https://brasil.un.org/pt-br/170560-artigo-li%C3%A7%C3%B5es-e-legados-do-aux%C3%ADlio-emergencial-para-o-fortalecimento-da-prote%C3%A7%C3%A3o-social

4 - Dados casos confirmados e óbitos - https://covid.saude.gov.br/
            
5 - Principais sintomas covid19 - https://www.gov.br/inss/pt-br/noticias/dengue-ou-covid-sintomas-das-duas-doencas-sao-parecidos-fiquem-alertas-1#:~:text=J%C3%A1%20a%20Covid%2D19%20%C3%A9,e%20dificuldade%20para%20se%20alimentar.''')
