FROM ubuntu:18.04
USER root

RUN apt-get update
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
RUN apt-get install -y python3 gcc
