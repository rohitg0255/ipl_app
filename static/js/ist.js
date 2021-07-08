const api_url ="/csv";
//document.getElementById('getData').addEventListener('click', getData);
document.getElementById('getapi').addEventListener('click', getapi);
// Defining async function
async function getapi(url) {
fetch(api_url).then((res) => { console.log(res) ;});

//        .then(console.log(res)
//(data) => {
//            let result = `<h2> Random User Info From Jsonplaceholder API</h2>`;
//            data.forEach((user) => {
//                const { id, name, email, address: { city, street } } = user
//                result +=
//                    `<div>
//                     <h5> User ID: ${id} </h5>
//                         <ul class="w3-ul">
//                             <li> User Full Name : ${name}</li>
//                             <li> User Email : ${email} </li>
//                             <li> User Address : ${city}, ${street} </li>
//                         </ul>
//                      </div>`;
//                        document.getElementById('result').innerHTML = result;
//                    });
//                })
    // Storing response
//    const response = await fetch(url);
//
//    // Storing data in form of JSON
////    var data = await response.json();
//    alert(1);
//    console.log(response);
//    if (response) {
//        hideloader();
//    }
//    show(data);
}
// Calling that async function
getapi(api_url);

//function loadDoc() {
//  var xhttp = new XMLHttpRequest();
//  xhttp.open("GET", "/csv", true);
//  xhttp.responseType = 'json';
//
//  xhttp.onreadystatechange = function() {
//    if (this.readyState == 4 && this.status == 200) {
//    console.log(0)
//     console.log(this.responseText);
////     var c=document.getElementById("data").innerHTML ;
////     console.log(c)
//    }
//  };
////  xhttp.open("GET", "/csv", true);
//  xhttp.send();
//}
//    window.onload=loadDoc;
