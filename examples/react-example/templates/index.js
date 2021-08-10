import ReactDOM from 'react-dom';
import React from 'react';

// import the bootstrap
import * as bootstrap from 'bootstrap';

// import the echarts core module
import * as echarts from 'echarts';

window.onload = function () {
    const canvas = document.getElementById('chart');

    const myChart = echarts.init(canvas);

    window.onresize = function () {
        setTimeout(function () {
            // Resize chart
            myChart.resize();
        }, 200);
    }

    const option = {
        xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [150, 230, 224, 218, 135, 147, 260],
            type: 'line'
        }]
    };

    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }
}

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