#!/usr/bin/node
exports.esrever = function (list) {
	let len = list.length - 1;
	let i = 0;
	while ((len - i) > 0) {
		const exchange = list[len];
		list[len] = list[i];
		list[i] = exchange;
		i++;
		len--;
	}
	return list;
};
