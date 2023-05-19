# ApiRunner
一个基于swagger接口文档的自动化测试框架,功能包括自动生成用例、自动化测试、测试报告、用例管理等。

## 功能
-  [ ] 支持通过swagger.json文件自动生成接口测试用例（json格式 or pytest）
-  [ ] 支持http(s)协议的GET、POST、PUT、DELETE等方法
-  [ ] 支持响应校验，目前我们只校验了状态码,后续扩展到校验响应内容,headers等。可以使用JSON schema或正则表达式进行校验。
-  [ ] 支持执行mock服务。可以在测试环境启动一个mock服务器,进行接口测试而不依赖实际的服务端。
-  [ ] 支持测试用例的重跑。可以在JSON的测试用例文件中添加测试用例的执行状态,支持对单个或多个失败的测试用例进行重跑。
-  [ ] 支持测试报告定制化。可以生成更加美观的HTML测试报告,包含测试概况,通过/失败情况及失败用例详情等。
-  [ ] 支持CI/CD集成。通过输出标准的测试用例JSON文件,可以与Jenkins, Travis CI等实现自动化测试和部署流程。
-  [ ] 支持测试用例的管理维护。后续将与测试平台进行集成,实现对测试用例的查看、删除、修改、新增功能,方便测试用例的管理维护。
-  [ ] 支持数据驱动扩展。支持从测试数据文件中读取测试数据进行数据驱动，自动生成用例,充分组合接口的所有参数，生成更加全面且细致的接口测试用例。
-  [ ] 支持接口依赖管理。 Swagger在文件中定义接口与接口之间的依赖,实现接口的顺序执行。


## 安装方法
```shell
pip install git+https://github.com/yunfei07/apirunner
```

## 使用方法