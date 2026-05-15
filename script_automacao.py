import subprocess
import datetime

def executar_automacao():
    print(f"=== Iniciando automação em {datetime.datetime.now()} ===")
    
    try:
        # 1. Adicionar todos os arquivos modificados
        print("📝 Adicionando arquivos...")
        subprocess.run(['git', 'add', '.'], check=True)
        
        # 2. Fazer commit com data/hora
        mensagem = f"Atualização automática - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}"
        print(f"💾 Fazendo commit: {mensagem}")
        subprocess.run(['git', 'commit', '-m', mensagem], check=True)
        
        # 3. Fazer push para o GitHub
        print("🚀 Enviando para o GitHub...")
        subprocess.run(['git', 'push'], check=True)
        
        print("✅ Automação concluída com sucesso!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro durante a execução: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    executar_automacao()
