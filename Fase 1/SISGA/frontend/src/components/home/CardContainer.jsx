import React, { useEffect } from 'react';

import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/Container';

import CardNumeroTotal from './CardNumeroTotal';

const CardContainer = ( {valores} ) => {

  return (
    <Container className='my-5'>
      <Row xs={1} md={2} xl={4} className="g-4">
      {
        valores.map((valor, idx) => (
          <Col key={idx}>
            <CardNumeroTotal valor={valor}/>
          </Col>
        ))
      }
      </Row>
    </Container>
  );
}

export default CardContainer;
