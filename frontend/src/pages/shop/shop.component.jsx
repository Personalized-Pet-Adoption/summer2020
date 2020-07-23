import React from 'react';

import SHOP_DATA from './shop.data.js';

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
      <div className='shop-page'>
        
      </div>
    );
  }
}

export default ShopPage;
