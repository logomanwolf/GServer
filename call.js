// call.js
const exec = require('child_process').exec;
const execSync = require('child_process').execSync;
// 异步执行
const communityDetect=(filename)=>{   
    const output=execSync('python comunityDetect.py '+filename)
    var json = output.toString()
    return json
}

const shortestPath=()=>exec('python ',function(error,stdout,stderr){
    if(error) {
        console.info('stderr : '+stderr);
    }
    console.log('exec: ' + stdout);
}
)

const pageRank=()=>exec('python ',function(){
    if(error) {
        console.info('stderr : '+stderr);
    }
    console.log('exec: ' + stdout);
})


module.exports={pageRank,shortestPath,communityDetect}

// // 同步执行
// const ShortestPath = execSync('python web.py')
// console.log('sync: ' + output.toString())
// console.log('over')
