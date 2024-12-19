Códigos de serão utilizados como exemplo pertence ao: https://refactoring.guru/pt-br/design-patterns


<h1>Padrão de Projeto Criaconal: Singleton<h1/> 
  
O Singleton busca garantir que exista uma única instância de uma classe, forcendo um ponto de acesso global a essa instância. Sendo muito utilizado em situações onde a quantidade de instâncias pode
vir a causar problemas. 

<h2>Problemas Resolvido pelo Singleton:<h2/> 
  1. Controle de instância: Garante que uma classe tenha apenas uma única instância durante a execução de um programa, dessa forma simplificando as insconsistências que poderiam surgir decorrente de várias instâncias.

  2. Ponto de Acesso Global: Fornece um único ponto de acesso para uma determinada instância de uma classe, dessa forma permintindo um compartilhamento mais fácil em diferentes partes do código.

<h2>Solução para os problemas:<h2/> 
  1. Fazer com que o construtor da classe seja privado, assim previnindo que outros objetos possam criar uma instância nova dessa classe.
  2. Fazer um método estático que tenha a função de um construtor, dessa forma, esse método chama o construtor privador quando não existir instância "viva", e apenas retorna a instância atual quando solicitada.
