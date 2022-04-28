Cada usuário pode receber créditos e realizar pagamentos por QRCodes únicos gerados para a transação específica.
**Não implementar validação para chave única

Versão 1.0
--- Implemetanções ---

Cada Usuário deve possuir uma conta

Cada Conta pode realizar pagamentos e receber créditos de outros usuários.

Todas as informações que serão embarcadas nos QRCode serão
apresentadas como Strings. 


Quando um usuário for realizar um pagamento, ele deve
informar o usuário que vai receber esse valor, o valor e a
String do QRCode. 

Quando ele for receber algum valor, ele deve
gerar a chave de autorização da transação.


---  CLASSES ---

Usuário
- nome
- senha
- e-mail

Contas
- idConta (único para cada conta)
- saldo

Transações

*não deve possui atributos

Ela traz a implementação dos métodos para gerar os QRCode em String para cada operação. Segue as seguintes regras:
- Toda transação deve ser composta pelo id da conta;
- A String gerada deve conter o nome do usuário que
vai receber o valor;
- A String gerada deve conter o valor da transação;
