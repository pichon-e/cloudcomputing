import boto

def deleteInstances(instances):
	stop_instances(instances, force=true) 
	terminate_instances(instances)
