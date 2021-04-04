import jstyleson
import subprocess
import os


class Claunch:
    def __init__(self):
        self.path = ".vscode/launch.json"
        self._config = None

    @property
    def config(self):
        if self._config is None:
            with open(self.path) as fd:
                self._config = jstyleson.load(fd)
        return self._config

    def list(self):
        for config in self.config.get("configurations", []):
            if config['request'] == 'launch':
                yield config

    def get_config(self, name):
        for config in self.list():
            if config['name'] == name:
                return config
        raise LookupError(f"Failed to find {name}")

    def start(self, name):
        config = self.get_config(name)
        if config['type'] == 'python':
            env = os.environ.copy()
            env.update(config.get('env', {}))
            args = config.get('args', [])
            for idx, arg in enumerate(args):
                if arg.startswith('${env:'):
                    key = arg.split(":")[-1][:-1]
                    args[idx] = env.get(key, '')
            cmd = ["python3", "-m", config["module"]] + args
            print("Launching {}".format(" ".join(cmd)))
            subprocess.run(" ".join(cmd), env=env, shell=True)
        else:
            raise RuntimeError(f"Launch type {config['type']} is not supported")
