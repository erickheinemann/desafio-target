const prompt = require("prompt-sync")();

function Fibonacci(numero) {
  let a = 0;
  let b = 1;
  let temp;

  if (numero === 0 || numero === 1) {
    return true;
  }

  while (b < numero) {
    temp = a + b;
    a = b;
    b = temp;
  }

  return b === numero;
}

const numero = parseInt(prompt("Digite o número: "));

if (Fibonacci(numero)) {
  console.log(`O número ${numero} faz parte da sequência de Fibonacci.`);
} else {
  console.log(`O número ${numero} não faz parte da sequência de Fibonacci.`);
}
