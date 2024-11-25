#!/usr/bin/python3

import subprocess

# Executa o comando do terminal
def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar o comando: {e.output}"

# Função para verificar se um serviço está ativo
def check_service(service_name):
    command = f"systemctl is-active {service_name}"
    result = run_command(command)
    if result == "active":
        return f"{service_name}  ...RODANDO."
    else:
        return f"{service_name} ...PARADO."

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


def main():
    score = 0
    username = "developer"

    # Verificar serviços
    print("\nVERIFICANDO SERVIÇOS EM EXECUÇÃO...\n")
    
    # Verificar o status do Apache
    print(check_service("apache2"))
    
    # Verificar o status do MariaDB
    print(check_service("mariadb"))
    
    # Verificar o status do Docker
    print(check_service("docker"))
    

    print(f"\nPontuação inicial: {score} pontos\n")
    print("VERIFICANDO AS CONFIGURACOES E SOMANDO PONTOS\n")
    if check_apache():
        print("SERVICO WEB.......OK")
        score += 100
    else:
        print("SERVICO WEB.......NO")

    if check_php():
        print("PHP...............OK")
        score += 50
    else:
        print("PHP...............NO")

    if check_maria():
        print("MARIADB...........OK")
        score += 150
    else:
        print("MARIADB...........NO")

    if check_maria_user(username):
        print(f"USER:{username}....YES")
        score += 200
    else:
        print(f"{username}....NO")

    if check_docker():
        print("Docker............OK")
        score += 200
    else:
        print("Docker............NO")

    if check_compose():
        print("Compose...........OK")
        score += 200
    else:
        print("Compose...........NO")

    if check_vscode():
        print("VSCODE............OK")
        score += 200
    else:
        print("VSCODE............NO")

    if check_phpmyadmin():
        print("PHPMYADMIN........OK")
        score += 200
    else:
        print("PHPMYADMIN........NO")

    if check_shine():
        print("SHINEMODAS........OK")
        score += 300
    else:
        print("SHINEMODAS........NO")

    if check_www():
        print("/var/www .........OK")
        score += 200
    else:
        print("/var/www .........NO")

    if check_dev():
        print("Diretorio DEV ....OK")
        score += 200
    else:
        print("Diretorio DEV ....NO")

    print(f"\nPONTUAÇÃO COMPUTADA: {score} pontos")

if __name__ == "__main__":
    main()

