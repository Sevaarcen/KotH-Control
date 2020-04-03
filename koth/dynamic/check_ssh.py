import paramiko

from koth.checks import ServiceChecker

# TODO make this


class SSHChecker(ServiceChecker):
    def __init__(self):
        pass

    def _run(self, host: str, team_identifiers: dict, args: dict):
        port = args.get('port', 22)


