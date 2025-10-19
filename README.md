# gamepgzero
Jogo para fim didático em Pythin

# Desenvolvimento
Para desenvolver este jogo foi utilizado a biblioteca pgzero logo é um pré requisito telá instalado na sua máquina para que o jogo funcione corretamemente.

# Intrusções do desenvolvimento
Foram desenvolvidos 4 atores para os resíduos sendo um para plástico, um para vidro, um para metal e um para papel.
Foi criado a variável atores para receber o um vetor dos quatro atores.
E o ator_ativo que é o ator sorteado.

Para o background inicial foi utilizado uma imagem com os coletores
Para a colisão foi utilizado a posição de cada coletor combinado com o ator selecionado. Ex: o resíduo plástico precisa ser clicado até no máximo na posição x<=120
Foi criada uma função para confirmar se o click foi correto ou errado, no caso de acerto um som de acerto é toca juntamente com a exibição de um ícone de acerto.
Quando o click for errado é tocado um som de erro e um ícone de erro é exibido.


Na função vidas é exibida as mensagens:
Clique no resíduo quando ele passar sobre o coletor correto! - quando o jogo tiver rolando
Pressione R para reiniciar o jogo! - quando o jogo for finalizado

Para reiniciar o jogo foi definido o clique na tecla R.

Quando o jogo é finalizado o background é alterado para uma imagem de gameover.

# Instruções de jogo
Clique sobre o resíduo quando ele estiver passando sobre o coletor correto.
Se você clicar sobre outro coletor uma vida será perdida.
Se o resíduo já tiver passado do coletor correto não clique na tela para não perder ponto.
O jogo inicia com três vidas.
