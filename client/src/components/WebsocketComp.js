import React, { Component } from 'react';

let ws = new WebSocket('ws://localhost:5000/api')

class WebsocketComp extends Component {
  state = {
    input:''
  }

  componentDidMount() {
    ws.onmessage = function(msg) {
      console.log(msg)
    }
  }

  onChange = (e) => {
    this.setState({ input: e.target.value })
  }

  onClick = () => {
    ws.send(this.state.input)
  }

  render() {
    return (
      <div>
        <input onChange={this.onChange} value={this.state.input}></input>
        <button onClick={this.onClick}>Click me</button>
      </div>
    )
  }
}

export default WebsocketComp;
