// call.js
const exec = require('child_process').exec;
const execSync = require('child_process').execSync;
// 异步执行
exec('python web.py',function(error,stdout,stderr){
    if(error) {
        console.info('stderr : '+stderr);
    }
    console.log('exec: ' + stdout);
})
// 同步执行
const output = execSync('python web.py')
console.log('sync: ' + output.toString())
console.log('over')
