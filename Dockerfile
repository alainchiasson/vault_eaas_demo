FROM centos

WORKDIR /WORKDIR

RUN yum install -y yum-utils 
RUN yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo

RUN yum -y install vault

RUN yum install -y libcap which unzip jq
RUN setcap cap_ipc_lock= /usr/bin/vault

# Copy shell scripts to setup.
COPY scripts/* /usr/local/sbin

RUN yum install -y python3 python3-pip
RUN  pip3 install pip --upgrade

COPY python/requirements.txt .

RUN pip install -r requirements.txt

COPY python/app.py /usr/local/bin

# Set command line to wait for login.
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

