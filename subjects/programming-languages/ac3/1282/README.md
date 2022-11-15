<img alt=">" src="../../../../assets/images/difficulty-level/01.webp" width=50 />
<style>
    img[alt$=">"] {
    float: right;
}
</style>

## ImpacTube - 1282
A ImpacTube, uma famosa empresa de compartilhamento de vídeos, quer premiar alguns de seus mais notáveis criadores de conteúdo. Para isso, a ImpacTube montará uma tabela com alguns dos canais que possuem grande quantidade de usuários inscritos.

No site da ImpacTube, os canais geram renda para seus criadores de conteúdo por meio de diversos mecanismos, a conhecida "monetização", o que geralmente é influenciado pela quantidade de inscritos no canal e que acessam aos vídeos postados.

Para possibilitar a premiação, cada registro da tabela (vide exemplo na Figura 1) terá quatro campos dispostos em colunas na seguinte ordem:

1. O nome do canal;
2. A quantidade atual de inscritos;
3. A monetização do último mês do canal e;
4. Um valor indicando se o canal produz conteúdo premium, que são vídeos exclusivos para usuários que pagam uma mensalidade à ImpacTube.

Com esses dados será possível definir a bonificação de cada canal, que será composta pelo valor "monetização" da tabela acrescido de um valor fixo para cada mil inscritos.  O valor fixo será definido pela ImpacTube, sendo X para canais com conteúdo premium e Y para os que não possuem conteúdo premium.

![Image of the problem](https://i.imgur.com/hRjvUJs.png "Image problem")

Você foi escolhido para desenvolver um programa que receberá como entrada os dados de cada canal, gerando internamente a tabela modelo, e que mostrará os nomes dos canais, na ordem em que foram dados na entrada, acompanhados do valor que receberão como bonificação. Observe cuidadosamente o formato de entrada e o formato de saída especificados.

### Entrada
- Na primeira linha será informado um número inteiro que representa a quantidade N (1 <= N <= 200) de canais da tabela;

- Em cada uma das N linhas seguintes serão informados os registros que compõem a tabela, com os valores das colunas separados por um ponto e vírgula, nesta ordem: (1) uma string com o nome do canal que será bonificado; (2) um número natural que é a quantidade de inscritos no canal; (3) um número real simbolizando a monetização do canal no mês anterior (dado em reais R$) e; (4) uma string 'sim' ou 'não', sem apóstrofos e completamente em minúsculo, que indica se o canal produz conteúdo premium;

- Por fim, serão informados dois números reais X e Y, um em cada linha, que indicam o valor fixo (em reais R$) que os canais receberão a mais para cada mil inscritos no canal. O primeiro valor é X e refere-se aos canais que possuem conteúdo premium. O segundo valor é Y e refere-se aos canais que não possuem conteúdo premium.

### Saída
O cabeçalho contém três linhas,  sendo a primeira e a terceira compostas por apenas cinco hifens, e a segunda composta unicamente pela palavra 'BÔNUS', sem apóstrofos e completamente em maiúsculo. Nas próximas N linhas, estão os nomes dos canais, na mesma ordem em que foram dados na entrada, acompanhados à direita pelo valor que receberão como bonificação, em reais e com duas casas decimais, exatamente como consta nos exemplos.

| Input | Output |
| :----- | :----- |
| 8 <br> Clow Podcast;2700000;500.99;não <br> Felipe Nelson;3500000;1000.25;sim <br> Porta dos Mundos;16800000;2000.00;sim <br> PodHá!;2120000;450.00;não <br> Winter SonNones;42400000;20000.00;sim <br> Manual do Urso;14600000;1800.50;sim <br> Humorado Games;4130000;5000.00;não <br> Joãozinho TôComeçando;950;10.00;não <br> 1.00 <br> 0.50 | ----- <br> BÔNUS <br> ----- <br> Clow Podcast: R$ 1850.99 <br> Felipe Nelson: R$ 4500.25 <br> Porta dos Mundos: R$ 18800.00 <br> PodHá!: R$ 1510.00 <br> Winter SonNones: R$ 62400.00 <br> Manual do Urso: R$ 16400.50 <br> Humorado Games: R$ 7065.00 <br> Joãozinho TôComeçando: R$ 10.00 |
|  6 <br> Canal A;2000;100.00;sim <br> Canal B;1000;100.00;sim <br> Canal C;1999;100.00;sim <br> Canal D;999;100.00;sim <br> Canal E;1;100.00;sim <br> Canal F;15000;0.00;não <br> 0.01 <br> 1.00 | ----- <br> BÔNUS <br> ----- <br> Canal A: R$ 100.02 <br> Canal B:  R$ 100.01 <br> Canal C: R$ 100.01 <br> Canal D: R$ 100.00 <br> Canal E: R$ 100.00 <br> Canal F: R$ 15.00
