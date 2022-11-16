<img align="right" style="aspect-ratio: 1; object-fit: cover" width="50" src="../../../../assets/images/difficulty-level/03.webp"/>

## Carrinho de compras - 1269
Você está criando um site para uma loja virtual e precisa guardar os itens que os usuários adicionam em seu carrinho. Cada item é representado no sistema por um código numérico, isto é, um número inteiro que é capaz de identificá-lo unicamente. Como solução inicial, você decidiu guardar os itens adicionados ao carrinho em uma lista e, para testar o seu programa, implementou alguns comandos básicos para simular uma interação do usuário com o sistema:

- adicionar: inclui o código de um novo produto à lista;
- remover: remove o código de um produto da lista;
- exibir: exibe os itens da lista em ordem crescente;
- encerrar: exibe os itens da lista, de modo idêntico ao comando exibir, e encerra o programa.

A primeira linha poderá conter uma lista de inteiros separados por espaços, representando produtos que já estavam no carrinho, por exemplo, de uma sessão anterior que o usuário iniciou mas não finalizou a compra. Você deve receber essa lista e inicializar o carrinho de compras já com os códigos dessa lista, que devem ser números inteiros.

Caso não haja nenhum produto salvo de uma sessão anterior, essa primeira linha será uma linha em branco, sem nenhum texto ou caractere.

### Entrada
- A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha vazia;
- As próximas linhas serão os comandos citados anteriormente, sendo que linhas com comandos "adicionar" e "remover" também possuem um valor à direita do comando, que representa o código do produto, note que há um espaço entre o comando e o código;
- A entrada sempre é encerrada com o comando "encerrar".

### Saída
A saída deve conter:

- Os códigos dos produtos que estão no carrinho separados por um espaço e de acordo com a execução dos comandos "exibir" e "encerrar". Note que deve haver um espaço apenas entre os itens, portanto não deverá existir espaço após o último item;
- A mensagem "código <código> não encontrado" (sem aspas), quando o comando remover for executado com um código que não esteja no carrinho. Substitua <código> pelo código não encontrado, conforme os casos de teste de exemplo.

Observação: Lembre-se de não exibir texto no input.


| INPUT | OUTPUT    |
| :----- | :--------- |
| 3 25 12 <br> exibir <br> adicionar 1 <br> adicionar 312 <br> exibir <br> adicionar 19 <br> encerrar | 3 12 25 <br> 1 3 12 25 312 <br> 1 3 12 19 25 312 |
| <br> adicionar 10 <br> adicionar 11 <br> adicionar 5 <br> encerrar | 5 10 11 |
| 5 27 389 <br> exibir <br> adicionar 1 <br> remover 200 <br> exibir <br> remover 389 <br> encerrar | 5 27 389 <br> código 200 não encontrado <br>  5 27 389 <br> 1 5 27 |
| <br> remover 300 <br> encerrar | código 300 não encontrado |