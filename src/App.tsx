import React from 'react';
import {
  Container,
  Columns,
  Column,
  Button,
  Title,
  Content,
  Box
} from 'bloomer';
import { useMachine } from '@xstate/react';
import GameState from './GameState';
import IconCredits from './IconCredits';
import Book from './Book';
import ItemIcon from './ItemIcon';
import './App.css';

function hasRequiredState(optionId: number, context: any) {
  const option = Book.option[optionId];
  const { events, inventory } = context;
  const {
    requiredItems = [],
    requiredEvents = [],
    excludingItems = [],
    excludingEvents = []
  } = option;

  if (!(requiredEvents || requiredItems)) {
    return true;
  }

  const hasEvents = requiredEvents.every(i => events.includes(i));
  const hasItems = requiredItems.every(i => inventory.includes(i));
  const avoidedEvents = excludingEvents.every(i => !events.includes(i));
  const avoidedItems = excludingItems.every(i => !inventory.includes(i));

  return hasEvents && hasItems && avoidedEvents && avoidedItems;
}

interface TextProps {
  chapter: {
    title: string;
    text: string;
    options: number[];
  };
  context: Object;
  onChoose: Function;
}

const Text: React.FC<TextProps> = ({ chapter, context, onChoose }) => {
  return (
    <>
      <Title hasTextAlign='centered' isSize={2}>
        {chapter.title}
      </Title>
      <Content>
        <div
          className='body-text'
          dangerouslySetInnerHTML={{ __html: chapter.text }}
        />
        {chapter.options.map(opt => (
          <Container key={opt}>
            <Button
              isColor='light'
              key={opt}
              disabled={!hasRequiredState(opt, context)}
              onClick={() =>
                onChoose({
                  type: 'SELECT_OPTION',
                  target: Book.option[opt].target,
                  option: opt,
                  chapter: chapter
                })
              }
            >
              {Book.option[opt].text}
            </Button>
          </Container>
        ))}
      </Content>
    </>
  );
};

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
            {!current.context.inventory.length && <p>Nothing here</p>}
            {current.context.inventory.map(item => (
              <ItemIcon
                title={Book.item[item].name}
                path={Book.item[item].path}
              />
            ))}
            <IconCredits />
          </Box>
          <Box>
            <pre>{JSON.stringify(current.context, null, 4)}</pre>
          </Box>
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
