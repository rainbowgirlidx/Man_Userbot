from userbot import RANDOM_STUFF_API_KEY
from subprocess import PIPE, Popen


def install_pip(pipfile):
    print(f"installing {pipfile}")
    pip_cmd = ["pip", "install", f"{pipfile}"]
    process = Popen(pip_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout


try:
    import randomstuff
except ModuleNotFoundError:
    install_pip("randomstuff.py")
    import randomstuff


rs_client = randomstuff.AsyncClient(api_key=RANDOM_STUFF_API_KEY, version="5")
