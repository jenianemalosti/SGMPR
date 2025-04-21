import oracledb
import json

# Função de conexão com o banco de dados
def conectar_oracle():
    dsn = oracledb.makedsn('localhost', '1521', service_name='xe')
    conn = oracledb.connect(user='system', password='1234', dsn=dsn)
    return conn

# --- PRODUTORES ---

def cadastrar_produtor(nome, propriedade, tipo_cultivo):
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        query = """INSERT INTO produtores (id_produtor, nome, propriedade, tipo_cultivo)
                   VALUES (seq_produtor.NEXTVAL, :nome, :propriedade, :tipo_cultivo)"""
        cursor.execute(query, {'nome': nome, 'propriedade': propriedade, 'tipo_cultivo': tipo_cultivo})
        conn.commit()
        print(f"\n✅ Cadastro concluído com êxito!")
    except oracledb.Error as e:
        print(f"💥 Erro ao cadastrar produtor: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        voltar_ou_sair()

def alterar_produtor(id_produtor, nome, propriedade, tipo_cultivo):
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        query = """UPDATE produtores 
                   SET nome = :nome, propriedade = :propriedade, tipo_cultivo = :tipo_cultivo
                   WHERE id_produtor = :id_produtor"""
        cursor.execute(query, {'id_produtor': id_produtor, 'nome': nome, 'propriedade': propriedade,
                               'tipo_cultivo': tipo_cultivo})
        conn.commit()
        if cursor.rowcount == 0:
            print(f"\n❌ Nenhum produtor com ID {id_produtor} foi encontrado.")
        else:
            print(f"\n✅ Alteração concluída com êxito!")
    except oracledb.Error as e:
        print(f"💥 Erro ao alterar produtor: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        voltar_ou_sair()

def excluir_produtor(id_produtor):
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM produtores WHERE id_produtor = :id", {'id': id_produtor})
        existe = cursor.fetchone()[0]

        if existe == 0:
            print(f"\n❌ Produtor com ID {id_produtor} não encontrado.")
        else:
            cursor.execute("DELETE FROM produtores WHERE id_produtor = :id", {'id': id_produtor})
            conn.commit()
            print(f"\n✅ Produtor excluído com sucesso.")
    except oracledb.Error as e:
        print(f"💥 Erro ao excluir produtor: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        voltar_ou_sair()

def listar_produtores():
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtores")
        produtores = cursor.fetchall()
        print("\n📋 Lista de Produtores:")
        for p in produtores:
            print(f"ID: {p[0]} | Nome: {p[1]} | Propriedade: {p[2]} | Cultivo: {p[3]}")
    except oracledb.Error as e:
        print(f"💥 Erro ao listar produtores: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# --- INSUMOS ---

def cadastrar_insumo(nome, quantidade, tipo, unidade):
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        query = """INSERT INTO insumos (id_insumo, nome, quantidade, tipo, unidade)
                   VALUES (seq_insumo.NEXTVAL, :nome, :quantidade, :tipo, :unidade)"""
        cursor.execute(query, {'nome': nome, 'quantidade': quantidade, 'tipo': tipo, 'unidade': unidade})
        conn.commit()
        print(f"\n✅ Insumo '{nome}' cadastrado com êxito!")
    except oracledb.Error as e:
        print(f"💥 Erro ao cadastrar insumo: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def monitorar_insumos():
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM insumos")
        insumos = cursor.fetchall()
        print("\n📋 Lista de Insumos:")
        for i in insumos:
            print(f"ID: {i[0]} | Nome: {i[1]} | Quantidade: {i[2]} | Tipo: {i[3]} | Unidade: {i[4]}")
    except oracledb.Error as e:
        print(f"💥 Erro ao listar insumos: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def gerar_relatorio_insumos():
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, tipo, unidade, SUM(quantidade) FROM insumos GROUP BY nome, tipo, unidade")
        insumos = cursor.fetchall()
        print("\n📊 Relatório de Insumos:")
        for i in insumos:
            print(f"Nome: {i[0]} | Tipo: {i[1]} | Unidade: {i[2]} | Quantidade total: {i[3]}")
    except oracledb.Error as e:
        print(f"💥 Erro ao gerar relatório: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def salvar_relatorio_insumos_txt():
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, tipo, unidade, quantidade FROM insumos")
        insumos = cursor.fetchall()
        with open("relatorio_insumos.txt", "w", encoding="utf-8") as f:
            for i in insumos:
                f.write(f"Nome: {i[0]}, Tipo: {i[1]}, Unidade: {i[2]}, Quantidade: {i[3]}\n")
        print("✅ Relatório salvo em 'relatorio_insumos.txt'")
    except Exception as e:
        print(f"Erro ao salvar relatório: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# --- JSON ---

def exportar_produtores_json():
    try:
        conn = conectar_oracle()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtores")
        produtores = cursor.fetchall()
        dados = [{"id": p[0], "nome": p[1], "propriedade": p[2], "tipo_cultivo": p[3]} for p in produtores]
        with open("produtores.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4)
        print("✅ Exportado para 'produtores.json'")
    except Exception as e:
        print(f"Erro ao exportar: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def importar_produtores_json():
    try:
        with open("produtores.json", "r", encoding="utf-8") as f:
            produtores = json.load(f)
        conn = conectar_oracle()
        cursor = conn.cursor()
        for p in produtores:
            cursor.execute("INSERT INTO produtores (id_produtor, nome, propriedade, tipo_cultivo) VALUES (:1, :2, :3, :4)",
                           (p["id"], p["nome"], p["propriedade"], p["tipo_cultivo"]))
        conn.commit()
        print("✅ Produtores importados com sucesso.")
    except FileNotFoundError:
        print("⚠️ Arquivo 'produtores.json' não encontrado.")
    except Exception as e:
        print(f"Erro ao importar: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# --- UTILITÁRIO ---

def voltar_ou_sair():
    opcao = input("\nDeseja voltar ao menu principal (s) ou sair (n)? ").lower()
    if opcao != 's':
        print("Saindo... 👋")
        exit()

def menu():
    print("\n=== Sistema de Gestão e Monitoramento de Produção Rural ===")
    print("1. Cadastrar Produtor")
    print("2. Alterar Produtor")
    print("3. Excluir Produtor")
    print("4. Listar Produtores")
    print("5. Cadastrar Insumo")
    print("6. Monitorar Insumos")
    print("7. Gerar Relatório de Insumos")
    print("8. Exportar produtores para JSON")
    print("9. Importar produtores de JSON")
    print("10. Salvar relatório de insumos em TXT")
    print("11. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do produtor: ")
            propriedade = input("Propriedade: ")
            tipo = input("Tipo de cultivo: ")
            cadastrar_produtor(nome, propriedade, tipo)
        elif escolha == "2":
            listar_produtores()
            try:
                idp = int(input("ID do produtor: "))
                nome = input("Novo nome: ")
                propriedade = input("Nova propriedade: ")
                tipo = input("Novo tipo de cultivo: ")
                alterar_produtor(idp, nome, propriedade, tipo)
            except ValueError:
                print("❌ ID inválido.")
        elif escolha == "3":
            listar_produtores()
            try:
                idp = int(input("ID do produtor: "))
                excluir_produtor(idp)
            except ValueError:
                print("❌ ID inválido.")
        elif escolha == "4":
            listar_produtores()
        elif escolha == "5":
            nome = input("Nome do insumo: ")
            quantidade = float(input("Quantidade: "))
            unidade = input("Unidade de medida: ")
            tipo = input("Tipo (semente, fertilizante, etc.): ")
            cadastrar_insumo(nome, quantidade, tipo, unidade)
        elif escolha == "6":
            monitorar_insumos()
        elif escolha == "7":
            gerar_relatorio_insumos()
        elif escolha == "8":
            exportar_produtores_json()
        elif escolha == "9":
            importar_produtores_json()
        elif escolha == "10":
            salvar_relatorio_insumos_txt()
        elif escolha == "11":
            print("Saindo... 👋")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    main()
