

class ServiceChecker:
    """class for dynamic service checkers to conform to"""
    def __init__(self):
        '''Empty init method, to be overridden by modules'''
        pass

    def run(self, host: str, team_identifiers:dict, args: dict) -> None:
        """ wrapper method to perform checks and error handling and handle results of check"""
        # TODO implement this
        self._run(host, team_identifiers, args)

    def _run(self, host: str, team_identifiers: dict, args: dict) -> dict:
        """ blank method to be overwritten by dynamic checker modules """