import React from 'react';
import { Container, Button, Title, Content } from 'bloomer';
import Book from './Book';

interface TextProps {
  chapter: {
    title: string;
    text: string;
    options: number[];
  };
  context: Object;
  onChoose: Function;
}

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

export default Text;
