const fs = require("fs"); 
const commonmark = require('commonmark');

// Read users.json file 
// fs.readFile("/Users/ehaas/Downloads/USCORE-package-list.json", function(err, data) { 
fs.readFile("/Users/ehaas/Documents/FHIR/davinci-ecdx/input/examples/cdex-document-digital-sig-example.json", function(err, data) { 

    // Check for errors 
    if (err) throw err; 

    // Converting to JSON 
    const history = JSON.parse(data); 
    // console.log(history["introduction"]); // Print users 
    var reader = new commonmark.Parser();
    var writer = new commonmark.HtmlRenderer();
    // var parsed = reader.parse(history["introduction"])
    var parsed = reader.parse(history["meta"]["extension"][1]["valueMarkdown"])
    var result = writer.render(parsed); // result is a String
    console.log(result)
}); 


