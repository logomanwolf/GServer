// call.js
const exec = require('child_process').exec;
const execSync = require('child_process').execSync;
//调用python文件来执行
const communityDetect=(filename)=>{   
    const output=execSync('python comunityDetect.py '+filename)
    var json = output.toString()
    return json
}

const shortestPath=(argvs)=>{
    const buffer=execSync('python shortestPath.py '+argvs)
    return buffer.toString()
}

const pageRank= (filename)=>{
    const buffer=execSync('python pageRank.py '+filename)
    return buffer.toString()
}


module.exports={pageRank,shortestPath,communityDetect}

// // 同步执行
// const ShortestPath = execSync('python web.py')
// console.log('sync: ' + output.toString())
// console.log('over')
