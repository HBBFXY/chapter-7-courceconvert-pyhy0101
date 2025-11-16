import keyword
import re

def convert_non_reserved_to_uppercase(input_path, output_path):
    # 读取源文件内容
    with open(input_path, 'r', encoding='utf-8') as f:
        code_content = f.read()
    
    # 获取Python保留字集合
    reserved_words = set(keyword.kwlist)
    
    # 匹配Python标识符的正则表达式（变量名、函数名等）
    identifier_pattern = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
    
    # 替换函数：保留字不变，其他标识符转为大写
    def replace_identifier(match):
        token = match.group()
        return token if token in reserved_words else token.upper()
    
    # 执行替换操作
    converted_content = identifier_pattern.sub(replace_identifier, code_content)
    
    # 将转换结果写入新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

# 执行转换：读取random_int.py，输出到random_int_upper.py
convert_non_reserved_to_uppercase('random_int.py', 'random_int_upper.py')
print("转换完成！结果已保存至 random_int_upper.py")
