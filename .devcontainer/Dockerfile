# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.148.1/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Option] Install Node.js
ARG INSTALL_NODE="true"
ARG NODE_VERSION="lts/*"
RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "source /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# RUN pip3 --disable-pip-version-check --no-cache-dir install ipykernel

RUN pip3 --disable-pip-version-check --no-cache-dir install \
altair==4.1.0 \
attrs==20.3.0 \
backcall==0.2.0 \
cycler==0.10.0 \
decorator==4.4.2 \
entrypoints==0.3 \
ipykernel==5.3.4 \
ipython==7.19.0 \
ipython-genutils==0.2.0 \
jedi==0.17.2 \
Jinja2==2.11.2 \
joblib==0.17.0 \
jsonschema==3.2.0 \
jupyter-client==6.1.7 \
jupyter-core==4.7.0 \
kiwisolver==1.3.1 \
MarkupSafe==1.1.1 \
matplotlib==3.3.3 \
numpy==1.19.4 \
pandas==1.1.4 \
parso==0.7.1 \
pexpect==4.8.0 \
pickleshare==0.7.5 \
Pillow==8.0.1 \
prompt-toolkit==3.0.8 \
ptyprocess==0.6.0 \
Pygments==2.7.2 \
pyparsing==2.4.7 \
pyrsistent==0.17.3 \
python-dateutil==2.8.1 \
pytz==2020.4 \
pyzmq==20.0.0 \
scikit-learn==0.23.2 \
scipy==1.5.4 \
six==1.15.0 \
SQLAlchemy==1.3.20 \
tenacity==6.2.0 \
threadpoolctl==2.1.0 \
toolz==0.11.1 \
tornado==6.1 \
traitlets==5.0.5 \
wcwidth==0.2.5 

    
# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1
