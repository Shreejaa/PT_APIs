$(document).ready(function(){
    var url = 'http://localhost:5000/periodictable';
    $.ajax({
        url: url+'/standard_states/',
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        },
        success: function(response){
            var state = response["states"];
            var htmlcode = "<select onchange='generate_state_ele()' class='form-select' aria-label='Default select example' id='state_op'>"+
                            "<option selected>Select a Standard state</option>"
            for(var i=0; i<state.length; i++){
                htmlcode += "<option value='"+state[i]+"'>"+state[i]+"</option>";
            }
            htmlcode += "</select>"
            $("#state").html(htmlcode);
        },
        error: function(error){
            alert("ERROR")
            console.log(error)
        }
    })
    
    sleep(7000);
    $.ajax({
        url: url+'/classifications/',
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        },
        success: function(response){
            var state = response["classifications"];
            var htmlcode = "<select onchange='generate_clss_ele()' class='form-select' aria-label='Default select example' id='clss_op'>"+
                            "<option selected>Select a Classifications</option>"
            for(var i=0; i<state.length; i++){
                htmlcode += "<option value='"+state[i]+"'>"+state[i]+"</option>";
            }
            htmlcode += "</select>"
            $("#clss").html(htmlcode);
        },
        error: function(error){
            alert("ERROR")
            console.log(error)
        }
    }) 
    
    sleep(2000);
    $.ajax({
        url: url+'/blocks/',
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        },
        success: function(response){
            var state = response["blocks"];
            var htmlcode = "<select onchange='generate_block_ele()' class='form-select' aria-label='Default select example' id='block_op'>"+
                            "<option selected>Select a Block</option>"
            for(var i=0; i<state.length; i++){
                htmlcode += "<option value='"+state[i]+"'>"+state[i]+"</option>";
            }
            htmlcode += "</select>"
            $("#block").html(htmlcode);
        },
        error: function(error){
            alert("ERROR")
            console.log(error)
        }
    })
    
    sleep(2000);
    $.ajax({
        url: url+'/groups/',
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        },
        success: function(response){
            var state = response["groups"];
            var htmlcode = "<select onchange='generate_group_ele()' class='form-select' aria-label='Default select example' id='group_op'>"+
                            "<option selected>Select a Group</option>"
            for(var i=0; i<state.length; i++){
                htmlcode += "<option value='"+state[i]+"'>"+state[i]+"</option>";
            }
            htmlcode += "</select>"
            $("#group").html(htmlcode);
        },
        error: function(error){
            alert("ERROR")
            console.log(error)
        }
    })
    sleep(2000);
    $.ajax({
        url: url+'/periods/',
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        },
        success: function(response){
            var state = response["periods"];
            var htmlcode = "<select onchange='generate_period_ele()' class='form-select' aria-label='Default select example' id='period_op'>"+
                            "<option selected>Select a Period</option>"
            for(var i=0; i<state.length; i++){
                htmlcode += "<option value='"+state[i]["number"]+"'>"+state[i]["period"]+"</option>";
            }
            htmlcode += "</select>"
            $("#period").html(htmlcode);
        },
        error: function(error){
            alert("ERROR")
            console.log(error)
        }
    })
    
});

function generate_state_ele(){
    var url = 'http://localhost:5000/periodictable/standard_state/'+$("#state_op").val()+'/';
    generate_ele(url)
}

function generate_clss_ele(){
    var url = 'http://localhost:5000/periodictable/classification/'+$("#clss_op").val()+'/';
    generate_ele(url)
}

function generate_block_ele(){
    var url = 'http://localhost:5000/periodictable/block/'+$("#block_op").val()+'/';
    generate_ele(url)
}

function generate_group_ele(){
    var url = 'http://localhost:5000/periodictable/group/'+$("#group_op").val()+'/';
    generate_ele(url)
}

function generate_period_ele(){
    var url = 'http://localhost:5000/periodictable/period/'+$("#period_op").val()+'/';
    generate_ele(url)
}

function generate_ele(url){
    var dis = document.getElementById('result')
    if(dis.style.display == "none"){
        dis.style.display = "block";
    }
    document.getElementById("rtable").innerHTML = ""
    $.ajax({
        url: url,
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Methods","GET")
            request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        },
        success: function(response){
            var ele = response["elements"];
            var table = document.getElementById('rtable');
            len1 = ele.length
            console.log(len1)
            if(len1>5){
                    for(var i = 0,l = 0;i<len1;l++){
                        var row = table.insertRow(l);
                        addCol(row, '<a id="'+ ele[i]["symbol"]+'" onclick="get_ele(this)">'+ele[i]["name"]+'</a>');
                        if(i+1<len1){
                            addCol(row,  '<a id="'+ ele[i+1]["symbol"]+'" onclick="get_ele(this)">'+ele[i+1]["name"]+'</a>');
                        }
                        if(i+2<len1){
                            addCol(row,  '<a id="'+ ele[i+2]["symbol"]+'" onclick="get_ele(this)">'+ele[i+2]["name"]+'</a>');
                        }
                        if(i+3<len1){
                            addCol(row,  '<a id="'+ ele[i+3]["symbol"]+'" onclick="get_ele(this)">'+ele[i+3]["name"]+'</a>');
                        }
                        if(i+4<len1){
                            addCol(row,  '<a id="'+ ele[i+4]["symbol"]+'" onclick="get_ele(this)">'+ele[i+4]["name"]+'</a>');
                        }
                        i = i + 5
                        table.appendChild(row);
                        }
                        }
                    else{
                        var row = table.insertRow(0);
                        for(var i =0;i<ele.length;i++){
                            addCol(row, '<a id="'+ ele[i]["symbol"]+'" onclick="get_ele(this)">'+ele[i]["name"]+'</a>')
                        }
                    }
        }
    })
}

function addCol(tr,val){
    var col = document.createElement('td');
    col.innerHTML = val;
    tr.appendChild(col);
}


function get_ele(a){
    var dis = document.getElementById('elementDetails')
    console.log(dis.style.display)
    if(dis.style.display == "none"){
        dis.style.display = "block";
    }
    document.getElementById("ele_detail").innerHTML = ""
    var url = 'http://localhost:5000/periodictable/element/'+a.id+'/';
    $.ajax({
        url: url,
        type: 'GET',
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin","*")
            request.setRequestHeader("Access-Control-Allow-Methods","GET")
            request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        },
        success: function(response){
            var ele = response
            var table = document.getElementById('ele_detail');
                var keys = Object.keys(ele);
                var i =0;
                keys.forEach(function(key){
                    var row = table.insertRow(i);
                    addCol(row,key)
                    addCol(row," : ")
                    addCol(row,ele[key])
                    i = i+1
                })
            console.log(ele)

        }
    })
}

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}
