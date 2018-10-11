import React, { Component } from 'react';
import './App.css';
import { Form, Input, Button} from 'antd';
import { Row, Col, Divider } from 'antd';
import { Switch } from 'antd';


const FormItem = Form.Item;


class Register extends Component {
    constructor() {
        super();
        this.state = {
          formLayout: 'horizontal',
        };
      }
      
  render() {
    const { TextArea } = Input;
    const { formLayout } = this.state;
    const formItemLayout = formLayout === 'horizontal' ? {
      labelCol: { span: 6 },
      wrapperCol: { span: 10 },
    } : null;
    const buttonItemLayout = formLayout === 'horizontal' ? {
      wrapperCol: { span: 14, offset: 6 },
    } : null;
    return (
        <div>
            <Row type="flex" justify="center">
                <Col span={12}>
                    <br></br>
                    <h1 style={{display: "flex", justifyContent: "center"}}>Add new Project</h1>
                    <Form layout={formLayout}>
                        <FormItem
                            label="Project Name"
                            {...formItemLayout}
                        >
                            <Input placeholder="Name of project" />
                        </FormItem>
                        <FormItem
                            label="Description"
                            {...formItemLayout}
                        >
                            <TextArea rows={4} />
                        </FormItem>
                        <FormItem
                            label="Founder"
                            {...formItemLayout}
                        >
                            <Input placeholder="Name of founder" />
                        </FormItem>
                        <FormItem
                            label="Contact"
                            {...formItemLayout}
                        >
                            <Input placeholder="Contact details" />
                        </FormItem>
                        <FormItem {...buttonItemLayout}>
                            <Button type="primary">Submit</Button>
                        </FormItem>
                    </Form>
                </Col>
            </Row>
        </div>
    );
  }
}


export default Register;
