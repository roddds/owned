import React from 'react';
import { Button } from 'bloomer';
import { ContextType } from './GameState';
import { Option as OptionType } from './Types';

interface OptionProps {
  optionId: number;
  option: OptionType;
  onChoose: Function;
  context: ContextType;
  chapter: any;
}

function hasRequiredState(option: OptionType, context: any) {
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

const Option = (props: OptionProps) => {
  const { option, optionId, onChoose, context, chapter } = props;
  return (
    <Button
      style={{ margin: '1px 0' }}
      key={option.target}
      isFullWidth
      isColor='dark'
      disabled={!hasRequiredState(option, context)}
      onClick={() =>
        onChoose({
          type: 'SELECT_OPTION',
          target: option.target,
          option: optionId,
          chapter: chapter
        })
      }
    >
      {option.text}
    </Button>
  );
};

export default Option;
