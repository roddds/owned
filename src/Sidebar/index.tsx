import React from 'react';

import { Column, Hero } from 'bloomer';
import SidebarImage from './sidebar.png';

const Sidebar = ({ side }: { side: 'left' | 'right' }) => (
  <Column isSize={2} isPaddingless isHidden='mobile'>
    <Hero
      isFullHeight
      style={{
        backgroundImage: `
          linear-gradient(
            to ${side === 'left' ? 'right' : 'left'},
            rgba(255,255,255,0.90) 0%,
            rgba(255,255,255,0.95) 80%,
            rgba(255,255,255,1) 100%),
            url(${SidebarImage})`,
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        position: 'sticky',
        top: 0
      }}
    />
  </Column>
);

export default Sidebar;
