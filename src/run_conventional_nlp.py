import sys
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def ipynb_to_code(filename: str) -> str:
    with open(f"{filename}") as file:
        notebook = nbformat.read(file, nbformat.NO_CONVERT)
    code = "\n".join([i["source"] for i in notebook["cells"]])
    return code





''' 
    Process datasets
'''
'''
source_code = ipynb_to_code("Process_dataset.ipynb")


for data_name in ["LIAR", "ISOT", "WELFAKE"]:
    context = {'argv' : data_name}
    exec(source_code, context)
'''

'''
    Run classifier models on processed datasets
'''
for i in os.listdir(r"fake_news_classifiers/"):
    code = ipynb_to_code(i)
    exec(i)