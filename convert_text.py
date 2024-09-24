import re

def process_bibitem(bibitem_text):
  """
  处理 BibTeX 条目，去除 \bibitem 开头，以及 \newblock 或 \allowbreak 等斜杠带一个单词的 LaTeX 格式，并在前面添加序号。
  同时识别并删除 \bibitem{} 类型的条目。

  Args:
    bibitem_text: BibTeX 条目文本。

  Returns:
    处理后的 BibTeX 条目文本，每行一个条目，并带有序号。
  """

  # 将 BibTeX 文本按条目分割
  bibitem_list = bibitem_text.split('\n\n')

  # 处理每个条目并添加序号
  processed_text = []
  for i, bibitem in enumerate(bibitem_list):
    # 去除 \bibitem 开头
    bibitem = re.sub(r'^\\bibitem\[.*?\].*?\n|^\\bibitem\{.*?\}.*?\n', '', bibitem)

    # 如果条目为空，则跳过
    if not bibitem:
      continue

    # 去除 \newblock 或 \allowbreak 等斜杠带一个单词的 LaTeX 格式
    bibitem = re.sub(r'\\newblock|\\allowbreak', '', bibitem)

    # 将每个条目存储在一行
    bibitem = bibitem.replace('\n', ' ')

    # 添加序号
    processed_text.append(f"[{i+1}] {bibitem}")

  # 将处理后的条目连接成一个字符串
  processed_text = '\n'.join(processed_text)

  return processed_text

# 读取 BibTeX 文件
with open('bibitem.txt', 'r', encoding='utf-8') as f:
  bibitem_text = f.read()

# 处理 BibTeX 条目
processed_text = process_bibitem(bibitem_text)

# 打印处理后的文本
print(processed_text)

# 将处理后的文本写入新文件
with open('processed_bibitem.txt', 'w', encoding='utf-8') as f:
  f.write(processed_text)