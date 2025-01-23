# GameBomb
Leonardo Gonçalves Martins, slentmartz@gmail.com

Evandro Nicolau, evandronicolau55@gmail.com

Marcelo Ribeiro, marcelormartins0@gmail.com

Kaio Katsuo, kaiokatsuo88@gmail.com

Viktor Augusto, augustoviktor24@gmail.com

Apresentação do Jogo GAMEBOMB

Sobre o Jogo

O jogo ASCII é um projeto desenvolvido em Python, inspirado em jogos clássicos de batalha com mecânicas simples e visuais baseados em caracteres ASCII. O jogo conta com uma combinação de elementos de estratégia, exploração e combate, trazendo desafios dinâmicos para dois jogadores em um ambiente interativo.

Principais Características


Jogabilidade Avançada:

Controle de dois jogadores com diferentes direções de movimentação (cima, baixo, esquerda, direita).

Possibilidade de colocar bombas no cenário e explodi-las após um determinado intervalo de tempo.


Sistema de Bombas:

As bombas podem ser posicionadas na direção em que o jogador está virado.

Temporizadores controlam a duração da bomba antes de explodir e o tempo que a explosão permanece visível.


Efeitos Sonoros:

Uso do módulo pygame para reproduzir efeitos sonoros, incluindo o som da explosão das bombas, aumentando a imersão.


Desenho Dinâmico do Cenário:

Atualização constante do mapa usando a biblioteca WConio2, garantindo fluidez na movimentação e interações dos jogadores.


Regras de Fim de Jogo:

O jogo termina quando um dos jogadores é eliminado.


Estrutura do Jogo


Movimentação dos Jogadores:

Cada jogador controla seu personagem em tempo real, podendo alterar a direção e interagir com o ambiente.


Sistema de Bombas:

Ativação: Quando um jogador ativa uma bomba, ela é posicionada de acordo com a direção do jogador.

Temporizador: A bomba é desenhada no mapa por um período predefinido, seguido pela sua explosão.

Reset: Após a explosão, o estado da bomba é resetado, permitindo novas ativações.


Interação com o Cenário:

O cenário é dinâmico e é atualizado a cada ciclo da execução do jogo.

Mecânica de Temporização das Bombas

O comportamento das bombas é controlado pelas seguintes variáveis:


Objetivo do Projeto

O objetivo deste jogo é explorar conceitos de desenvolvimento de jogos em Python, com foco em:

Manipulação de matrizes para o desenho do mapa.

Controle de tempo usando o módulo time.

Integração de sons para criar uma experiência mais imersiva.

Implementação de mecânicas de interação e colisão em um ambiente dinâmico.


Como Jogar

Clone o repositório para sua máquina local.

Certifique-se de ter Python instalado.

Instale as dependências necessárias (como WConio2, caso aplicável).

Execute o jogo com o comando:

python nome_do_arquivo.py

Divirta-se controlando os jogadores e utilizando bombas para derrotar seu oponente!
