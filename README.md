# Trabajo de Fin de Máster: Análisis de malware obtenido en redes de señuelos

## Descripción

Este repositorio contiene las políticas de Tetragon y programas eBPF desarrollados y utilizados durante la realización del Trabajo de Fin de Máster titulado **"Análisis de malware obtenido en redes de señuelos"**. El objetivo principal de este trabajo es montar un sistema de detección y monitorización de intrusos.

## Contenido del Repositorio

El repositorio está organizado de la siguiente manera:

- **files-and-dirs-monitoring.yaml**: Contiene la política de Tetragon para monitorizar la escritura y lectura de ficheros y directorios.
- **logseBPF.txt**: Contiene los logs obtenidos con el programa eBPF **syscall-monitoring.py**.
- **logsTetragon.json**: Contiene los logs obtenidos con las políticas de Tetragon.
- **network-monitoring.yaml**: Contiene la política de Tetragon para monitorizar los accesos a redes externas al cluster.
- **syscall-monitoring.py**: Contiene el código eBPF para monitorizar la llamada al sistema execve.
