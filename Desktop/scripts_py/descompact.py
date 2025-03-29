import os
import zipfile
from PIL import Image

# Diretório onde os arquivos ZIP estão
zip_dir = "caminho/para/os/zips"
output_dir = "caminho/para/extracao"
merged_tiff_dir = "caminho/para/salvar/tiffs_unidos"

# Criar diretório de saída para os TIFF unidos
os.makedirs(merged_tiff_dir, exist_ok=True)

# Função para unir imagens TIFF em um multipágina
def merge_tiff(tiff_files, output_path):
    if not tiff_files:
        return
    images = [Image.open(img_path) for img_path in tiff_files]
    
    # Salvar o primeiro TIFF com as páginas subsequentes
    images[0].save(output_path, save_all=True, append_images=images[1:])
    print(f"TIFF multipágina salvo: {output_path}")

# Processar todos os arquivos ZIP
for file in os.listdir(zip_dir):
    if file.endswith(".zip"):
        zip_path = os.path.join(zip_dir, file)
        extract_path = os.path.join(output_dir, os.path.splitext(file)[0])

        # Descompactar
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        # Encontrar arquivos TIFF extraídos
        tiff_files = sorted(
            [os.path.join(extract_path, f) for f in os.listdir(extract_path) if f.lower().endswith((".tiff", ".tif"))]
        )

        # Unir TIFFs em um único multipágina
        if tiff_files:
            output_tiff_path = os.path.join(merged_tiff_dir, f"{os.path.splitext(file)[0]}.tiff")
            merge_tiff(tiff_files, output_tiff_path)
