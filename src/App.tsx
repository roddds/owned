import React from 'react';
import { Container, Columns, Column, Button, Title, Box, Hero } from 'bloomer';
import { useMachine } from '@xstate/react';
import GameState from './GameState';
import IconCredits from './IconCredits';
import Book from './Book';
import ItemIcon from './ItemIcon';
import PrettyState from './PrettyState';
import Text from './Text';
import Option from './Option';
import SidebarImage from './sidebar/sidebar.png';
import './App.css';

const sidebarColumnBackground = (direction: 'left' | 'right') => ({
  backgroundImage: `
    linear-gradient(
      to right,
      rgba(255,255,255,0.90) 0%,
      rgba(255,255,255,0.95) 80%,
      rgba(255,255,255,1) 100%),
      url(${SidebarImage})`,
  backgroundPosition: 'center',
  backgroundSize: 'cover',
  backgroundRepeat: 'no-repeat',
  transform: `scaleX(${direction === 'left' ? '-1' : '1'})`
});

const App: React.FC = () => {
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
    <Container isMarginless isFluid isFullWidth isPaddingless>
      <Columns isCentered isMarginless>
        <Column isSize={2} isPaddingless isHidden='mobile'>
          <Hero isFullHeight style={sidebarColumnBackground('right')} />
        </Column>
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
          <PrettyState context={context} />
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
        <Column isSize={2} isPaddingless isHidden='mobile'>
          <Hero isFullHeight style={sidebarColumnBackground('left')} />
        </Column>
      </Columns>
    </Container>
  );
};

export default App;
