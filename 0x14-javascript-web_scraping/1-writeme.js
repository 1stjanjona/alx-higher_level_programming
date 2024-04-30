#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

// Check if the file path and string to write are provided as command-line arguments
if (process.argv.length < 4) {
  console.error('Error: Please provide both the file path and the string to write as command-line arguments.');
  process.exit(1); // Terminate the script with a non-zero exit code to indicate an error
}

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // Use fs.writeFile() to write data to a file specified as the third command-line argument (process.argv[2]).
  // The data to be written is taken from the fourth command-line argument (process.argv[3]).

  if (error) {
    // If an error occurs during the write operation, the 'error' parameter will contain an error object.
    console.error(error);
  }
});
