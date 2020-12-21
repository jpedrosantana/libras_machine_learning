# libras_machine_learning
**Proposta de trabalho da disciplina de Técnicas de Visão e Fala do curso de Pós Graduação em Internet das Coisas da Faculdade SENAI Mariano Ferraz.**

A ideia era criar uma aplicação simples que envolvesse o processamento de imagens, e a escolha do tema foi desenvolver um algoritmo que consiga identificar algumas letras da Linguagem Brasileira de Sinais (LIBRAS), essa aplicação pode ser adaptada a outros tipos de gestos.

## Os passos da aplicação foram:

![enter image description here](https://i.imgur.com/oWm8u3g.jpg)
![enter image description here](https://i.imgur.com/vk9bIvH.jpg)
 - Criação de um dataset próprio com 10 imagens para as letras A, B e C;
 - Unificação de todas as imagens;
 - Aplicação da binarização das imagens;
 - Criação de um modelo de machine learning (KNN);
 - Criação de um código para o reconhecimento em tempo real.

As imagens foram tiradas sob mesma luminosidade e plano de fundo para evitar possíveis ruídos, e a câmera utilizada foi uma convencional do próprio notebook.

## Resultados:
A abordagem adotada foi a binarização das imagens para fazer o reconhecimento, tendo 100% de precisão para as letas A, B e C.

![enter image description here](https://i.imgur.com/D6YCBev.png)![enter image description here](https://i.imgur.com/md6gSeH.png)![enter image description here](https://i.imgur.com/0NpcmxZ.png)
## Dificuldades encontradas:
Devida a abordagem de binarização adotada, em gestos muito similares, como os que simbolizam as letras **A**, **E** e **S** o algoritmo não teria o mesmo aproveitamento, porém para o propósito do trabalho o resultado foi satisfatório.
Outro problema encontrado foi que caso nenhum gesto seja inserido o algoritmo ainda informa um resultado.

## Tentativa de melhorias na aplicação:
Ampliação do dataset e aplicar filtros para tentar pegar apenas o contorno das imagens (por exemplo blur e sobel).
Encontrar uma maneira do algoritmo retornar nada caso nenhum gesto seja informado.
