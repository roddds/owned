import React from 'react';
import { Title, Content } from 'bloomer';
import { Chapter } from './Types';

interface TextProps {
  chapter: Chapter;
}

const Text: React.FC<TextProps> = ({ chapter, children }) => {
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
        {children}
      </Content>
    </>
  );
};

export default Text;
