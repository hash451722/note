# FastAPI note

## 実行方法


```
$ uvicorn app:app --port 8080  --reload 
```

または、次のPythonファイルを実行

```
from fastapi import FastAPI
import uvicorn
 
app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app=app, port=8080, reload=True)
```
