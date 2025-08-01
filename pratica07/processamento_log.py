'''1- Processamento de Logs de Treinamento  
Crie um programa que analisa um arquivo CSV contendo dados de execução de um processo de treinamento. O programa deve:

* Solicitar ao usuário o nome do arquivo CSV (ex: logs_treinamento.csv).  
* Ler os dados usando a biblioteca `pandas`.  
* Calcular a média e o desvio padrão da coluna `tempo_execucao`.  
* Exibir os resultados com duas casas decimais.  
* Tratar erros como arquivo inexistente ou formatação incorreta.

Dica: Use `df['coluna'].mean()` e `df['coluna'].std()` para obter os resultados estatísticos.'''

import pandas as pd

def main():
    nome_arquivo = input("Digite o nome do arquivo CSV: ")

    try:
        #Tenta ler o arquivo CSV
        df = pd.read_csv(nome_arquivo)

        # Verifica se a coluna 'tempo_execucao' existe
        if 'tempo_execucao' not in df.columns:
            print('Erro: a coluna "tempo_execucao" não foi encontrada no arquivo.')
            return

        #Calcula a média e o desvio padrão
        media = df['tempo_execucao'].mean()
        desvio = df['tempo_execucao'].std()

        #Exibe os resultados formatados com duas casas decimais
        print(f'Média do tempo de execução: {media:.2f}')
        print(f'Desvio padrão do tempo de execução: {desvio:.2f}')

    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except pd.errors.EmptyDataError:
        print('Erro: O arquivo está vazio ou mal formatado.')
    except pd.errors.ParserError:
        print('Erro: Não foi possível analisar o arquivo. Revise a formatação.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')

if __name__ == '__main__':
    main()
