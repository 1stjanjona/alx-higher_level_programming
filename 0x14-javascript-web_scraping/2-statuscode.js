#!/usr/bin/node

const request = require('request');
// Import the 'request' module.

// Check if the URL to request is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Error: Please provide the URL to request as a command-line argument.');
  process.exit(1); // Terminate the script with a non-zero exit code to indicate an error
}

request.get(process.argv[2])
// Use the 'request' module to perform an HTTP GET request to the URL.

  .on('response', function (response) {
    // Set up an event listener for the 'response' event emitted by the HTTP request.

    console.log(`code: ${response.statusCode}`);
    // Log the HTTP status code of the response to the console.
  });
