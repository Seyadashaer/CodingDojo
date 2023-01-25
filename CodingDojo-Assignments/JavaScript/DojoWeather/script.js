var cookieMessage = document.querySelector(".cookie")
var tempreatureRatio = 1.8 

//Code review Nasri comment Desc: This funcation will do ... 
function displayAlert() {
    alert("Loading weather report .. ")

}

function dismissCookie() {
    cookieMessage.remove();
}

function convertTemperture(element) {
    for (var i=1; i<=8 ; i++) {
        var tempElement = document.querySelector("#temp" + i);
        var tempValue = parseInt(tempElement.innerText); 
        if (element.value == 1 ) {
            tempElement.innerText = convertToCelsius(tempValue)
        } else {
            tempElement.innerText = convertToFah(tempValue)
        }
        }
    }

function convertToCelsius(temp) {
    return Math.round(1 / tempreatureRatio * (temp - 32));
}

function convertToFah(temp) {
    return Math.round( tempreatureRatio * temp + 32);
}