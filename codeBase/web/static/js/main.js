var app = new Vue({
    el: '#app',
    data: {
        upper_symps_list: [
            { "name": "sneezing", "code": 1 },
            { "name": "runny nose", "code": 2 },
            { "name": "headache", "code": 3 }
        ]
    },
    created: function() {
        $.getJSON(window.location.origin + '/static/js/symptoms.json', function(data) {
            for(let attr in data) {
                this[attr] = data[attr]
            }
            console.log(this);
        }.bind(this));
    }
});

function openSymp(evt, partName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("symp");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" w3-border-red", "");
    }
    document.getElementById(partName).style.display = "block";
    evt.currentTarget.firstElementChild.className += " w3-border-red";
}