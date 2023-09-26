extensions = [
    'sphinx_selective_exclude.eager_only',
    'mlx.traceability'
]

def setup(app):
    app.add_config_value('tags_file', '', 'env')
    app.connect("config-inited", config_inited)

def config_inited(app, config):
    import os
    import sys

    if config.tags_file:
        with open(config.tags_file) as f:
            for line in f.readlines():
                line = line.strip()
                if line != "":
                    app.tags.add(line)