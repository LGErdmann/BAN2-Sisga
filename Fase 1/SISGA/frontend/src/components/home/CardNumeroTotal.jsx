import React from 'react';

import { Card } from 'react-bootstrap';

const CardNumeroTotal = ({valor}) => {

  return (
    <Card className="text-center">
      {/* <Card.Img variant="top" src="holder.js/100px160" alt='alt="100%x160"'/> */}
      <Card.Header>Total de {valor.titulo}</Card.Header>

      <Card.Body>
        <Card.Title>{valor.total}</Card.Title>
        {/* <Card.Text>
          This is a longer card with supporting text below as a natural
          lead-in to additional content. This content is a little bit
          longer.
        </Card.Text> */}
      </Card.Body>
    </Card>
  );
}

export default CardNumeroTotal;
