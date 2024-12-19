Códigos de serão utilizados como exemplo pertence ao: https://refactoring.guru/pt-br/design-patterns


<h1><strong>Padrão de Projeto Criacional: Singleton</strong></h1>

<p>
O <strong>Singleton</strong> é um padrão de projeto criacional que garante a existência de apenas uma única instância de uma classe e força um ponto de acesso global a essa instância. É amplamente utilizado em situações onde múltiplas instâncias poderiam causar problemas, como no gerenciamento de recursos compartilhados.
</p>

<h2>Problemas Resolvidos pelo Singleton:</h2>
<ol>
  <li><strong>Controle de Instância:</strong> Garante que uma classe tenha apenas uma única instância durante a execução de um programa. Isso simplifica a gestão de recursos e evita inconsistências que poderiam surgir devido à existência de várias instâncias.</li>
  <li><strong>Ponto de Acesso Global:</strong> Fornece um único ponto de acesso para uma instância específica de uma classe, permitindo seu compartilhamento de forma eficiente em diferentes partes do código.</li>
</ol>

<h2>Solução para os Problemas:</h2>
<ol>
  <li>
    Tornar o construtor da classe <strong>privado</strong>, impedindo que outras partes do código criem novas instâncias diretamente.
  </li>
  <li>
    Criar um <strong>método estático</strong> que funciona como um construtor controlado. Esse método verifica se já existe uma instância "viva" da classe:
    <ul>
      <li>Se não existir, o método chama o construtor privado para criar uma nova instância e a armazena.</li>
      <li>Se já existir, ele retorna a instância existente.</li>
    </ul>
  </li>
</ol>
