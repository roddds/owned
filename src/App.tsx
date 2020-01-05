import React from 'react';
import { Container, Columns, Column, Button, Title, Box } from 'bloomer';
import Sidebar from './Sidebar';
import Game from './Game';

const App = () => {
  return (
    <Container isMarginless isFluid isFullWidth isPaddingless>
      <Columns isCentered isMarginless>
        <Sidebar side='left' />
        <Game />
        <Sidebar side='right' />
      </Columns>
    </Container>
  );
};

export default App;
