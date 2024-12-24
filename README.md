Códigos de serão utilizados como exemplo pertence ao: https://refactoring.guru/pt-br/design-patterns
O ChatGPT também foi utilizado para algumas documentações.

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

<h2>Considerações:</h2>
<p>
  Em anexo estará também um código em python de exemplo desse padrão de projeto e também um diagrama UML que melhora o entendimento sobre qual o seu funcionamento.
  Temos que na prática, o singleton será um "Controller" das instâncias que serão geradas de uma determinada classe, fazendo com que apenas 1 exista ao mesmo tempo.
</p>

<h1><strong>Padrão de Projeto Estrutural: Flyweight</strong></h1>

<p>
O <strong>Flyweight</strong> é um padrão de projeto estrutural que permite que programas usem eficientemente grandes quantidades de objetos semelhantes.
    Ele economiza memória compartilhando partes do estado entre objetos em vez de armazená-las separadamente em cada instância
</p>

<h2>Problemas Resolvidos pelo Flyweight:</h2>
<ol>
    <li><strong>Redução de Consumo de Memória:</strong> Em aplicações que precisam lidar com muitos objetos semelhantes, criar uma instância separada para cada um pode ser ineficiente. O Flyweight compartilha os dados comuns entre os objetos para reduzir o consumo de recursos.</li>
    <li><strong>Melhoria no Desempenho:</strong> Ao reutilizar objetos e evitar a criação excessiva de instâncias, o Flyweight reduz o overhead de processamento associado à gestão de memória.</li>
</ol>

<h2>Solução para os Problemas:</h2>
<p>
  O padrão Flyweight sugere que você pare de armazenar o estado extrínseco dentro do objeto. Ao invés disso, você deve passar esse estado para métodos específicos que dependem dele. Somente o estado intrínseco fica dentro do objeto, permitindo que você o reutilize em 
  diferentes contextos. Como resultado, você vai precisar de menos desses objetos uma vez que eles diferem apenas em seu estado intrínseco, que tem menos variações que o extrínseco.
</p>
<ol>
    <li>
        Separar o estado do objeto em dois tipos:
        <ul>
            <li><strong>Estado Intrínseco:</strong> Dados que podem ser compartilhados entre múltiplos objetos, como formas geométricas, configurações de fonte ou modelos de objetos.</li>
            <li><strong>Estado Extrínseco:</strong> Dados específicos de cada instância que não podem ser compartilhados, como posição, cor ou contexto em que o objeto é usado.</li>
        </ul>
    </li>
    <li>
        Criar uma <strong>fábrica de Flyweights</strong>  que gerencie a criação e o compartilhamento de objetos com estados intrínsecos, garantindo a reutilização de instâncias existentes. O método aceita o estado intrínseco do flyweight desejado por um cliente, procura por um objeto flyweight existente que coincide com esse estado, e retorna ele se for encontrado. Se não for, ele cria um novo flyweight e o adiciona ao conjunto.
    </li>
</ol>

<h2>Considerações:</h2>
<p>
O padrão Flyweight é somente uma optimização. Antes de aplicá-lo, certifique-se que seu programa tem mesmo um problema de consumo de RAM relacionado a existência de múltiplos objetos similares na memória ao mesmo tempo. Certifique-se que o problema não possa ser resolvido por outra forma relevante. Anexado está um diagrama UML e um código em python exemplificando o funcionamento deste padrão de projeto.
</p>

<h1><strong>Padrão de Projeto Comportamental: Mediator</strong></h1>

<p>
  O Mediator é um padrão de projeto comportamental que permite que você reduza as dependências caóticas entre objetos. O padrão restringe comunicações diretas entre objetos e os força a colaborar apenas através do objeto mediador.
</p>

<h2>Problemas Resolvidos pelo Mediator:</h2>
<ol>
    <li><strong>Redução de Acoplamento:</strong>Em sistemas com muitos objetos interdependentes, as relações diretas tornam o código complexo e difícil de manter. O Mediator centraliza a lógica de interação, eliminando essas dependências diretas</li>
    <li><strong>Melhoria na Reutilização de Componentes:</strong> Os componentes ficam independentes entre si, podendo ser reutilizados em diferentes contextos sem alterações significativas.</li>
    <li><strong>Simplificação da Lógica de Coordenação:</strong>Em vez de os objetos coordenarem suas interações diretamente, o mediador gerencia toda a lógica de comunicação.</li>
</ol>

<h2>Solução para os Problemas:</h2>
<ol>
    <li><strong>Uso de um Mediador Central:</strong>Um objeto mediador é criado para gerenciar as interações entre vários componentes. Os componentes notificam o mediador sobre eventos e aguardam respostas ou comandos.</li>
    <li><strong>Interface de Notificação::</strong> Todos os componentes se comunicam com o mediador através de uma interface comum. Isso garante flexibilidade, permitindo que novos mediadores possam ser usados sem alterar os componentes existentes.</li>
</ol>

<h2>Considerações:</h2>
<p>
Em anexo está um código implementando esse padrão de projeto, juntamente com um diagrama UML que o exemplifica. Vale ressaltar também que antes de adotar o padrão Mediator, avalie a necessidade real de desacoplamento e centralização de interações no seu sistema. Aplicá-lo desnecessariamente pode introduzir complexidade adicional ao código.
</p>


