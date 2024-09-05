import subprocess

# Fungsi untuk menjalankan ZAP Proxy dengan command sesuai domain
def run_zap_proxy(domain):
    command = [
        'zaproxy', 
        '-cmd', 
        '-quickurl', f'https://{domain}', 
        '-quickout', f'/home/idhenz/VA/{domain}.html', 
        '-quickprogress'
    ]
    
    try:
        print(f"Scanning domain: {domain}")
        # Menjalankan command ZAP Proxy
        subprocess.run(command, check=True)
        print(f"Finished scanning: {domain}")
    except subprocess.CalledProcessError as e:
        print(f"Error scanning domain {domain}: {e}")

# Membaca domain dari file teks
def scan_domains_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()
            # Memproses setiap domain di file
            for domain in domains:
                domain = domain.strip()  # Menghapus spasi atau newline
                if domain:
                    run_zap_proxy(domain)
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")

# Path ke file txt yang berisi daftar domain
file_path = 'list_domain.txt'

# Menjalankan scan untuk domain dalam file
scan_domains_from_file(file_path)