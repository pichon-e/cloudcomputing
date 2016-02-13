# !/usr/bin/env python
import boto

def deleteInstances(conn, instance):
	conn.terminate_instances(instance[id_instance])
