import React from 'react';
import { Container, Columns, Column, Button, Title, Box } from 'bloomer';
import { useMachine } from '@xstate/react';
import Sidebar from './Sidebar';
import GameState from './GameState';
import IconCredits from './IconCredits';
import Book from './Book';
import ItemIcon from './ItemIcon';
import Text from './Text';
import Option from './Option';
import './App.css';

const Game: React.FC = () => {
  const [current, send] = useMachine(
    GameState,
    JSON.parse(localStorage.getItem('game-state') || '{}')
  );

  const {
    context,
    context: { inventory }
  } = current;

  (window as any).Book = Book;
  (window as any).Game = current;

  const chapter = Book.chapter[context.chapter];

  React.useEffect(() => {
    localStorage.setItem('game-state', JSON.stringify(current));
  }, [current]);

  return (
    <>
      <Column className='text-column' isSize={{ desktop: 5, mobile: 12 }}>
        <Text chapter={chapter}>
          {chapter.options.map(opt => (
            <Option
              optionId={opt}
              option={Book.option[opt]}
              onChoose={(e: any) => send(e)}
              chapter={chapter}
              context={context}
            />
          ))}
        </Text>
      </Column>
      <Column isSize={3}>
        <Box>
          <Title isSize={4}>Inventory</Title>
          {inventory.map(item => (
            <ItemIcon
              title={Book.item[item].name}
              path={Book.item[item].path}
            />
          ))}
          <ul>
            {context.events.map(c => (
              <li>{Book.event[c].name}</li>
            ))}
          </ul>
          {inventory.length ? <IconCredits /> : <p>Nothing here</p>}
        </Box>
        <Button
          isFullWidth
          isColor='warning'
          onClick={() => {
            localStorage.setItem('game-state', '{}');
            window.location.reload();
          }}
        >
          New Game
        </Button>
      </Column>
    </>
  );
};

export default Game;
