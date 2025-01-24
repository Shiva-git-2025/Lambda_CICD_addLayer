import json
import boto3
import dns.resolver
import logging

elb_client = boto3.client('elbv2', region_name='eu-central-1')
ec2_client = boto3.client('ec2', region_name='eu-central-1')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")

    alb_dns_name = "www.google.com"
    
    logger.info(f"Resolving ALB DNS: {alb_dns_name}")

    try:
        ip_addresses = resolve_alb_dns(alb_dns_name)
        logger.info(f"Resolved IP addresses for ALB: {ip_addresses}")

        logger.info(f"Successfully updated NLB target group with IPs: {ip_addresses}")

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        raise e

def resolve_alb_dns(dns_name):
    try:
        result = dns.resolver.resolve(dns_name, 'A')
        ip_addresses = [ip.address for ip in result]
        return ip_addresses
    except Exception as e:
        logger.error(f"Error resolving ALB DNS {dns_name}: {str(e)}")
        raise Exception(f"Failed to resolve ALB DNS {dns_name}") 


















