import React, { Component } from 'react';
import './App.css';
import { List, Avatar, Button, Spin, Menu, Icon, Card } from 'antd';
import { Row, Col } from 'antd';
import img from './image/back.jpg';

class ContactUs extends Component {
  render() {
    return (
      <div align="center" style={{ background: '#ECECEC', padding: '30px' }}>
        <Card>
            <h1 style={{fontSize: "50px"}}>Contact Us</h1>
            <h3>
              <b>Phone Number :</b> 8988989898
            </h3>
            <h3>
            <b>Email :</b> helpothers@help.com
            </h3>
                <Icon style={{ fontSize: '32px', color: 'blue', margin: '20px' }} type="facebook" theme="outlined" />
                <Icon style={{ fontSize: '32px', color: 'red', margin: '20px' }} type="youtube" theme="outlined" />
                <Icon style={{ fontSize: '32px', color: '#08c', margin: '20px' }} type="twitter" theme="outlined" />
                <Icon style={{ fontSize: '32px', color: 'pink', margin: '20px' }} type="instagram" theme="outlined" />
            </Card>
      </div>
    );
  }
}


export default ContactUs;