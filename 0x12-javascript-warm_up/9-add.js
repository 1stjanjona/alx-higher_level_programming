#!/usr/bin/node
function add(a, b) {
	const z = a + b;
	console.log(z);
}
add(Number(process.argv[2]), Number(process.argv[3]));
