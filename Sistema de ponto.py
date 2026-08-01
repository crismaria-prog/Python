
import csv
import os




from datetime import datetime, timedelta, time
import csv
import json
from pathlib import Path

# Arquivo para persistir os dados
DATA_FILE = Path(__file__).parent / "dados_ponto.json"
CSV_FILE = Path(__file__).parent / "dados_ponto.csv"


def save_funcionarios(funcionarios):
    data = {}
    for matricula, f in funcionarios.items():
        data[matricula] = {
            "nome": f.get("nome"),
            "senha": f.get("senha"),
            "empresa": f.get("empresa"),
            "pontos": {}
        }
        for dia, p in f.get("pontos", {}).items():
            ser = {}
            for k, v in p.items():
                if isinstance(v, datetime):
                    ser[k] = v.isoformat()
                else:
                    ser[k] = v
            data[matricula]["pontos"][dia] = ser

    with open(DATA_FILE, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def load_funcionarios():
    if not DATA_FILE.exists():
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as fh:
        raw = json.load(fh)

    out = {}
    for matricula, f in raw.items():
        out[matricula] = {
            "nome": f.get("nome"),
            "senha": f.get("senha"),
            "empresa": f.get("empresa"),
            "pontos": {}
        }
        for dia, p in f.get("pontos", {}).items():
            novo = {}
            for k, v in p.items():
                if v is None:
                    novo[k] = None
                elif k in ("entrada", "inicio_almoco", "fim_almoco", "saida") and isinstance(v, str):
                    try:
                        novo[k] = datetime.fromisoformat(v)
                    except Exception:
                        novo[k] = v
                else:
                    novo[k] = v
            out[matricula]["pontos"][dia] = novo

    return out


def exportar_pontos_csv(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    with open(CSV_FILE, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow([
            "matricula",
            "nome",
            "empresa",
            "dia",
            "entrada",
            "inicio_almoco",
            "fim_almoco",
            "saida",
            "sem_almoco",
            "motivo_hora_extra"
        ])

        def fmt(dt):
            if dt is None:
                return ""
            if isinstance(dt, str):
                return dt
            return dt.strftime("%H:%M")

        for matricula, f in funcionarios.items():
            nome = f.get("nome", "")
            empresa = empresas.get(f.get("empresa"), "")
            for dia, p in sorted(f.get("pontos", {}).items()):
                writer.writerow([
                    matricula,
                    nome,
                    empresa,
                    dia,
                    fmt(p.get("entrada")),
                    fmt(p.get("inicio_almoco")),
                    fmt(p.get("fim_almoco")),
                    fmt(p.get("saida")),
                    p.get("sem_almoco", False),
                    p.get("motivo_hora_extra") or ""
                ])

    print(f"Arquivo CSV gerado em: {CSV_FILE}")


# Aqui serão armazenados os funcionários (carregados do disco)
funcionarios = load_funcionarios()


# Unidades da empresa
empresas = {
    "1": "Matriz",
    "2": "Filial 1",
    "3": "Filial 2",
    "4": "Filial 3"
}

# (dados já carregados do disco em `funcionarios`)


while True:
    print("\n==============================")
    print("     SISTEMA DE PONTO")
    print("==============================")
    print("1 - Cadastrar funcionário")
    print("2 - Registrar ponto")
    print("3 - Encerrar sistema")
    print("4 - Visualizar funcionário/pontos")
    print("5 - Exportar registros para CSV")

    opcao = input("Escolha uma opção: ").strip()

    # ==========================================
    # CADASTRO DO FUNCIONÁRIO
    # ==========================================
    if opcao == "1":

        print("\n=== UNIDADES DA EMPRESA ===")
        print("1 - Matriz")
        print("2 - Filial 1")
        print("3 - Filial 2")
        print("4 - Filial 3")

        codigo_empresa = input("Escolha a unidade: ").strip()

        if codigo_empresa not in empresas:
            print("Unidade inválida.")
            continue

        nome = input("Digite o nome do funcionário: ").strip()
        matricula = input("Digite a matrícula: ").strip()
        senha = input("Digite a senha: ").strip()

        if matricula in funcionarios:
            print("Essa matrícula já está cadastrada.")
            continue

        funcionarios[matricula] = {
            "nome": nome,
            "senha": senha,
            "empresa": codigo_empresa,
            "pontos": {}
        }
        save_funcionarios(funcionarios)

        print("\nFuncionário cadastrado com sucesso!")
        print("Nome:", nome)
        print("Unidade:", empresas[codigo_empresa])

    # ==========================================
    # REGISTRO DO PONTO
    # ==========================================
    elif opcao == "2":

        print("\n=== ACESSO DO FUNCIONÁRIO ===")

        matricula = input("Digite sua matrícula: ").strip()
        senha = input("Digite sua senha: ").strip()

        if matricula not in funcionarios:
            print("Matrícula não encontrada.")
            continue

        funcionario = funcionarios[matricula]

        if funcionario["senha"] != senha:
            print("Senha incorreta.")
            continue

        # Obtém a data e hora atuais
        agora = datetime.now()
        data_atual = agora.strftime("%d/%m/%Y")
        hora_atual = agora.time()

        # Cria o registro do dia
        if data_atual not in funcionario["pontos"]:
            funcionario["pontos"][data_atual] = {
                "entrada": None,
                "inicio_almoco": None,
                "fim_almoco": None,
                "saida": None,
                "sem_almoco": False,
                "motivo_hora_extra": None
            }

        ponto = funcionario["pontos"][data_atual]

        print("\nBem-vindo,", funcionario["nome"])
        print("Unidade:", empresas[funcionario["empresa"]])
        print("Data:", data_atual)
        print("Horário atual:", agora.strftime("%H:%M"))

        print("\n1 - Registrar chegada")
        print("2 - Registrar início do almoço")
        print("3 - Registrar retorno do almoço")
        print("4 - Registrar saída")

        tipo_ponto = input("Escolha uma opção: ").strip()

        # ======================================
        # REGISTRAR CHEGADA
        # ======================================
        if tipo_ponto == "1":

            if ponto["entrada"] is not None:
                print("A chegada já foi registrada hoje.")

            elif hora_atual < time(8, 0):
                print("A chegada só pode ser registrada a partir das 08:00.")

            elif hora_atual > time(17, 0):
                print("Não é permitido registrar chegada após as 17:00.")

            else:
                ponto["entrada"] = agora
                save_funcionarios(funcionarios)

                print(
                    "Chegada registrada às",
                    agora.strftime("%H:%M")
                )

                # Chegada depois das 12:00
                if hora_atual > time(12, 0):
                    ponto["sem_almoco"] = True
                    save_funcionarios(funcionarios)

                    print(
                        "Chegada registrada após as 12:00."
                    )
                    print(
                        "O funcionário não poderá registrar horário de almoço."
                    )

        # ======================================
        # INÍCIO DO ALMOÇO
        # ======================================
        elif tipo_ponto == "2":

            if ponto["entrada"] is None:
                print("Primeiro registre a chegada.")

            elif ponto["sem_almoco"]:
                print(
                    "Funcionários que chegaram após as 12:00 "
                    "não podem registrar almoço."
                )

            elif ponto["inicio_almoco"] is not None:
                print("O início do almoço já foi registrado.")

            elif hora_atual > time(13, 0):
                print(
                    "O almoço precisa começar até as 13:00,"
                    " para terminar até as 14:00."
                )

            else:
                ponto["inicio_almoco"] = agora
                save_funcionarios(funcionarios)

                horario_retorno = agora + timedelta(hours=1)

                print(
                    "Início do almoço registrado às",
                    agora.strftime("%H:%M")
                )

                print(
                    "O retorno poderá ser registrado a partir das",
                    horario_retorno.strftime("%H:%M")
                )

        # ======================================
        # RETORNO DO ALMOÇO
        # ======================================
        elif tipo_ponto == "3":

            if ponto["sem_almoco"]:
                print(
                    "Este funcionário não possui horário de almoço hoje."
                )

            elif ponto["inicio_almoco"] is None:
                print("O início do almoço ainda não foi registrado.")

            elif ponto["fim_almoco"] is not None:
                print("O retorno do almoço já foi registrado.")

            else:
                horario_minimo_retorno = (
                    ponto["inicio_almoco"] + timedelta(hours=1)
                )

                if agora < horario_minimo_retorno:
                    print("O intervalo de almoço deve durar 1 hora.")

                    print(
                        "O retorno poderá ser registrado às",
                        horario_minimo_retorno.strftime("%H:%M")
                    )

                else:
                    ponto["fim_almoco"] = agora
                    save_funcionarios(funcionarios)

                    print(
                        "Retorno do almoço registrado às",
                        agora.strftime("%H:%M")
                    )

                    if hora_atual > time(14, 0):
                        print(
                            "Atenção: retorno registrado após as 14:00."
                        )
                        print("Informar o RH.")

        # ======================================
        # REGISTRAR SAÍDA
        # ======================================
        elif tipo_ponto == "4":

            if ponto["entrada"] is None:
                print("A chegada ainda não foi registrada.")

            elif ponto["saida"] is not None:
                print("A saída já foi registrada hoje.")

            elif hora_atual > time(19, 0):
                print(
                    "A saída não pode ser registrada após as 19:00."
                )
                print(
                    "O limite permitido é de 2 horas extras."
                )

            elif (
                ponto["sem_almoco"] == False
                and ponto["fim_almoco"] is None
            ):
                print(
                    "Registre o início e o retorno do almoço "
                    "antes da saída."
                )

            else:
                ponto["saida"] = agora
                save_funcionarios(funcionarios)

                print(
                    "Saída registrada às",
                    agora.strftime("%H:%M")
                )

                # Hora extra depois das 17:00
                if hora_atual > time(17, 0):
                    print("Foram registradas horas extras.")

                    motivo = input(
                        "Informar o RH o motivo das horas extras: "
                    ).strip()

                    ponto["motivo_hora_extra"] = motivo
                    save_funcionarios(funcionarios)

                    print("Motivo registrado com sucesso.")

        else:
            print("Opção de ponto inválida.")

    # ==========================================
    # ENCERRAR SISTEMA
    # ==========================================
    elif opcao == "3":
        print("Sistema encerrado.")
        break

    # ==========================================
    # VISUALIZAR FUNCIONÁRIO E PONTOS
    # ==========================================
    elif opcao == "4":
        print("\n=== VISUALIZAR FUNCIONÁRIO ===")
        matricula_v = input("Digite a matrícula (ou Enter para listar todos): ").strip()

        if matricula_v == "":
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                print("Funcionários cadastrados:")
                for mat, f in funcionarios.items():
                    nome = f.get("nome")
                    emp = empresas.get(f.get("empresa"), "-")
                    print(f"- {mat}: {nome} ({emp})")
            continue

        if matricula_v not in funcionarios:
            print("Matrícula não encontrada.")
            continue

        f = funcionarios[matricula_v]
        print()
        print("Nome:", f.get("nome"))
        print("Unidade:", empresas.get(f.get("empresa"), "-"))

        pontos = f.get("pontos", {})
        if not pontos:
            print("Ainda não há registros de ponto para este funcionário.")
            continue

        print("\nRegistros de ponto:")
        for dia in sorted(pontos.keys()):
            p = pontos[dia]
            def fmt(dt):
                if dt is None:
                    return "-"
                if isinstance(dt, str):
                    return dt
                return dt.strftime("%H:%M")

            print(f"\nData: {dia}")
            print(f"  Entrada: {fmt(p.get('entrada'))}")
            print(f"  Início almoço: {fmt(p.get('inicio_almoco'))}")
            print(f"  Fim almoço: {fmt(p.get('fim_almoco'))}")
            print(f"  Saída: {fmt(p.get('saida'))}")
            motivo = p.get('motivo_hora_extra') or "-"
            print(f"  Motivo hora extra: {motivo}")

    # ==========================================
    # EXPORTAR PARA CSV
    # ==========================================
    elif opcao == "5":
        exportar_pontos_csv(funcionarios)

    else:
        print("Opção inválida.")