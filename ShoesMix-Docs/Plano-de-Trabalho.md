# PLANO DE TRABALHO

| Nome do Projeto:       | ShoesMix |
| ---------------------- | --------------------------------- |
| Versão:                | 1.0                              |
| Status:                | Implementação      |
| Executor Principal:    | Amanda da Silva, Brayner Santana, João Asafe Batista, João Vitor Oliveira,  Lais Samily  e Manoele Braga     |
| Coordenador Principal: | Edson Silva                  |

---

# HISTÓRICO DE VERSÕES
| Versão | Descrição                              | Autor                          | Data       |
| ------ | -------------------------------------- | ------------------------------ | ---------- |
| 1.0    | Especificação e Planejamento        | Amanda da Silva, Brayner Santana, Ebler, João Asafe Batista, João Vitor Oliveira,  Lais Samily  e Manoele Braga | 12/05/2025 |
| 1.2    |  |  |  |


---

# 1. INTRODUÇÃO
Em um cenário cada vez mais orientado pelo consumo digital, a ausência de presença online tornou-se uma das principais dificuldades para a sobrevivência e o crescimento de pequenas empresas. Muitos empreendedores ainda dependem exclusivamente de canais físicos para comercializar seus produtos, o que limita significativamente seu alcance e sua capacidade de competir em um mercado dominado por grandes marcas e plataformas digitais.
A falta de um sistema adequado para apresentar seus produtos de forma organizada e acessível ao público acaba gerando obstáculos como baixa visibilidade, vendas paradas, dificuldades no controle de estoque e menor fidelização de clientes. Esse contexto revela uma falta de alinhamento entre o comportamento atual dos consumidores que cada vez mais buscam praticidade, agilidade e informações online e a estrutura de negócios que ainda operam de maneira tradicional.
Essa realidade impõe desafios operacionais e estratégicos às pequenas empresas, ao mesmo tempo em que evidencia a urgência de soluções que promovam sua inserção no ambiente digital de forma eficiente e acessível.

## 1.1 Objetivo
O principal objetivo é desenvolver uma plataforma web para a venda de calçados masculinos e femininos, visando digitalizar o atendimento de uma empresa que atualmente realiza vendas apenas de forma presencial. O sistema tem como propósito facilitar o acesso dos clientes aos produtos da loja, permitindo a visualização, seleção e compra de calçados de maneira prática e segura pela internet. Além disso, a plataforma busca ampliar o alcance da empresa, possibilitando a expansão para novos mercados e aumentando sua visibilidade e competitividade no setor de calçados.

## 1.2 Motivação, Justificativa e Oportunidade
Muitas pequenas empresas ainda enfrentam dificuldades para se inserir no comércio digital, o que limita seu alcance e competitividade. A ausência de um sistema online para apresentar e vender produtos compromete o controle de estoque, a organização dos pedidos e a fidelização de clientes. Diante disso, este projeto representa uma oportunidade de promover a digitalização do setor varejista de calçados, oferecendo uma solução acessível que melhora a gestão interna e amplia a presença da marca no mercado.

## 1.3 Caracterização do Projeto
### 1.3.1 Classe
| Classe                 | Detalhamento                                                                                                                                 |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Aplicativo WEB | Aplicativo WEB acessado por navegadores de internet, com funcionalidades de exibição, busca e venda de calçados, além de gerenciamento de usuários e pedidos. |

### 1.3.2 Enquadrabilidade

| Enquadrabilidade  | Detalhamento                                                                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Sistema web de vendas de calçados | Está em conformidade com normas de proteção ao consumidor e regulamentações aplicáveis ao comércio eletrônico. Respeita os direitos de propriedade intelectual, privacidade de dados (conforme a LGPD) e adota medidas de segurança digital. |

### 1.3.3 Tipo
| Tipo                        | Detalhamento                                                                                                                                       |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Desenvolvimento de Software | Desenvolvimento de um sistema web para vendas de calçados, com banco de dados em nuvem, design responsivo compatível com dispositivos móveis e estrutura de navegação simplificada, priorizando a experiência do usuário e a segurança de dados. |

# 2 INFORMAÇÕES GERAIS
## 2.1 Escopo geral
O projeto envolve o desenvolvimento de uma plataforma de comércio eletrônico voltada para a venda de sapatos, com foco em funcionalidades essenciais para a navegação, compra e administração dos produtos. A solução abrangerá tanto a interface para os usuários finais quanto o painel administrativo, garantindo uma experiência eficiente e segura para ambos os perfis.
A plataforma permitirá que apenas usuários cadastrados e logados realizem compras, assegurando o controle adequado de acessos. O sistema gerenciará automaticamente o estoque dos produtos após cada venda e aplicará regras de promoções e descontos configuradas pelo administrador. Além disso, permitirá a solicitação de devoluções dentro do prazo de até 7 dias após o recebimento dos produtos, conforme definido nas regras de negócio.
O projeto também priorizará a segurança dos dados dos usuários e a alta disponibilidade da aplicação, atendendo aos requisitos não funcionais estabelecidos. A interface será responsiva, compatível com navegadores modernos e acessível tanto em dispositivos móveis quanto desktop.

### 2.2.1 Escopo Específico
- Desenvolver funcionalidades de cadastro de usuários, login e recuperação de senha, com autenticação segura.
- Implementar a busca e filtragem de produtos, com exibição organizada e intuitiva dos sapatos disponíveis para compra.
- Criar um carrinho de compras funcional, com controle automático de estoque após a finalização da compra.
- Integrar o sistema com gateways de pagamento, permitindo a realização de transações financeiras de forma segura.
- Disponibilizar uma área de acompanhamento de pedidos para que os usuários visualizem o status de suas compras.
- Implementar módulo administrativo que permita o gerenciamento de produtos, controle de estoques, visualização de vendas e configuração de promoções e descontos.
- Assegurar a segurança dos dados dos usuários, utilizando práticas como criptografia de senhas e navegação via HTTPS.
- Prover uma disponibilidade mínima de 99,5%, garantindo que o site esteja operacional de forma contínua.
- Implementar um sistema de devoluções de produtos dentro do prazo de 7 dias após o recebimento, conforme regras de negócio.

### 2.2.2 Escopo Negativo
- Avaliações e comentários de produtos por parte dos usuários não estarão disponíveis.
- Compra como visitante (sem login/cadastro) não será permitida, conforme regra de negócio.
- Integração com redes sociais (login via Google, Facebook, etc.) não será realizada inicialmente.
- Chat em tempo real com suporte ou vendedores não fará parte da primeira entrega do sistema.
- Relatórios analíticos avançados sobre vendas, comportamento de compra ou desempenho de produtos não estarão disponíveis no painel administrativo neste momento.
- Sistema de cupons personalizados por usuário não será contemplado inicialmente, apenas regras gerais de promoções definidas pelo administrador.
- Aplicativo nativo (Android/iOS) não será desenvolvido nesta fase, apenas a versão responsiva da plataforma web.

## 2.3 Ambiente de Desenvolvimento
### Ferramentas e Tecnologias
| Tipo                                        | Modelo e Especificações     |
| ------------------------------------------- | --------------------------- |
| Repositório Online                          | GitHub                      |
| Plataforma de Modelagem UML                        |Draw.io                      |
| Plataforma de Modelagem DER | BR Modelo Web    |
| Plataforma para criar bancos de dados relacionais.        | MySQL |
| Executar o back-end e banco de dados localmente        | XAMPP  |
| Implementar a lógica do sistema e conexão com o banco. | Python (Flask/Django) |
| Escrever e organizar o código-fonte.                  |   VS Code                         |  

# 3 METODOLOGIA DE PROJETO
## 3.1 Estrutura do Projeto
- PO – Product Owner.
- Scrum Master.
- Squad: Analista de requisitos, Arquiteto de Dados, Designer de Banco de Dados e Administrador de Banco de Dados.

## 3.2 Equipe de Projeto: Papéis e Responsabilidades dos integrantes
| Integrante       | Cargo                 | Responsabilidade   |
| ----------------------- | ------------------------------ | ------------------------------ |
| João Vitor  |  Scrum Master |Organização geral do trabalho, revisão técnica e formatação.       |
| João Vitor e Lais  | Analista de Requisitos    | Elaboração do Plano de Trabalho e Diagrama de Caso de Uso.       |
| João Asafe  | Arquiteto de Dados | Criação do Modelo Conceitual e definição de entidades e relacionamentos.       |
| Manoele, Brayner e Amanda       | Designer de Banco de Dados   | Construção do Modelo Lógico e normalização das tabelas.       |
| João Vitor    | Administrador de Banco de Dados   | Desenvolvimento do Modelo Físico e definição dos scripts SQL.       |
| João Vitor, Lais e João Asafe | Desenvolvedor Back-End            | Criar APIs, integrar com o banco de dados, aplicar regras de negócio. |
| Manoele e Brayner             |  Desenvolvedor Front-End          | Conectar a interface do usuário com as APIs.  |
|  Lais                         |   Tester                          |     Testar se o sistema realmente grava, lê, atualiza e exclui dados do banco corretamente.|

## 3.3 Fases, Atividades e Cronograma
- **Fase I: Especificação e Planejamento – Maio/Junho:**
  - Levantamento de requisitos funcionais e não funcionais, definição das regras de negócio, planejamento geral do projeto e a criação de diagramas:  Caso de Uso, modelos conceitual (Entidade Relacionamento), lógico (Relacional) e Físico (Script para o SGBD).

- **Fase II: Implementação Banco de Dados – Junho/Julho:**
  - Sistema implementado com conexão com o banco de dados.

## 3.4 Entregas de cada Fase
| Fase                           | Mês               | Entregável                                                                            |
| ------------------------------ | ----------------- | ------------------------------------------------------------------------------------- |
| I. Especificação e Planejamento | 26/05| Documento contendo os requisitos, regras de negócios e Diagramas, lógico (Relacional) e Físico (Script para o SGBD).|
| II. Implementação Banco de Dados | 02/07      | Sistema implementado com conexão com o banco de dados funcional. |

## 3.5 Controle de Mudanças
O monitoramento e controle do escopo do projeto serão realizados a partir das seguintes diretrizes:

- Requisitos do projeto devem ser compreendidos por todos os membros da equipe.
- Todas as questões técnicas, de entregas e do cronograma que a equipe do projeto possui devem ser respondidas.
- Todas as entregas devem ser acordadas pela equipe do projeto e entidades parceiras.
- Todas as informações devem estar atualizadas no escopo e não-escopo.
- Nenhum trabalho fora do escopo do projeto deve ser feito.
- Solicitações de mudança no escopo do projeto devem ser efetivamente comunicadas e compreendidas.

# 4 Requisitos
## 4.1 Requisitos Funcionais
| ID     | RF  | Detalhamento | Prioridade|
| -------| --- | ------------ | --------- |
| RF-001  | Cadastro, login e recuperação de senha para usuários.  |  Permitir criação de contas, autenticação de usuários e recuperação de senhas via e-mail. Requisito essencial para o uso das funcionalidades do sistema.    | Alta  |
| RF-002  | Busca, filtragem e exibição de produtos.               | Interface que permite aos usuários localizar produtos por nome, categoria e tamanho, com resultados exibidos de forma clara e responsiva.                  | Alta  |
| RF-003  | Carrinho de compras e controle de estoque.             | Adicionar/remover produtos do carrinho. O estoque de cada produto será automaticamente atualizado após a finalização da compra.                          | Alta  |
| RF-004  | Processamento de pagamento integrado a gateways.       | Integração com gateways de pagamento (ex: PagSeguro, Stripe) para realizar compras de forma segura, com retorno de sucesso ou falha da transação.             | Alta  |
| RF-005  | Acompanhamento de pedidos pelo usuário.                | Os usuários podem visualizar o status de seus pedidos (ex: em processamento, enviado, entregue) diretamente pela conta.                                 | Média |
| RF-006  | Área administrativa para gerenciar produtos, estoques, vendas e promoções. | Módulo interno com acesso restrito para administradores que permite cadastrar produtos, monitorar vendas, configurar promoções e ajustar o estoque.       | Alta |


## 4.2 Requisitos Não Funcionais
| ID     | RNF  | Detalhamento | Prioridade|
| -------| --- | ------------ | --------- |
| RNF-001  |Interface responsiva (web).  |A aplicação deve se adaptar a diferentes resoluções e tamanhos de tela, funcionando corretamente em celulares, tablets e computadores.  | Alta  |
| RNF-002  | Segurança dos dados dos usuários.| Senhas armazenadas com criptografia segura (ex: bcrypt) e comunicação entre cliente e servidor via HTTPS. | Alta|
| RNF-003  | Disponibilidade mínima de 99,5%.| O sistema deve estar acessível e operacional pelo menos 99,5% do tempo, com planos de contingência para quedas. |Média  |
| RNF-004  | Suporte a múltiplos navegadores modernos. | A plataforma deve funcionar corretamente nos principais navegadores atuais, como Chrome, Firefox, Safari e Edge. | Média  |


## 4.3 Regras de Negócios
| ID     | RDN  | Detalhamento | Prioridade|
| -------| --- | ------------ | --------- |
| RDN-001  | Só podem comprar usuários cadastrados e logados | O botão de finalização de compra só é habilitado para usuários autenticados. Impede transações anônimas. | Alta  |
| RDN-002  | Cada produto deve ter estoque atualizado automaticamente após a venda.| Após a confirmação da compra, o sistema reduz automaticamente a quantidade disponível do produto correspondente. | Alta|
| RDN-003  | Promoções e descontos são aplicados conforme regras do administrador. | O administrador define promoções válidas, que são aplicadas automaticamente no carrinho, conforme critérios pré definidos (ex: percentual, combos). |Média  |
| RDN-004  | Devoluções só são permitidas dentro do prazo de 7 dias. | O sistema permite solicitação de devolução somente se o pedido estiver dentro do prazo de 7 dias corridos após o recebimento do produto. | Média  |
