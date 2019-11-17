import React from 'react';
import 'bulma/css/bulma.css';
import { Container, Columns, Column, Button } from 'bloomer';
import { useMachine } from '@xstate/react';
import GameState from './GameState';
import Book from './Book';
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

const App: React.FC = () => {
  const [current, send] = useMachine(
    GameState,
    JSON.parse(localStorage.getItem('game-state') || '{}')
  );

  const chapter = Book.chapter[current.context.chapter];

  React.useEffect(() => {
    localStorage.setItem('game-state', JSON.stringify(current));
  }, [current]);

  return (
    <Container>
      <Columns isCentered>
        <Column isSize='2/3'>
          <div
            className='body-text'
            dangerouslySetInnerHTML={{ __html: chapter.text }}
          />

          {chapter.options.map(opt => (
            <Container key={opt}>
              <Button
                isColor='light'
                key={opt}
                disabled={!hasRequiredState(opt, current.context)}
                onClick={() =>
                  send({
                    type: 'SELECT_OPTION',
                    target: Book.option[opt].target,
                    chapter: chapter
                  })
                }
              >
                {Book.option[opt].text}
              </Button>
            </Container>
          ))}
        </Column>
        <Column isSize='1/3'>
          <ul>
            {current.context.inventory.map(item => (
              <li key={item}>{Book.item[item].name}</li>
            ))}
          </ul>
          <pre>{JSON.stringify(current.context, null, 4)}</pre>
          <button onClick={() => localStorage.setItem('game-state', '{}')}>
            clear
          </button>
        </Column>
      </Columns>
    </Container>
  );
};

export default App;
