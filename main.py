from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates

from io import BytesIO

from myOwnStreamCipher import myOwnStreamCipher

app = FastAPI()

@app.get('/')
async def home(request: Request):
    return FileResponse('streamcipher.html')

@app.post('/encrypt_text2text')
async def encrypt_text2text(plain_text: str = Form(None), key: str = Form(None)):
    buf = myOwnStreamCipher(plain_text, key)
    return buf

@app.post('/encrypt_text2file')
async def encrypt_text2file(plain_text: str = Form(None), key: str = Form(None)):
    buf = BytesIO((myOwnStreamCipher(plain_text, key).encode('latin-1')))
    return StreamingResponse(buf, media_type='text/plain')

@app.post('/encrypt_file')
async def encrypt_file(plain_file: UploadFile = File(None), key: str = Form(None)):
    return StreamingResponse(BytesIO(myOwnStreamCipher((await plain_file.read()).decode('latin-1'), key).encode('latin-1')), media_type=plain_file.content_type)

@app.post('/decrypt_text')
async def decrypt_text(cipher_text: str = Form(None), key: str = Form(None)):
    return myOwnStreamCipher(cipher_text.encode('latin-1').decode('unicode-escape'), key)

@app.post('/decrypt_file')
async def decrypt_file(cipher_file: UploadFile = File(None), key: str = Form(None)):
    return StreamingResponse(BytesIO(myOwnStreamCipher((await cipher_file.read()).decode('latin-1'), key).encode('latin-1')), media_type=cipher_file.content_type)