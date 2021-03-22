#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const argv = process.argv.slice(2);
  argv.sort(function (a, b) { return b - a; });
  console.log(argv[1]);
}
