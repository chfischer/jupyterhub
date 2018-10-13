FROM jupyterhub/jupyterhub:latest
RUN /opt/conda/bin/conda install -c conda-forge --yes jupyter

COPY jupyter_config.py /srv/jupyterhub/jupyter_config.py
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyter_config.py"]
