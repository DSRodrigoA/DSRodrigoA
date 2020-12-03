# Data Mining - Market Basket Analysis

**A modelagem do comportamento do cliente sempre foi - e sempre será - uma das inteligências mais buscadas por empresas que visam aumentar suas vendas, sua lucratividade e, especialmente, sua acertividade em relação ao que oferecer em suas prateleias, sejam elas físicas ou online.**

**As Regras de Associação (ou Association Rules), veio para ajudar nessa modelagem e tentar prever o comportamento de compra do cliente por meio dos dados transacionais da empresa. Basicamente, o estudo das notas fiscais, tickets e carrinhos de compra até sua conversão final.**

**A Análise de Cesta de Compras (ou Market Basket Analysis (MBA)), é uma análise exploratória de uma base de dados com histórico de transações que ajuda a explorar, limpar, filtrar, preparar e carregar em um modelo de Machine Learning, utilizando o algoritimo Apriori.**

**Utilizando inferências estatísticas de Suporte, Confiança e Elevação, o modelo basicamente analisa a base de dados em busca de itens mais frequentes em uma amostra de transações concluídas e seus respectivos consequentes, ou itens que normalmente estão juntos na mesma transação.**

**Assim, o modelo ajuda a apontar os itens mais relevantes, conhecidos também como keystone products (ou itens chave), e seus respectivos "pares", gerando insights importantes para toda uma cadeia de negócios de varejo, tais como:**

* **Cross Sell: Ajustando o layout de uma planta física de vendas, aproximando produtos que geram grupos frequentes.**
* **Vendas Online: Um sistema de recomendação para portais de venda online (ou até mesmo em espaços físicos!), tal como "Os clientes que compraram A, também compraram B)**
* **Marketing: Construção de companhas promocionais voltadas para um público específico por diversos canais e promoções que ajudam a alavancar a venda de produtos frequentes. Pode-se dizer, o aproveitamento da sinergia.**
* **Supply e Logística: Entendimento da necessidade da disponibilidade de tais produtos (keystone products) a fim de não permitir rupturas de estoque e impacto nas vendas.**   


**Nesse projeto de Data Mining desenvolvido em Python, será utilizado a biblioteca MLxtend (http://rasbt.github.io/mlxtend/), importando a função Apriori para criação dos conjuntos (itemsets) (http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/), que irá intergir com a função Association Rules para criação das listas de regras de associação com os parâmetros estatísticos (http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/association_rules/).**
