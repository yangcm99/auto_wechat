# Use a pipeline as a high-level helper
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# 加载千问7B模型
model_path = "dataroot/models/Qwen/Qwen2-7B-Instruct"
qa_tokenizer = AutoTokenizer.from_pretrained(model_path)
qa_model = AutoModelForCausalLM.from_pretrained(model_path)
# 创建生成管道
qa_pipeline = pipeline("text-generation", model=qa_model, tokenizer=qa_tokenizer)

# 示例问题
question = "你好"

# 生成答案
answer = qa_pipeline(question)
print("Answer:", answer[0]['generated_text'])