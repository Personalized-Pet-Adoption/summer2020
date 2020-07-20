import React from 'react';
import { Link } from 'react-router-dom';
import './advance-search.styles.css';


const AdvanceSearch = () => (
<div class = "right-panel">
    <div class = "nav">
         {/* {% if user.is_authenticated %} */}
            {/* <a  href="{% url 'profile' %}"> */}
                <button class = "nav-btn" type="button" name="profile" >Profile</button>
            {/* </a> */}
            {/* <a  href="{% url 'logout' %}"> */}
                <button class = "nav-btn" type="button" name="logout" >Logout</button>
            {/* </a> */}
            <button class = "nav-btn" type="button" name="sell" onclick="newPostForm()">Sell A Pet</button>
            {/* {% else %} */}
            {/* <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
            <a class="nav-item nav-link" href="{% url 'register' %}">Register</a> */}
            {/* {% endif %} */}
    </div>
    <div class="form-div">
                {/* {% include "tradeboard/searchForm.html" %} */}
    </div>
</div>
);

export default AdvanceSearch;