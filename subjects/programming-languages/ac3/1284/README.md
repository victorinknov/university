<img align="right" style="aspect-ratio: 1; object-fit: cover" width="50" src="../../../../assets/images/difficulty-level/03.webp"/>

## Segunda Chance - 1284 
Em uma faculdade de um mundo muito distante, dois jovens professores buscam ajudar seus alunos a estudarem e melhorarem seus conhecimentos sobre a disciplina de programação, fazendo com que notas mais altas sejam conquistadas. Para isso, desenvolveram a estratégia da "Segunda Chance".
A "Segunda Chance" consiste em uma nova atividade com os mesmos problemas da atividade original, porém com um prazo estendido e com a disponibilização de vídeos detalhados com a resolução de cada problema, de modo a incentivar que os alunos revisitem e comparem suas próprias propostas de solução.
Para aumentar ainda mais o incentivo para a turma, os professores concedem um bônus de dois pontos sobre a nota original para aqueles que resolverem TODOS os problemas dentro do prazo estendido, isto é, que obtiverem dez na nova atividade, o que é uma "moleza", considerando que basta assistir as resoluções e aplicá-las. Mas é claro, o bônus é concedido até o limite de dez pontos, ou seja, caso a soma do bônus com a nota original resulte em um valor superior a dez, a nota final será dez.
Como esperado, os alunos ficaram contentes e empolgados com a oportunidade. De tão agradecidos, ofereceram um software aos dois professores, de modo a reduzir um pouco da carga extra de trabalho que eles terão para recalcular as notas.
Você se voluntariou para implementar esse software, que precisa receber um valor inicial indicando a quantidade de alunos da turma, seguido pelas notas originais de cada aluno e pelas notas obtidas na nova atividade. O programa deverá exibir a quantidade de alunos que tiveram suas notas alteradas, assim como as notas originais e finais de cada aluno, destacando aqueles que aumentaram as notas.

### Entrada
- Na primeira linha haverá um número natural N (1 <= N <= 999) indicando a quantidade de alunos da turma;
- Nas próximas N linhas, haverá a nota original de cada aluno, que são valores reais no intervalo fechado [ 0,10 ];
- Por fim, nas N linhas seguintes, haverá a nota obtida na nova atividade por cada aluno, também situadas no intervalo fechado [ 0,10 ].

Note que as N primeiras notas correspondem as notas originais dos N primeiros alunos, e as próximas N notas correspondem as notas da "Segunda Chance" dos mesmos alunos. Portanto, se N = 5, a 1ª nota é do primeiro aluno e a 6ª nota também é do primeiro aluno (original e "Segunda Chance), a 2ª nota é do segundo aluno e a 7ª também, a 5ª é do quinto aluno e a 10ª também.

### Saída
- A primeira linha será a frase 'NOTAS ALTERADAS: <quantidade>', sem apóstrofos e completamente em maiúsculo, em que <quantidade> deve ser substituído pela quantidade de alunos que tiveram suas notas originais alteradas em decorrência da aplicação do bônus;
- As próximas N linhas serão as notas de todos os alunos, na mesma ordem dada na entrada, iniciando com asterisco ('*') para indicar as notas que foram alteradas e hífen ('-') para indicar aquelas que não foram, seguido pela posição da referida nota entre parênteses. O formato de cada linha pode ser observada nos exemplos, onde se destacam três características: (I) a posição tem sempre três dígitos, completada com zeros à esquerda quando necessário; (II) todas as notas são exibidas com duas casas decimais e; (III) todas as notas ocupam cinco colunas, incluindo o caractere ponto, e completadas com zeros à esquerda quando necessário.

<img src="../../../../assets/images/pictures/screenshot.png"/>