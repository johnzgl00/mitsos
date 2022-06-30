var temp = 5;
var cpuUsage = 48;
var ramUsage = 13;
var storage = 15;
var power = 5.1;
var user = "root";
var bperc = "50%";

const tempString = "Temperature: ";
const cpuString = "CPU Usage: ";
const ramString = "RAM Usage: ";
const storageString = "Free Storage: ";
const powerString = "Power Input: ";
const userString = "Logged In as: ";

const tempText = document.getElementById("temp");
const cpuText = document.getElementById("cpu_usage");
const ramText = document.getElementById("ram_usage");
const storageText = document.getElementById("storage");
const powerText = document.getElementById("power");
const userText = document.getElementById("user");
const batteryPerc = document.getElementById("Bperc");
const batteryPercText = document.getElementById("bperc");

tempText.innerHTML = tempString + temp + "C";
cpuText.innerHTML = cpuString + cpuUsage + "%";
ramText.innerHTML = ramString + ramUsage + "%";
storageText.innerHTML = storageString + storage + "GB";
powerText.innerHTML = powerString + power + "V";
userText.innerHTML = userString + user;
batteryPerc.style.width = bperc;
batteryPercText.innerHTML = bperc;