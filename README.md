# Design-Patterns
Python Design Patterns

# RESUMO DO PADRAO SINGLETON
• Há muitas aplicações do mundo real em que precisamos criar apenas um objeto. Se criarmos
várias instâncias para cada aplicação, teremos um uso excessivo de recursos. O padrão
Singleton funcionam muito bem nestas situações;
• O Singleton é um método comprovado, resistente ao teste do tempo, e oferece um ponto de
aesso global sem muitas desvantagens;
• É claro que há algumas desvantagens já que o singleton pode exercer um impacto inesperado
por trabalhar com variáveis globais ou por instanciarem classes que exigem muitos recursos,
mas que acabam por não utilizá-los.



## Singleton
Lembre-se que o Singleton tem um ponto de acesso global, e desta formas os seguintes
problemas podem ocorrer:

• Variáveis globais podem ser alteradas por engano em algum lugar e, como o desenvolvedor
pode achar que elas permanecem inalteradas, as variáveis poderão acabar sendo usadas em
outro lugar na aplicação;

• Variáveis referência podem ser criadas para o mesmo objeto. Como o Singleton cria apenas um
objeto, várias referências podem ser criadas neste ponto para o mesmo objeto;
• Todas as classes que são dependentes de variáveis globais acabam se tornando altamente
acopladas, pois uma mudança feita por uma classe no dado global poderá exercer um impacto
em outra classe
