# GServer
***
## Description
The back-end for big-graph demo.

## Install
`npm i`
## Start
`nodemon app.js`
## Usage
### basic usage
`localhost:3000/communityDetect                  //detect community`
` localhost:3000/pageRank                         //page rank`
` localhost:3000/shortestPath/1/2                 //The shortest paths from node#1 to node#2.`

### api

|                 |       参数格式        |                             输出                             |
| :-------------: | :-------------------: | :----------------------------------------------------------: |
| communityDetect |           -           |        {0:1,1:1}  //string , 反映每个节点属于哪个社团        |
|    pageRank     |           -           | [('0',0.02),('1',0.01)]//string, 根据权值大小排序，反映每个节点的权值 |
|  shortestPath   | {start：int, end:int} |     [[‘1’,’3’,’2’],[‘1’,’4’,’5’,’2’]] //string, 最短路径     |

## Example

```javascript
var params={start:1,end:2}
$.ajax({
    url:"localhost:3000/shortestPath",
    type:"POST",
    data:params,
    dataType:String,
    success:(data)=>{
        console.log(data);
    }
})
//[[‘1’,’3’,’2’],[‘1’,’4’,’5’,’2’]]
```

