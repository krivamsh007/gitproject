FROM openjdk:8-jdk-slim

# Set the Apache Atlas version and home directory
ENV ATLAS_VERSION=2.1.0
ENV ATLAS_HOME=/opt/atlas
ENV JAVA_HOME=/usr/local/openjdk-8

WORKDIR /opt

# Install required packages and download/extract Apache Atlas from GitHub
RUN apt-get update && apt-get install -y curl tar git maven && rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/apache/atlas.git && \
    cd atlas && \
    git checkout tags/release-2.1.0-rc3 && \
    export MAVEN_OPTS="-Xms2g -Xmx2g" && \
    # Create a symbolic link for tools.jar to fix the dependency issue
    ln -sf ${JAVA_HOME}/lib/tools.jar /usr/lib/jvm/tools.jar && \
    # Skip the Sqoop bridge component to avoid dependency issues
    mvn clean package -DskipTests -Pdist -pl -:sqoop-bridge-shim && \
    tar -xzf distro/target/apache-atlas-${ATLAS_VERSION}-server.tar.gz -C /opt && \
    mv /opt/apache-atlas-${ATLAS_VERSION} /opt/atlas && \
    rm -rf /opt/atlas/.git && \
    rm -rf /root/.m2 && \
    apt-get purge -y git maven && \
    apt-get autoremove -y

# Expose the Atlas UI port
EXPOSE 21000

# Start Atlas in the foreground
CMD ["/opt/atlas/bin/atlas_start.py", "-fg"]
