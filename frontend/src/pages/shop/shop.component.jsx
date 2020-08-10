import React from 'react';

import SHOP_DATA from './shop.data.js';
import {Link} from 'react-router-dom';
class ShopPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      collections: SHOP_DATA
    };
  }

  render() {
    const { collections } = this.state;
    return (
      <div  >
        <Link to = '/' >To homepage</Link>
        <h1>Pet detail page</h1>
      </div>
    );
  }
}

export default ShopPage;
