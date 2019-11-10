var app = new Vue({
    el: '#app',
    data: {
        upper_symps_list: [],
        lower_symps_list: [],
        skin_symps_list: [],
        general_symps_list: [],
        symp_names: [],
        checkedSymptoms: []
    },
    created: function() {
        $.getJSON(window.location.origin + '/static/js/symptoms.json', function(data) {
            let items = [];
            for(let [attr, list] of Object.entries(data)) {
                this[attr] = list;
                list.forEach(function(pair) { items[pair['code']] = pair['name']; });
            }
            console.log(items);
            this.symp_names = items;
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