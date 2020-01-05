import React from 'react';
import { Container, Columns, Column, Content, Button, Title } from 'bloomer';
import Sidebar from './Sidebar';
import Game from './Game';
import logo from './logo_flat.png';
import { newGame } from './GameState';

const App = () => {
  const [isPlaying, setIsPlaying] = React.useState(false);

  return (
    <Container isMarginless isFluid isFullWidth isPaddingless>
      <Columns isMarginless>
        <Sidebar side='left' />

        {isPlaying ? (
          <Game quit={() => setIsPlaying(false)} />
        ) : (
          <Columns
            isVCentered
            hasTextAlign='centered'
            style={{ width: '100%' }}
          >
            <Column isSize={10} isOffset={1}>
              <img src={logo} alt='Owned logo' style={{ maxWidth: '50%' }} />
              <Title>Owned - Um Novo Jogador</Title>
              <Content>
                <p>
                  <strong>OWNED - um novo jogador</strong> é um jogo interativo.
                  Você decide o final.
                </p>

                <p>
                  Em <strong>OWNED</strong> você é André, um técnico de
                  informática viciado em videogames que vai tentar conquistar
                  pelo menos uma dentre <strong>sete</strong> garotas. Para
                  jogar, basta clicar em uma das opções no final de cada trecho
                  de história, dando um rumo à vida de André.
                </p>

                <p>
                  Você pode salvar o jogo e pode jogar de novo quantas vezes
                  quiser. É grátis!
                </p>

                <p>
                  <span>Recomendado para maiores de 18 anos.</span>
                </p>
              </Content>
              <Button
                onClick={() => {
                  newGame();
                  setIsPlaying(true);
                }}
              >
                New Game
              </Button>
              <Button onClick={() => setIsPlaying(true)}>Continue</Button>
            </Column>
          </Columns>
        )}

        <Sidebar side='right' />
      </Columns>
    </Container>
  );
};

export default App;
