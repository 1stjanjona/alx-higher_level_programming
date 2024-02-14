#!/usr/bin/node
function nmOccurences(list, searchElement) {
	return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
module.exports = { nbOccurrences };
