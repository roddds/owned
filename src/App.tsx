import React from 'react';
import 'bulma/css/bulma.css';
import { Container, Columns, Column } from 'bloomer';
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
          <div dangerouslySetInnerHTML={{ __html: chapter.text || '' }} />

          {chapter.options.map(opt => (
            <button
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
            </button>
          ))}
        </Column>
        <Column isSize='1/3'>
          <pre>{JSON.stringify(current.context, null, 1)}</pre>
        </Column>
      </Columns>
    </Container>
  );
};

export default App;
