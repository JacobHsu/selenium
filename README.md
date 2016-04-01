Selenium
---
http://www.seleniumhq.org

### Firefox IDE

[Selenium IDE (Firefox)](http://www.seleniumhq.org/download/)  
Click To Record / Play entire test suite  

[Selenium Commands – “Selenese”](http://www.seleniumhq.org/docs/02_selenium_ide.jsp#selenium-commands-selenese)  

Webdriver.io
---

http://webdriver.io/guide.html

### Installation

[![NPM](https://nodei.co/npm/webdriverio.png?downloads=true&stars=true)](https://www.npmjs.com/package/webdriverio)  

`$ npm install webdriverio --save`  

### selenium-server

http://www.seleniumhq.org/download/

Download version 2.53.0

### Windows Batch Scripting

jar.bat
`$ java -jar selenium-server-standalone-2.53.0.jar`

### Service

將 `jar.bat` 以服務啟動

```js
var exec = require('child_process').exec,child;
child = exec('jar.bat', {cwd:"bin", encoding:"utf8"}, function(err, stdout, stderr) {
       if (err) throw err;
});
```
Windows 工作管理員 / 處理程序
影像名稱: `cmd.exe`
命令列: `C:\Windows\System32\cmd.exe /s/c "jar.bat"`

### webdriver

[ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Usage
`$ node firefox`   
`$ node chrome`  


### Docs

* http://webdriver.io/api/property/getText.html
* https://nodejs.org/api/child_process.html#child_process_child_process_exec_command_options_callback
