var webdriverio = require('webdriverio');

var exec = require('child_process').exec;
exec('jar.bat', {cwd:"bin", encoding:"utf8"}, function(err, stdout, stderr) {
       if (err) throw err;
});

var options = {
    desiredCapabilities: {
        browserName: 'firefox'
    }
};

webdriverio
  .remote(options)
  .init()
  .url('http://www.bbc.com/') // navigate to the web page
  .setValue('#orb-search-q', ['surfing'], function(){}) // find the element and enter the query
  .submitForm('#orb-search-form') // submit the form
  .title(function(err, res) {
      console.log('Title was: ' + res.value); // Confirm the page title
  })
  .saveScreenshot('./snapshot.png'); // Save the screenshot to disk
  //.end();
