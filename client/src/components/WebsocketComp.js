import React, { Component } from 'react';

class WebsocketComp extends Component {
  ws = new WebSocket('ws://localhost:5000/api')
  state = {
    input:'',
    messages:[]
  }

  componentDidMount() {
    this.ws.onopen = () => {
      console.log('the websocket is open')
    }
    let that = this
    this.ws.onmessage = function(msg) {
      that.setState({ messages: that.state.messages.concat(msg.data) })
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
        {this.state.messages.map(x => <h1 key={Math.random()}>{x}</h1>)}
      </div>
    )
  }
}

export default WebsocketComp;
