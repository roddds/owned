import React from 'react';
import { Box } from 'bloomer';
import { StateType } from './GameState';

const PrettyState = ({ context }: { context: StateType }) => {
  return (
    <Box style={{ maxHeight: '400px', overflowY: 'scroll' }}>
      <pre>{JSON.stringify(context, null, 2)}</pre>
    </Box>
  );
};

export default PrettyState;
