
from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 指令模板
INSTRUCTIONS = {
    "hr": """You are an experienced HR recruiter conducting behavioral interviews...""",
    "tech": """You are a senior software engineer conducting technical interviews...""",
    "pm": """You are a product manager conducting interviews...""",
    "mixed": """You are a senior technical interviewer conducting comprehensive mock interviews..."""
}

# 岗位方向补充说明
JOB_FOCUS = {
    "frontend": "Focus the interview questions on frontend technologies such as JavaScript, React, CSS, and browser performance.",
    "backend": "Focus the interview on backend topics such as APIs, databases, concurrency, and system architecture.",
    "fullstack": "Ask questions that assess both frontend and backend skills, and how to coordinate full-stack projects.",
    "algo": "Concentrate on data structures, algorithms, time complexity, and whiteboard coding challenges.",
    "testing": "Focus the interview on software testing strategies, bug tracking, automation frameworks, CI/CD pipelines, and quality assurance processes.",
    "default": "Focus on computer science knowledge and practical skills."
}

@app.route("/interview", methods=["POST"])
def interview():
    data = request.get_json()
    role = data.get("role", "mixed").lower()
    job = data.get("job", "default").lower()
    description = data.get("description", "")
    message = data.get("message", "")

    # 构建指令
    prompt = INSTRUCTIONS.get(role, INSTRUCTIONS["mixed"]) + "\n\n" + JOB_FOCUS.get(job, JOB_FOCUS["default"])
    if description:
        prompt += "\n\nHere is the job description:\n" + description

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ]
    )

    return jsonify({"answer": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
