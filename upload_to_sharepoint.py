import os
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

# Configurações do SharePoint
SHAREPOINT_SITE_URL = os.environ['SHAREPOINT_SITE_URL']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
FOLDER_PATH = os.environ['FOLDER_PATH']

# Autenticação
credentials = ClientCredential(CLIENT_ID, CLIENT_SECRET)
ctx = ClientContext(SHAREPOINT_SITE_URL).with_credentials(credentials)

# Arquivo a ser enviado
file_path = "/personal/tesouraria4_raggagestao_com_br/Documents/BASE DE DADOS - POWERBI
"  # Substitua pelo caminho do seu arquivo
file_name = os.path.basename(file_path)

# Upload do arquivo
with open(file_path, 'rb') as file_content:
    target_folder = ctx.web.get_folder_by_server_relative_url(FOLDER_PATH)
    target_folder.upload_file(file_name, file_content).execute_query()

print(f"Arquivo '{file_name}' enviado com sucesso para o SharePoint!")
