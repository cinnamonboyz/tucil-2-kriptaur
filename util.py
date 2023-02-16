from io import BytesIO

def clean(text):
    return "".join(c for c in text.upper() if c.isalpha())

async def read_file(file):
    data = await file.read()
    return data.decode('latin-1')

async def write_file(text):
    buf = BytesIO(text.encode('latin-1'))
    return buf