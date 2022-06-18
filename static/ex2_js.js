function calc() {
    var price = document.getElementById("cookies").value
    var val = document.getElementById("Amount").value;
    var tot_price = val * price;
    var divobj = document.getElementById('total');
    divobj.value = tot_price;
}

function changeByOpeningHours(){
    if (new Date().getHours() > 10 && new Date().getHours() < 20){
        document.getElementById("open").innerHTML = ' WE ARE OPEN NOW';
    }
    else{
        document.getElementById("open").innerHTML = 'WE ARE CLOSE NOW';
    }
}

function markOnNav() {
    for (var i = 0; i < document.links.length; i++) {
        if (document.links[i].href === document.URL) {
            thisPage = i;
        }
    }
    document.links[thisPage].className = 'thisPage';
}



