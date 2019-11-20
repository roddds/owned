import React from 'react';

const Flaticon = () => (
  <a target='blank' rel='noopener noreferrer' href='https://www.flaticon.com/'>
    Flaticon
  </a>
);

const Icons8 = () => (
  <a target='blank' rel='noopener noreferrer' href='https://icons8.com/icons'>
    Icons8
  </a>
);

const IconCredits = () => (
  <small
    style={{ display: 'block', opacity: '40%' }}
    className='is-unselectable'
  >
    Icons by <Flaticon /> and <Icons8 />
  </small>
);

export default IconCredits;
