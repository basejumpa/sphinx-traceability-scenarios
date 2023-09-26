extensions = [
    'sphinx.ext.ifconfig',
    'mlx.traceability'
]

def setup(app):
    app.add_config_value('feature_a', 0, 'env')
