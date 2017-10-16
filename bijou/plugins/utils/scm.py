class RepoDesc:
    """Repository descriptor
    """
    def __init__(self):
        pass

class SCM:
    """Repository manager for plugins

    Plugins are loaded via scm (currently only supporting git) into a root
    directory via descriptor. This class is designed to abstract that
    functionality into the common actions.

    Args:
        root: Path to root directory for plugins
        git: Path to git binary
    """

    def __init__(self, root: str = 'plugins', git: str = 'git'):
        self.git = git

    def parse(self, desc: str) -> RepoDesc:
        pass
