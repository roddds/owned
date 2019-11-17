import { Machine, assign } from 'xstate';

/*
  events:
    readChapter
*/

interface StateType {
  chapter: number;
  history: number[];
  choices: number[];
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
      choices: [],
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
              'saveChoices',
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

      saveChoices: assign((context, event) => {
        return {
          ...context,
          choices: [...context.choices, event.option]
        };
      }),

      updateInventory: assign((context, { chapter }) => {
        const { addsItems = [], removesItems = [] } = chapter;

        if (!addsItems && !removesItems) {
          return context;
        }

        const inventory = [...context.inventory, ...addsItems].filter(
          (i: number) => !removesItems.includes(i)
        );

        return {
          ...context,
          inventory: Array.from(new Set(inventory))
        };
      }),

      updateEvents: assign((context, event) => {
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
