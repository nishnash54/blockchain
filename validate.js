function myFunction(arr) {
	console.log("Connected");
var hash = document.getElementById("hash").value;
console.log(hash);
var xmlhttp = new XMLHttpRequest();
var url = "http://localhost:5000/validate?hash="+hash;
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var Arr = JSON.parse(this.responseText);
    console.log(Arr);
    response(Arr)
  }
};

xmlhttp.open("GET", url, true);
xmlhttp.send();
	
}

function response(arr){
console.log(arr)
	if (arr){
		if(Array.from(document.getElementById("result").classList).includes("invalid"))
			document.getElementById("result").classList.remove("invalid")
		if(!Array.from(document.getElementById("result").classList).includes("valid"))
			{
			document.getElementById("result").classList.add("valid");
    		document.getElementById("result").innerHTML = "VALID";
    	}
    }
  //else for 0
  else
  {		if(Array.from(document.getElementById("result").classList).includes("valid"))
			document.getElementById("result").classList.remove("valid")
		if(!Array.from(document.getElementById("result").classList).includes("invalid"))	
  			{
  				document.getElementById("result").classList.add("invalid");
  			 	document.getElementById("result").innerHTML = "INVALID";
  			}
  	}
}
