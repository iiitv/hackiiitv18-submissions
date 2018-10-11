import React, { Component } from 'react';
import './App.css';
import { List, Avatar, Button, Spin, Menu, Icon, Card } from 'antd';
import { Row, Col } from 'antd';
import img from './image/back.jpg';

class AboutUs extends Component {
  render() {
    return (
      <div align="center" style={{ background: '#ECECEC', padding: '30px' }}>
        <Card>
            <h1 style={{fontSize: "50px"}}>About Us</h1>
            <h3>
              Helping people to help
            </h3>
            </Card>
      </div>
    );
  }
}


export default AboutUs;