# Lab 01 - Um estudo das características de qualidade de sistema java

Integrantes:

- Fernando Couto
- Tito Chen
- Vinicius Lima

## Introdução

**Objetivo**:
Nosso objetivo nesta pesquisa é analisar a qualidade do código e a maturidade dos repositórios mais populares no GitHub, especificamente aqueles desenvolvidos na linguagem Java. A partir de hipóteses informais, esperamos que repositórios com maior número de estrelas (indicador de popularidade) apresentem melhores métricas de qualidade de código, como coesão, acoplamento e herança, além de possuírem maior número de linhas de código (LOC) e um ciclo de lançamentos mais frequente.

**Linguagem de programação**: Python 3

**Dependências**:

- matplotlib (gráficos)
- requests (chamadas http para GitHub API)
- csv (salvar o csv com os dados)  
- pandas (leitura do csv gerado)
- subprocess (rodar comandos de git clone e processar o ck)

**API utilizada**: Foi utilizada a GitHub API para coletar os dados necessários dos repositórios


## Hipóteses informais
- Repositórios com mais estrelas terão métricas de qualidade de código superiores (menor acoplamento, maior coesão e profundidade de herança mais eficiente).
- Repositórios com mais lançamentos serão mais maduros em termos de LOC e melhores práticas de código.
- Repositórios mais antigos terão métricas de qualidade de código mais aprimoradas devido à evolução contínua ao longo do tempo.

## Metodologia
### Coleta de Dados:
Utilizamos a API do GitHub para coletar os 1000 repositórios mais populares em Java, com base no número de estrelas. Para cada repositório, extraímos informações como o número de estrelas, lançamentos e a idade do repositório.

### Análise de Métricas de Código:
Utilizamos a ferramenta CK para calcular métricas de código, como:

- CBO (Coupling Between Objects) – Indicador de acoplamento.
- DIT (Depth of Inheritance Tree) – Profundidade da árvore de herança.
- LCOM* (Lack of Cohesion of Methods) – Falta de coesão entre os métodos.
- LOC (Lines of Code) – Linhas de código.

### Processamento dos Dados: 
Combinamos as métricas de qualidade de código com os dados coletados da API do GitHub para gerar um arquivo CSV. Um passo adicional foi feito para calcular a idade dos repositórios e incluir essa informação no CSV.

### Análise Estatística:
Calculamos as médias das métricas de qualidade de código e comparamos esses valores com a popularidade (número de estrelas) e a idade dos repositórios para validar as hipóteses.

## Resultados
#### RQ 01. Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?
Repositórios muito populares, com pelo menos 50.000 estrelas, tendem a apresentar métricas de qualidade de código mais favoráveis. Esses repositórios têm maior visibilidade e, por isso, atraem uma comunidade ativa de colaboradores e revisores. Isso resulta em práticas de desenvolvimento mais rigorosas, como revisões de código mais frequentes, testes automatizados, e a necessidade de manter a qualidade do código para facilitar futuras contribuições. Esses fatores ajudam a reduzir métricas como CBO, DIT e LCOM, já que o código é mais frequentemente revisado e melhorado para garantir que permaneça compreensível, coeso e modular.

Além disso, a popularidade de um repositório pode estar ligada ao uso de boas práticas desde o início do projeto, o que atrai mais desenvolvedores qualificados que seguem padrões elevados de qualidade. Com mais pessoas observando e contribuindo, é comum que haja um esforço contínuo para manter a arquitetura limpa e evitar o acúmulo de "dívida técnica", o que contribui para métricas de qualidade mais baixas.

![Gráfico](rq01_cbo_grouped.png)
![Gráfico](rq01_dit_grouped.png)
![Gráfico](rq01_lcom_grouped.png)

#### RQ 02. Qual a relação entre a maturidade do repositórios e as suas características de qualidade ?

Projetos mais antigos tendem a ter uma qualidade menor. Essa tendência pode ser explicada pela evolução natural de sistemas ao longo do tempo. À medida que um repositório cresce e é mantido por diferentes desenvolvedores, novas funcionalidades são adicionadas e alterações são feitas sem necessariamente refatorar ou melhorar o design original. Isso leva a um aumento no acoplamento entre classes (CBO), à introdução de hierarquias de herança mais profundas (DIT) e à menor coesão entre métodos em classes (LCOM), à medida que o código se torna mais complexo e difícil de manter.

Além disso, repositórios mais antigos frequentemente têm código legado que pode não seguir as melhores práticas modernas de desenvolvimento. Sem revisões adequadas e práticas como refatoração contínua, é comum que a qualidade do design se degrade com o tempo, resultando em valores mais altos dessas métricas de qualidade.

![Gráfico](rq02_cbo_grouped.png)
![Gráfico](rq02_dit_grouped.png)
![Gráfico](rq02_lcom_grouped.png)

#### RQ 03. Qual a relação entre a atividade dos repositórios e as suas características de qualidade?
Observamos que projetos com maior atividade tendem a apresentar uma deterioração nas suas métricas de qualidade. Acreditamos que isso está diretamente relacionado ao aumento do tamanho dos repositórios; à medida que um projeto se torna mais ativo, seu crescimento em termos de código e complexidade também aumenta. Essa expansão pode dificultar a gestão e a manutenção das boas práticas de desenvolvimento, resultando em métricas de qualidade menos favoráveis. Portanto, a relação entre a atividade do projeto e a complexidade associada ao seu tamanho pode ser um fator crucial para entender essa deterioração. 

![Gráfico](rq03_cbo_grouped.png)
![Gráfico](rq03_dit_grouped.png)
![Gráfico](rq03_lcom_grouped.png)


#### RQ 04. Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?

Podemos observar uma relação direta entre o tamanho dos repositórios e o CBO (Coupling Between Objects) e o DIT (Depth of Inheritance Tree). À medida que o repositório cresce, tende a aumentar o nível de acoplamento e herença entre classes. Muito provavelmente, pois um maior número de linhas de código geralmente implica um maior número de classes. Como resultado, há uma maior probabilidade de interações entre essas classes, o que eleva o acoplamento.

Além disso, também observamos que projetos de maior dimensão tendem a apresentar uma maior falta de coesão entre as classes. Essa tendência pode ser atribuída às dificuldades inerentes à gestão de um projeto mais extenso, onde a complexidade organizacional aumenta. Em grandes repositórios, a comunicação entre diferentes partes do código pode se tornar menos eficiente, resultando em classes que, em vez de trabalharem de maneira coesa em torno de uma única responsabilidade, acabam se espalhando por diversas funcionalidades.

![Gráfico](rq04_cbo_grouped.png)
![Gráfico](rq04_dit_grouped.png)
![Gráfico](rq04_lcom_grouped.png)
