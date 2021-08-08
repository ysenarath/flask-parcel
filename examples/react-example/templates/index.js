import ReactDOM from 'react-dom';
import React from 'react';

import * as bootstrap from 'bootstrap';

class Welcome extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            name: 'Unknown Two'
        };
    }

    componentDidMount() {
        fetch('/get_name')
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        name: result.name,
                    });
                },
                (error) => {
                    this.setState({
                        error: error,
                        isLoaded: true,
                    });
                }
            )
    }

    render() {
        return <h1>Hello, {this.state.name}</h1>;
    }
}

ReactDOM.render(
    <Welcome/>,
    document.getElementById('root')
);