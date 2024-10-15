const prompt = require("prompt-sync")();

function inverterString(str) {
  return str.split("").reverse().join("");
}

const string = prompt("Digite a palavra a ser invertida: ");

const stringInvertida = inverterString(string);

console.log("String original:", string);
console.log("String invertida:", stringInvertida);
