import React from 'react';
import { Container, Columns, Column, Button, Title, Box } from 'bloomer';
import { useMachine } from '@xstate/react';
import GameState from './GameState';
import IconCredits from './IconCredits';
import Book from './Book';
import ItemIcon from './ItemIcon';
import PrettyState from './PrettyState';
import Text from './Text';
import './App.css';

const App: React.FC = () => {
  const [current, send] = useMachine(
    GameState,
    JSON.parse(localStorage.getItem('game-state') || '{}')
  );

  (window as any).Book = Book;
  (window as any).Game = current;

  const chapter = Book.chapter[current.context.chapter];

  React.useEffect(() => {
    localStorage.setItem('game-state', JSON.stringify(current));
  }, [current]);

  return (
    <Container>
      <Columns isCentered>
        <Column isSize='2/3'>
          <Text
            chapter={chapter}
            context={current.context}
            onChoose={(e: any) => send(e)}
          />
        </Column>
        <Column isSize='1/3'>
          <Box>
            <Title isSize={4}>Inventory</Title>
            {current.context.inventory.map(item => (
              <ItemIcon
                title={Book.item[item].name}
                path={Book.item[item].path}
              />
            ))}
            {current.context.inventory.length ? (
              <IconCredits />
            ) : (
              <p>Nothing here</p>
            )}
          </Box>
          <PrettyState context={current.context} />
          <Button
            isColor='warning'
            onClick={() => {
              localStorage.setItem('game-state', '{}');
              window.location.reload();
            }}
          >
            reset
          </Button>
        </Column>
      </Columns>
    </Container>
  );
};

export default App;
