import subprocess
import sys

def upgrade_packages():
    try:
        # Run pip list command to get a list of installed packages
        process = subprocess.Popen([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=freeze'], stdout=subprocess.PIPE)
        out, _ = process.communicate()

        # Decode the byte output and split it into lines
        packages = out.decode('utf-8').strip().split('\n')

        # Extract package names
        package_names = [pkg.split('==')[0] for pkg in packages]

        # Upgrade each package to the latest version
        for package in package_names:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', package])

        print("All packages upgraded successfully!")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    upgrade_packages()

