A utility repository that automatically retrieves data of accepted papers from conferences hosted on openreview and using OpenAI GPT4, generates relavent categories and appropriately sorts the papers in them.

## Setup
```bash
pip install openreview-py
```

## Usage
1. List out all venues and find the one you want,
    
    ```python openreview_retriever.py --email <valid openreview email> --password <corresponding pswd> --venues```
2. Replace the venue name [here](https://github.com/ShivinDass/paper_sorter/blob/6e0d9154041455d6a18530fb305fa75ef76af581/openreview_retriever.py#L5).
3. Retreive papers: 

    ```python openreview_retriever.py --email <valid openreview email> --password <corresponding pswd> --output_file submission.txt```