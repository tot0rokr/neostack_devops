FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli

RUN apt-get install -y curl wget tar bzip2
# curl -sSL https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.10/gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2 | tar -xj 
RUN wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.10/gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2
RUN tar -xvf gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2
ENV PATH=/gcc-arm-none-eabi-10.3-2021.10/bin:$PATH
RUN wget https://www.nordicsemi.com/-/media/Software-and-other-downloads/Desktop-software/nRF-command-line-tools/sw/Versions-10-x-x/10-15-3/nrf-command-line-tools_10.15.3_amd64.deb
# RUN dpkg -i nrf-command-line-tools_10.15.3_amd64.deb
# RUN apt-get install -f
RUN apt install -y ./nrf-command-line-tools_10.15.3_amd64.deb


RUN apt-get install -y make cmake build-essential
# RUN cmake -DTOOLCHAIN=gccarmemb -DPLATFORM=nrf52840_xxAA -DBOARD=pca10056 -DSOFTDEVICE=s140_7.2.0 -DBUILD_EXAMPLES=no ../$Mesh_SDK
# RUN make merge_light_ctl_server_nrf52840_xxAA_s140_7.2.0

USER jenkins
ENV BLE_SDK nRF5_SDK_17.0.2_d674dde
ENV Mesh_SDK nrf5_SDK_for_Mesh_v5.0.0_src
RUN jenkins-plugin-cli --plugins "blueocean:1.25.2 docker-workflow:1.28"
