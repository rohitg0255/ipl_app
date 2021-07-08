 function getdata(){
    fetch('/csv')
    .then((res)=>res.json())
    .then(function(data){
    let x=[];
    let y=[];
    for(var i=1;i<data.length;i++){
        x.push(data[i][0]);
        y.push(parseInt(data[i][1]));
    }
    var data = [{
    x: x,
    y: y,
    type: 'bar'
  }];

Plotly.newPlot('bar', data);
    })
}
document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('button').onclick=getdata;
    })

//    const res=await fetch('/csv');
//    const data=await res.json();
//    console.log(data.length);
//    console.log(typeof data);
//
//    console.log(x ,y);
//    }
//    return data
//    for ()
//    console.log(data[0][0]);
//}
//async function d() {
//  let y= await getdata();
//  console.log(y[0]);
//}
//let c=getdata();
//console.log(c);
//d=getdata();
//d.then((values)=>{console.log(values);});
//console.log(typeof d);
//window.onLoad= getdata=>{
//
//}



//function init() {
//      var xhttp = new XMLHttpRequest();
//
//      xhttp.onreadystatechange = function() {
//        if (this.readyState == 4 && this.status == 200) {
//            console.log(0);
//            console.log(this.responseText);    }
//      };
//      xhttp.open("GET", '/csv', true);
//      xhttp.send();
//
//    }
//
//function loadDoc() {
//  var xhttp = new XMLHttpRequest();
//  xhttp.onreadystatechange = function() {
//    if (this.readyState == 4 && this.status == 200) {
//     var c=document.getElementById("data").innerHTML ;
//     console.log(c)
//    }
//  };
//  xhttp.open("GET", "/csv", true);
//  xhttp.send();
//}
//    window.onload=loadDoc;