# ENTIDADES:

* Cliente;
* User ADM;
* Produto;
* Tipo;
* Histórico de Vendas.

# RELACIONAMENTOS

* Cliente **ESCOLHE** tipo de produto;
* Cliente **COMPRA** produto;
* Cliente **FAZ** pagamento;
* Produto **CONTÉM** tipo de produto;
* User adm **CADASTRA** produto;
* User adm **ACESSA** Histórico de vendas;
* Histórico de Vendas **CONTÉM** produto.
