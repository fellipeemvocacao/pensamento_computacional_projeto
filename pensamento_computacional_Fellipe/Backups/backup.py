import shutil
import os
from datetime import datetime

def realizar_backup(pasta_origem, pasta_destino):
    
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não foi encontrada.")
        return


    data_hoje = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destino_final = os.path.join(pasta_destino, f"backup_{data_hoje}")

    try:
      
        shutil.copytree(pasta_origem, destino_final)
        
        print("--- Relatório de Backup ---")
        print(f"Origem: {os.path.abspath(pasta_origem)}")
        print(f"Destino: {os.path.abspath(destino_final)}")
        print(f"Status: Concluído com sucesso às {data_hoje}!")
        
    except Exception as e:
        print(f"Ocorreu um erro durante o backup: {e}")

origem = "meus_documentos"
destino = "disco_externo_backup"

if not os.path.exists(origem):
    os.makedirs(origem)
    with open(os.path.join(origem, "projeto.txt"), "w") as f:
        f.write("Conteúdo importante.")

realizar_backup(origem, destino)