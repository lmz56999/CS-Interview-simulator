
# 模拟面试机器人部署指南（Render）

1. 注册登录 https://render.com
2. 创建新 Web Service，连接你的 GitHub 仓库
3. 设置环境变量：
   - OPENAI_API_KEY=你的OpenAI密钥
4. 构建设置：
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py
5. 部署成功后，你将获得一个网址，例如：
   https://mock-interview-api.onrender.com/interview

你可以在前端网页中使用 fetch 调用此接口。
