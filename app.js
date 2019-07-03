// 导入koa，和koa 1.x不同，在koa2中，我们导入的是一个class，因此用大写的Koa表示:
const Koa = require('koa');
//路由
const router=require("koa-router")()
const exec = require('child_process').exec;
// 创建一个Koa对象表示web app本身:
const app = new Koa();

const call=require('./call.js')
// const filename="E:/Download/social_network/Email-EuAll.txt/Email-EuAll.edgelist"
const filename="./data/email-Eu-core.edgelist"
// 对于任何请求，app将调用该同步函数处理请求：
// 引入
const bodyParser = require('koa-bodyparser')
// 配置中间件
app.use(bodyParser())
// 调用路由中间件
app.use(router.routes())
//社团检测
router.post('/communityDetect', async (ctx, next) => {
    const result=call.communityDetect(filename)
    ctx.response.body=result
})
router.get('/communityDetect', async (ctx, next) => {
    const result=call.communityDetect(filename)
    ctx.response.body=result
})
//最短路径，需要输入参数(起始节点)
router.post('/shortestPath',async(ctx,next)=>{
    console.log(ctx.request.body)
    const {start,end}=ctx.request.body
    const argvs=filename+' '+start+' '+end+' '
    console.log(argvs)
    const result=call.shortestPath(argvs) 
    ctx.response.body=result
})
router.get('/shortestPath',async(ctx,next)=>{
    console.log(ctx.request.body)
    const {start,end}=ctx.request.body
    const argvs=filename+' '+start+' '+end+' '
    console.log(argvs)
    const result=call.shortestPath(argvs) 
    ctx.response.body=result
})
// router.get('/shortestPath',async(ctx,next)=>{
//     console.log(ctx.query)
//     const {start,end}=ctx.query
//     const argvs=filename+' '+start+' '+end+' '
//     console.log(argvs)
//     const result=call.shortestPath(argvs) 
//     ctx.response.body=result
// })
//节点排名，返回每一个节点的排名指数，所有节点排名指数相加等于1
router.post('/pageRank', async (ctx, next) => {
    const result=call.pageRank(filename)
    ctx.response.body=result
})
router.get('/pageRank', async (ctx, next) => {
    const result=call.pageRank(filename)
    ctx.response.body=result
})

// 在端口3000监听:
app.listen(3000);
console.log('app started at port 3000...');