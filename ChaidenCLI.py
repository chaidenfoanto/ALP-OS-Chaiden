import os
import shutil

def ls():
    """Menampilkan daftar file dan folder di direktori saat ini."""
    items = os.listdir()
    for item in items:
        print(item)

def pwd():
    """Menampilkan direktori kerja saat ini."""
    print(os.getcwd())

def cd(path):
    """Mengubah direktori kerja."""
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Error: Direktori '{path}' tidak ditemukan.")
    except NotADirectoryError:
        print(f"Error: '{path}' bukan direktori.")

def mkdir(directory_name):
    """Membuat direktori baru."""
    try:
        os.mkdir(directory_name)
        print(f"Direktori '{directory_name}' berhasil dibuat.")
    except FileExistsError:
        print(f"Error: Direktori '{directory_name}' sudah ada.")

def rmdir(directory_name):
    """Menghapus direktori (jika kosong)."""
    try:
        os.rmdir(directory_name)
        print(f"Direktori '{directory_name}' berhasil dihapus.")
    except FileNotFoundError:
        print(f"Error: Direktori '{directory_name}' tidak ditemukan.")
    except OSError:
        print(f"Error: Direktori '{directory_name}' tidak kosong.")

def touch(file_name):
    """Membuat file kosong baru."""
    try:
        with open(file_name, 'x'):
            print(f"File '{file_name}' berhasil dibuat.")
    except FileExistsError:
        print(f"Error: File '{file_name}' sudah ada.")

def rm(file_name):
    """Menghapus file."""
    try:
        os.remove(file_name)
        print(f"File '{file_name}' berhasil dihapus.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' tidak ditemukan.")

def cp(source, destination):
    """Menyalin file dari satu lokasi ke lokasi lain."""
    try:
        shutil.copy(source, destination)
        print(f"File '{source}' berhasil disalin ke '{destination}'.")
    except FileNotFoundError:
        print(f"Error: File '{source}' tidak ditemukan.")

def mv(source, destination):
    """Memindahkan atau mengganti nama file/direktori."""
    try:
        shutil.move(source, destination)
        print(f"File atau direktori '{source}' berhasil dipindahkan ke '{destination}'.")
    except FileNotFoundError:
        print(f"Error: File atau direktori '{source}' tidak ditemukan.")

def help_command():
    """Menampilkan daftar perintah yang tersedia."""
    commands = {
        "ls": "Menampilkan daftar file dan folder di direktori saat ini.",
        "pwd": "Menampilkan direktori kerja saat ini.",
        "cd <path>": "Mengubah direktori kerja.",
        "mkdir <directory_name>": "Membuat direktori baru.",
        "rmdir <directory_name>": "Menghapus direktori (jika kosong).",
        "touch <file_name>": "Membuat file kosong baru.",
        "rm <file_name>": "Menghapus file.",
        "cp <source> <destination>": "Menyalin file.",
        "mv <source> <destination>": "Memindahkan atau mengganti nama file/direktori.",
        "clear": "Membersihkan layar terminal.",
        "exit": "Keluar dari CLI.",
        "find_large <size>": "Menampilkan file yang lebih besar dari ukuran tertentu.",
        "tree": "Menampilkan struktur direktori dalam bentuk pohon.",
        "joke": "Menampilkan lelucon acak."
    }
    for cmd, desc in commands.items():
        print(f"{cmd}: {desc}")

def clear():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_cli():
    """Keluar dari CLI."""
    print("Keluar dari CLI. Sampai jumpa!")
    exit()

def find_large(size):
    """Menampilkan file yang lebih besar dari ukuran tertentu."""
    try:
        size = int(size)
        for item in os.listdir():
            if os.path.isfile(item) and os.path.getsize(item) > size:
                print(item)
    except ValueError:
        print("Error: Ukuran harus berupa angka.")

def tree(path="."):
    """Menampilkan struktur direktori dalam bentuk pohon."""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

def joke():
    """Menampilkan lelucon acak."""
    jokes = [
        "Kenapa programmer tidak pernah mandi? Karena mereka takut bug.",
        "Debugging adalah satu-satunya olahraga yang melibatkan komputer.",
        "Kenapa komputer kedinginan? Karena ada banyak cache!"
    ]
    import random
    print(random.choice(jokes))

def main():
    print("Simple CLI berbasis Python. Ketik 'help' untuk melihat daftar perintah.")
    while True:
        command = input("> ").strip().split()
        if not command:
            continue
        cmd = command[0]
        args = command[1:]
        if cmd == "ls":
            ls()
        elif cmd == "pwd":
            pwd()
        elif cmd == "cd" and args:
            cd(args[0])
        elif cmd == "mkdir" and args:
            mkdir(args[0])
        elif cmd == "rmdir" and args:
            rmdir(args[0])
        elif cmd == "touch" and args:
            touch(args[0])
        elif cmd == "rm" and args:
            rm(args[0])
        elif cmd == "cp" and len(args) == 2:
            cp(args[0], args[1])
        elif cmd == "mv" and len(args) == 2:
            mv(args[0], args[1])
        elif cmd == "help":
            help_command()
        elif cmd == "clear":
            clear()
        elif cmd == "exit":
            exit_cli()
        elif cmd == "find_large" and args:
            find_large(args[0])
        elif cmd == "tree":
            tree()
        elif cmd == "joke":
            joke()
        else:
            print(f"Perintah '{cmd}' tidak dikenali. Ketik 'help' untuk melihat daftar perintah.")

if __name__ == "__main__":
    main()
