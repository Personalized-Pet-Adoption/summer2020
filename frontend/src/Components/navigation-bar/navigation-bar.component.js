import React from 'react';
import { Link } from 'react-router-dom';
import './navigation-bar.styles.css';


const NavBar = () => (
<div class = "mid-panel">
<div class = "tab-bar">
    <div class= "arrange-as-row tab-row">
        <button class = "tab-btn active-tab" type="button" name="tradeboard">Trade Board</button>
        <button class = "tab-btn" type="button" name="bookmark">My Favorites</button>
        <button class = "tab-btn" type="button" name="sell-list">My Pets </button>
    </div>
    <div class= "extra">
        <hr class="tab-divider"/>
        <div class= "arrange-as-row">
            <p class = "question">Do you have a book that you'd like to sell?</p>
            {/* <button class = "sell-btn" onclick="newPostForm()">Sell A Book</button> */}
        </div>
    </div>
</div>
</div>
);

export default NavBar;