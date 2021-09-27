# SOLID

Implementação simples dos princípios SOLID

## Explanação

Criado por volta dos anos 2000 é um acrônimo para 5 princípios que tendem a melhorar o design e arquitetura do código.
Aplicando tais princípios, provavelmente haverá uma redução de complexidade do código, redução dos riscos de quebrar,
melhoria na comunicação entre diferentes entidades e o código torna-se mais flexível, legível e gerenciável.

Os princípios são os seguintes:

- S - Single Responsability

  Uma classe deve ter apenas uma responsabilidade primária, não devendo assumir outras responsabilidades.

  Exemplo: Uma classe de definição não deve ser responsável, também, pela persistência dos dados.

- O - Open-Closed Principle

  Entidades de software devem ser abertas para extensão, mas fechadas para modificação.

  Exemplo: Uma classe responsável pela autenticação possui no momento implementado a autenticação por e-mail e Facebook.
  Caso precise adicionar outra forma, Linkedin ou GitHub por exemplo, a classe precisa ser modificada toda vez?

  A abordagem desse princípio para esse caso seria transformar a classe de Autenticação em abstrata e extender dela para
  implementar os tipos de autenticação.

- L - Liskov Substitution Principle

  Uma classe derivada deve ser substituível por sua classe base. No caso, a classe derivada não deve alterar o
  comportamento

- I - Interface Segregation Principle

  Interfaces específicas são melhores que um interface geral, mas não abuse! Uma analogia seria associando
  comportamentos a canais de uma assinatura de TV. O cliente não quer e nem deveria pagar o preço por canais que não
  serão acessados em sua assinatura.

  Voltando para as classes, os comportamentos são separados em interfaces específicas e somente as necessárias serão
  implementadas pela classe base.

- D - Dependency Inversion Principle Uma classe de alto nível não deve depender de uma de baixo nível. Ambas devem
  depender de abstrações. Resumindo, uma classe não deve conhecer a outra, ambas dependem diretamente da abstração e não
  de sua implementação.

Link
Apresentação [SOLID Pedro](https://docs.google.com/presentation/d/1W2-UBhUcpwQ0OfmEHAvdw_uvSViFArYu36z4lHvxFM8/edit#slide=id.gef9e4d1b6b_0_69)
