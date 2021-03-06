import React from 'react';
import { Column, Button, Title, Box } from 'bloomer';
import { useGameState } from './GameState';
import IconCredits from './IconCredits';
import Book from './Book';
import ItemIcon from './ItemIcon';
import Text from './Text';
import Option from './Option';
import './App.css';

interface Props {
  quit: () => void;
}

const Game: React.FC<Props> = ({ quit }: Props) => {
  const { current, send } = useGameState();

  const {
    context,
    context: { inventory }
  } = current;

  (window as any).Book = Book;
  (window as any).Game = current;

  const chapter = Book.chapter[context.chapter];

  const playOption = (e: any) => {
    window.scrollTo(0, 0);
    send(e);
  };

  return (
    <>
      <Column className='text-column' isSize={{ desktop: 5, mobile: 12 }}>
        <Text chapter={chapter}>
          {chapter.options.map(opt => (
            <Option
              optionId={opt}
              option={Book.option[opt]}
              onChoose={playOption}
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
        <Button isFullWidth isColor='warning' onClick={quit}>
          Save and Quit
        </Button>
      </Column>
    </>
  );
};

export default Game;
