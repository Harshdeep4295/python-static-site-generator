from pathlib import Path


class Site:
    def Site(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for paths in self.source.glob("*"):
            if paths.is_dir:
                self.create_dir(path=paths)
