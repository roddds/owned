import React from 'react';
import { Box } from 'bloomer';
import { ContextType } from './GameState';

const PrettyState = ({ context }: { context: ContextType }) => {
  return (
    <Box>
      <pre style={{ maxHeight: '400px' }}>
        {JSON.stringify(context, null, 2)}
      </pre>
    </Box>
  );
};

export default PrettyState;
