var app = new Vue({
    el: '#app',
    data: {
        upper_symps_list: [],
        lower_symps_list: [],
        skin_symps_list: [],
        general_symps_list: [],
        symp_names: {},
        checkedSymptoms: []
    },
    created: function() {
        $.getJSON(window.location.origin + '/static/js/symptoms.json', function(data) {
            for(let attr in data) {
                this[attr] = data[attr]
                for(let pair in data[attr]) {
                    this['symp_names'][pair['code']] = pair['name']
                }
            }
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