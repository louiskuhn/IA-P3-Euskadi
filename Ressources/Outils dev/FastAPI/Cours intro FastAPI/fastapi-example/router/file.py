from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse


router = APIRouter(
  prefix='/file',
  tags=['file']
)

@router.post('/')
def get_file(file: bytes = File(...)):
  content = file.decode('utf-8')
  lines = content.split('\n')
  return {'lines': lines}

@router.post('/uploadfile')
def get_uploadfile(upload_file: UploadFile = File(...)):
  path = f"files/{upload_file.filename}"
  with open(path, 'w+b') as buffer:
    shutil.copyfileobj(upload_file.file, buffer)

  return {
    'filename': path,
    'type': upload_file.content_type
  }

@router.get('/download/{name}', response_class=FileResponse)
def get_file(name: str):
  path = f'files/{name}'
  return path