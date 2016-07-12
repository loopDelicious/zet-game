var React = require("react");
var ReactDOM = require("react-dom");

module.exports = React.createClass({
    componentDidMount: function() {
        console.log('component mounted');
    },

    render: function() {
        return <h1>Hello Joyce</h1>;
    }
})
