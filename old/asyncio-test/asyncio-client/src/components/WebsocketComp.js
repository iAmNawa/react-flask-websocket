import React, { Component } from 'react';

class WebsocketComp extends Component {
  ws = new WebSocket('ws://localhost:8765')
  state = {
    input:'',
    messages:''
  }

  componentDidMount() {
    this.ws.onopen = () => {
      console.log('the websocket is open')
    }
    this.ws.onmessage = function(msg) {
      console.log(msg.data)
    }
  }

  onChange = (e) => {
    this.setState({ input: e.target.value })
  }

  onClick = () => {
    this.ws.send(this.state.input)
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
