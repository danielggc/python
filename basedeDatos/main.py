from cassandra.cluster import Cluster
cluster=Cluster(['192.168.1.101','192.168.1.102'])
sesion=cluster.connect()
sesion.execute("INSERT INTO USERS (bar) VALUES (%s)", ("dgc7"))
