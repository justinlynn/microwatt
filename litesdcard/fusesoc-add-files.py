#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import os
import sys
import pathlib

class LiteSDCardGenerator(Generator):
    def run(self):
        board = self.config.get('board')

        # Collect a bunch of directory path
        script_dir = os.path.dirname(sys.argv[0])
        gen_dir = os.path.join(script_dir, "generated", board)

        print("Adding LiteSDCard for board... ", board)

        # Add files to fusesoc
        files = []
        f = os.path.join(gen_dir, "litesdcard_core.v")
        files.append({f : {'file_type' : 'verilogSource'}})

        self.add_files(files)

g = LiteSDCardGenerator()
g.run()
g.write()
