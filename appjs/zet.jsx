var React = require("react");
var ReactDOM = require("react-dom");
var $ = require("jquery");

function display_cards(cards) {
    for (var i = 0; i < cards.length; i++) {

    }
}

module.exports = React.createClass({
    getInitialState: function(){
        return {
            showCards: false,
            cards: [{
                color: 'red', 
                shape: 'triangle',
                fill: 'empty',
                count: '3'
            }],
        }
    },

    componentDidMount: function() {
        console.log('component mounted');
        $.ajax({
            type: "GET",
            url: '/generate_display',
            success: function(cards) { 
              this.setState({
                cards: cards
              })
            }.bind(this)
        });
    },

    render: function() {

        // var table;
        // var card_number = 1;
        // for (var i = 0; i <= 3; i++) {
        //     var row;
        //     for (var j = 0; j <= 4; j++) {
        //         row.push(<td>{ card_number }</td>);
        //         card_number ++;
        //     }
        //     table += (
        //         <tr>
        //             { row }
        //         </tr>
        //     );
        // }

        
        var card_list = this.state.cards.map(function(card) {
            return <li>
                { card.color + ', ' + card.shape + ', ' + card.fill + ', ' + card.count }
            </li>
        })

        return (
            <div>
                <ol className='cards'>
                    { card_list }
                </ol>
            </div>
        );
    }
})


