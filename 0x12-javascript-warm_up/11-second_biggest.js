#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);

  let highest = 0;
  let secondHighest = 0;
  for (let i = 0; i < args.length; i++) {
    if (args[i] > highest) {
      secondHighest = highest;
      highest = args[i];
    } else if (args[i] < highest && args[i] > secondHighest) {
      secondHighest = args[i];
    }
  }
  console.log(secondHighest);
}
