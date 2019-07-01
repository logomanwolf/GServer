// 导入koa，和koa 1.x不同，在koa2中，我们导入的是一个class，因此用大写的Koa表示:
const Koa = require('koa');
//路由
const router=require("koa-router")()
const exec = require('child_process').exec;
// 创建一个Koa对象表示web app本身:
const app = new Koa();

const call=require('./call.js')
const filename="E:/Download/social_network/Email-EuAll.txt/Email-EuAll.edgelist"
// 对于任何请求，app将调用该异步函数处理请求：
router.get('/communityDetect', async (ctx, next) => {
    const result=call.communityDetect(filename)
    ctx.response.body=result
})
// 调用路由中间件
app.use(router.routes())
// 在端口3000监听:
app.listen(3000);
console.log('app started at port 3000...');