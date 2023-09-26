extensions = [
    'sphinx.ext.ifconfig',
]

def setup(app):
    app.add_config_value('config_file', '', 'env')
    app.add_config_value('config', {}, 'env')
    app.connect("config-inited", config_inited)

# print(f"config_file={config_file}")

def config_inited(app, config):
    
    if config.config_file:
        with open(config.config_file) as f:
            from json import load as json_load
            app.config.__dict__["config"] = json_load(f)
