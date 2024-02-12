#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg));
if (args.length === 0 || args.length === 1) {
	console.log(0);
} else {
	const arg1 = [...new Set(args)];
	const arg2 = arg1.sort((a, b) => b - a);
	console.log(arg2[1]);
}
