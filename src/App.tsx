import React from 'react';
import { Container, Columns, Column, Button, Title } from 'bloomer';
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
            <Column>
              <img src={logo} alt='Owned logo' style={{ maxWidth: '50%' }} />
              <Title>Owned - Um Novo Jogador</Title>
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
