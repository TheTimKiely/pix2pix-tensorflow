import subprocess


def main():
    print('Installing image package')
    code = ['octave', '--eval', 'pkg install -forge image']
    code = [r'c:\Octave\Octave-5.1.0.0\mingw64\bin\octave-cli.exe', '--eval', "pkg install -forge image"]
    try:
        subprocess.check_output(code, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("failed to load octave image package")
        print("returncode:", e.returncode)
        print("output:", e.output)



if __name__ == '__main__':
    main()