# fastapi_pony

**Fastapi + pony 实践一**：使用@app.on_event("startup")，在Fastapi服务启动后，第一时间将db_session加载到全局的Request中。

注意，在src/model中，每次增加一个库表模块，都需要在____init____.py中import下。


Fastapi + pony 另一种实现方法参见：**[Fastapi + pony 实践二](https://github.com/superxuu/fastapi_pony_2)**
