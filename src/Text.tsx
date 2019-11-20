import React from 'react';
import { Title, Content } from 'bloomer';
import Book from './Book';
import Option from './Option';
import { Chapter } from './Types';

interface TextProps {
  chapter: Chapter;
  context: any;
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
          <Option
            optionId={opt}
            option={Book.option[opt]}
            onChoose={onChoose}
            context={context}
            chapter={chapter}
          />
        ))}
      </Content>
    </>
  );
};

export default Text;
