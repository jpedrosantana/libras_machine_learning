# libras_machine_learning
**Proposta de trabalho da disciplina de Técnicas de Visão e Fala do curso de Pós Graduação em Internet das Coisas da Faculdade SENAI Mariano Ferraz.**

A ideia era criar uma aplicação simples que envolvesse o processamento de imagens, e a escolha do tema foi desenvolver um algoritmo que consiga identificar algumas letras da Linguagem Brasileira de Sinais (LIBRAS).

## Os passos da aplicação foram:

 - Criação de um dataset próprio com 10 imagens para as letras A, B e C;
 - Unificação de todas as imagens e a criação de um modelo de machine learning;
 - Criação de um código para o reconhecimento em tempo real.

As imagens foram tiradas sob mesma luminosidade e plano de fundo para evitar possíveis ruídos, e a câmera utilizada foi uma convencional do próprio notebook.

## Dificuldades encontradas:
A abordagem adotada foi a binarização das imagens para fazer o reconhecimento, tendo 100% de precisão para as letas A, B e C, porém em gestos muito similares como os que simbolizam as letras A, E e S o algoritmo não teria o mesmo aproveitamento, porém para o propósito do trabalho o resultado foi satisfatório.

## Tentativa de melhorias na aplicação:
Ampliação do dataset e aplicar filtros para tentar pegar apenas o contorno das imagens (por exemplo blur e sobel).
