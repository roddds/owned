import { Machine, assign } from 'xstate';

/*
  events:
    readChapter
*/

interface StateType {
  chapter: number;
  history: number[];
  inventory: number[];
  events: number[];
}

const GameState = Machine<StateType>(
  {
    id: 'game-state',
    initial: 'reading',
    context: {
      chapter: 1,
      history: [],
      inventory: [],
      events: []
    },
    states: {
      reading: {
        on: {
          '': [
            {
              target: 'gameOver',
              cond: 'didReachEnding'
            }
          ],
          SELECT_OPTION: {
            target: 'reading',
            actions: [
              'selectOption',
              'setHistory',
              'updateInventory',
              'updateEvents'
            ],
            cond: 'validState'
          }
        }
      },

      gameOver: {
        on: {},
        type: 'final'
      }
    }
  },
  {
    actions: {
      selectOption: assign({ chapter: (context, { target }) => target }),

      setHistory: assign((context, event) => {
        return {
          ...context,
          history: [...context.history, event.target]
        };
      }),

      updateInventory: assign((context, event) => {
        console.log(event.chapter);
        if (!event.chapter.addsItems) {
          return context;
        }
        return {
          ...context,
          inventory: [...context.inventory, ...event.chapter.addsItems]
        };
      }),

      updateEvents: assign((context, event) => {
        console.log(event.chapter);
        if (!event.chapter.addsEvents) {
          return context;
        }
        return {
          ...context,
          events: [...context.events, ...event.chapter.addsEvents]
        };
      })
    },
    guards: {
      didReachEnding: (context, event) => {
        return event.isEnding;
      },
      validState: (context, { chapter }) => {
        const {
          requiredItems = [],
          requiredEvents = [],
          excludingItems = [],
          excludingEvents = []
        } = chapter;

        const hasRequiredItems = requiredItems.every((i: number) =>
          context.events.includes(i)
        );
        const hasRequiredEvents = requiredEvents.every((i: number) =>
          context.inventory.includes(i)
        );
        const avoidedItems = excludingItems.every(
          (i: number) => !context.events.includes(i)
        );
        const avoidedEvents = excludingEvents.every(
          (i: number) => !context.inventory.includes(i)
        );

        return (
          hasRequiredItems && hasRequiredEvents && avoidedItems && avoidedEvents
        );
      }
    }
  }
);

export default GameState;