c.JupyterHub.ip = '0.0.0.0'
c.Authenticator.whitelist = {'testli', 'hub1'}
c.LocalAuthenticator.create_system_users = True
c.JupyterHub.admin_access = True
c.Authenticator.admin_users = {'chfischer'}
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.Spawner.notebook_dir = '/notebooks'
