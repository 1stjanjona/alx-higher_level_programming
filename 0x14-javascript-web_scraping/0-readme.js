#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

// Check if the file path is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Error: Please provide the file path as a command-line argument.');
  process.exit(1); // Terminate the script with a non-zero exit code to indicate an error
}

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read the contents of a file specified as a command-line argument
  // 'utf8' specifies the encoding of the file being read

  if (error) {
    // If an error occurs during the file read operation, the 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);

  } else {
    // If the file is read successfully, the 'content' parameter will contain the contents of the file as a string.
    console.log(content);
  }
});
