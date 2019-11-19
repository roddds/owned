import React from 'react';
import icons from './inventoryIcons';

interface ItemProps {
  path: string;
  title: string;
}

const ItemIcon: React.FC<ItemProps> = ({ path, title }) => {
  const Icon = icons[path];

  if (!Icon) {
    throw new Error(`Invalid icon ${path}`);
  }

  return <Icon style={{ width: '75px', height: '75px' }} />;
};

export default ItemIcon;
