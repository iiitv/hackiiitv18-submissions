import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Register from "./Register";
import About from "./About";
import RequestList from './RequestList';
import NewRequest from './NewRequest';
import AboutRequest from './AboutRequest';
import Home from './Home';
import AboutUs from './AboutUs';
import ContactUs from './ContactUs';

import * as serviceWorker from './serviceWorker';
import {
    BrowserRouter as Router,
    Route,
    Link
  } from 'react-router-dom'

  import { List, Avatar, Button, Spin, Menu, Icon } from 'antd';



ReactDOM.render(
    <Router>
        <div>
            <Menu
                theme="dark"
                mode="horizontal"
                defaultSelectedKeys={["1"]}
                style={{ lineHeight: '64px' }}
                breakpoint="lg"
                collapsedWidth="0"
            >
                <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
                <Menu.Item key="2"><Link to="/projects">Project List</Link></Menu.Item>
                <Menu.Item key="3"><Link to="/aboutus">About Us</Link></Menu.Item>
                <Menu.Item key="4"><Link to="/contactus">Contact Us</Link></Menu.Item>
                {/* <span style={{
                    marginRight: '20px',
                    float: 'right'
                }} > */}
                <Icon style={{ fontSize: '20px', color: 'blue', margin: '10px' }} type="facebook" theme="outlined" />
                <Icon style={{ fontSize: '20px', color: 'red', margin: '10px' }} type="youtube" theme="outlined" />
                <Icon style={{ fontSize: '20px', color: '#08c', margin: '10px' }} type="twitter" theme="outlined" />
                <Icon style={{ fontSize: '20px', color: 'pink', margin: '10px' }} type="instagram" theme="outlined" />
                {/* </span> */}
                {/* <Menu.Item key="5"><Icon spin={true} type="plus-circle" className="publish-btn" /></Menu.Item>
                <Menu.Item key="6"><Icon spin={true} type="login" className="losggin-btn" /></Menu.Item> */}
            </Menu>
          <Route exact path="/" component={Home}/>
          <Route exact path="/projects" component={App}/>
          <Route exact path="/addproject"  component={Register} />
          <Route exact path="/aboutus" component={AboutUs} />
          <Route exact path="/contactus" component={ContactUs} />
          <Route exact path="/about" component={About} />
          <Route exact path="/requests" component={RequestList} />
          <Route exact path="/newrequest"  component={NewRequest} />
          <Route exact path="/aboutrequest" component={AboutRequest} />
        </div>
    </Router>
    
    , document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
