#!/usr/bin/python3

#VERIFICA TAREFAS REALIZADAS NA ATIVIDADE AMBIENTE DO DESENVOLVEDOR
#SISTEMAS OPERACIONAIS 
#SCRIPT ELABORADO POR PROF. ROBSON
#COM APOIO DA INTELIGENCIA ARTIFICIAL
##EM 25/11/2024

import subprocess
import time

# Executa o comando do terminal
def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar o comando: {e.output}"

# Teste o comando do terminal (exemplo: 'apache2 -v' ou 'httpd -v')
def check_apache():
    command = "apache2 -v"  # Altere conforme o comando que você quer testar
    result = run_command(command)
    if "Apache" in result:
        return True
    else:
        return False

def check_php():
    command = "php -v"  # Altere conforme o comando que você quer testar
    result = run_command(command)
    if "PHP" in result:
        return True
    else:
        return False

def check_maria():
    command = "mysql --version"  # Altere conforme o comando que você quer testar
    result = run_command(command)
    if "MariaDB" in result:
        return True
    else:
        return False

def check_maria_user(username):
    command = "mysql -u root -e \"SELECT User FROM mysql.user;\""  # Altere conforme o comando que você quer testar
    result = run_command(command)
    if username in result:
        return True
    else:
        return False

# Verificar se o phpMyAdmin está acessível
def check_phpmyadmin():
    command = "curl -sL http://localhost/phpmyadmin | grep phpMyAdmin"
    result = run_command(command)
    if "phpMyAdmin" in result:
        return True
    else:
        return False

# Verificar a instalação do Visual Studio Code
def check_vscode():
    command = "code --user-data-dir /tmp --version"
    result = run_command(command)
    if "x64" in result:
        return True
    else:
        return False

def check_docker():
    command = "docker --version"  # Altere conforme o comando que você quer testar
    result = run_command(command)
    if "Docker" in result:
        return True
    else:
        return False
def check_hello():
    command = "docker image ls"  # Altere conforme o comando que você quer testar
    result = run_command(command)
    if "hello-world" in result:
        return True
    else:
        return False

def check_compose():
    command = "docker-compose --version"  # Altere conforme o comando que você quer testar
    result = run_command(command)
    if "Compose" in result:
        return True
    else:
        return False

# Verificar se o phpMyAdmin está acessível
def check_shine():
    command = "curl -sL http://localhost/dev/shinemodas | grep SHINE"
    result = run_command(command)
    if "SHINE" in result:
        return True
    else:
        return False


# Verificar se o phpMyAdmin está acessível
def check_www():
    command = "ls -ld /var/www | grep www-data"
    result = run_command(command)
    if "www-data" in result:
        return True
    else:
        return False


# Verificar se o phpMyAdmin está acessível
def check_dev():
    command = "ls -ld /var/www/html/dev | grep developer"
    result = run_command(command)
    if "developer" in result:
        return True
    else:
        return False

# Verificar se o phpMyAdmin está acessível
def check_link():
    command = "ls -l /home/developer | grep projetos"
    result = run_command(command)
    if "projetos" in result:
        return True
    else:
        return False


def main():
    score = 0
    username = "developer"
     
    student = input("Por favor, informe seu nome: ")

    print(f"\nBem-vindo, {student}!")
    print(f"\nPONTUAÇÂO INICIAL: {score} PONTO\n")

    print(f"{student}, CHECANDO SUAS CONFIGURACOES E SOMANDO PONTOS\n")
    if check_apache():
        print("SERVICO WEB..........OK")
        score += 100
    else:
        print("SERVICO WEB..........NO")

    if check_php():
        print("PHP..................OK")
        score += 50
    else:
        print("PHP..................NO")

    if check_maria():
        print("MARIADB..............OK")
        score += 150
    else:
        print("MARIADB..............NO")

    if check_maria_user(username):
        print(f"USER:{username}.......YES")
        score += 200
    else:
        print(f"{username}.......NO")

    if check_docker():
        print("DOCKER...............OK")
        score += 100
    else:
        print("DOCKER...............NO")

    if check_hello():
        print("CONTAINER HELLO......OK")
        score += 200
    else:
        print("CONTAINER HELLO......NO")

    if check_compose():
        print("DOCKER COMPOSE.......OK")
        score += 200
    else:
        print("DOCKER COMPOSE.......NO")

    if check_vscode():
        print("IDE VSCODE...........OK")
        score += 200
    else:
        print("IDE VSCODE...........NO")

    if check_phpmyadmin():
        print("PHPMYADMIN...........OK")
        score += 200
    else:
        print("PHPMYADMIN...........NO")

    if check_shine():
        print("SHINEMODAS...........OK")
        score += 200
    else:
        print("SHINEMODAS...........NO")

    if check_www():
        print("WWW_DATA /VAR/WWW ...OK")
        score += 200
    else:
        print("WWW-DATA /VAR/WWW ...NO")

    if check_dev():
        print("DIRETORIO DEV .......OK")
        score += 100
    else:
        print("DIRETORIO DEV .......NO")

    if check_link():
        print("Link PROJETOS .......OK")
        score += 100
    else:
        print("Link PROJETOS .......NO")

    print("\nAguarde enquanto calculamos sua pontuação...\n")
    time.sleep(2)  # Pausa de 2 segundos para criar suspense

    print("SOMANDO ACERTOS...")
    time.sleep(3)  # Pausa de 1 segundo para manter o suspense

    print("PONTUAÇÃO FINAL: ", end="", flush=True)
    time.sleep(3)  # Pausa para suspense
    for digit in str(score):
        print(digit, end="", flush=True)
        time.sleep(0.5)  # Pausa de 0.3 segundos entre cada dígito

    print(f"\n\nMissão dada é missão cumprida!, \n\n{student}, PARABÉNS!!!")

if __name__ == "__main__":
    main()