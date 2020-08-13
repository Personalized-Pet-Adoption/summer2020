import React from 'react';
import './pet.styles.css';
import Card from 'react-bootstrap/Card'
import {Button, ListGroup, ListGroupItem} from 'react-bootstrap'
import { withRouter } from 'react-router-dom';

export const Pet = props =>(

<Card style={{ width: '18rem', margin: '2rem', spacing:'0 rem'}}>
  <Card.Img variant="top" src="https://s3-eu-west-1.amazonaws.com/w3.cdn.gpd/gb.pedigree.55/large_53b66497-3a2d-420c-a567-b1e0ae5c5823.jpg" />
  <Card.Body>
<Card.Title>{props.pet.name}</Card.Title>
    <Card.Text>
    Description
    </Card.Text>
  </Card.Body>
  <ListGroup className="list-group-flush">
    <ListGroupItem>{props.pet.species}</ListGroupItem>
    <ListGroupItem>{props.pet.gender}</ListGroupItem>
    <ListGroupItem>{props.pet.post_date}</ListGroupItem>
  </ListGroup>
  <Card.Body>
    <Card.Link href="/shop">More Info</Card.Link>
    <Card.Link href="#">Favorite</Card.Link>
  </Card.Body>
</Card>
);