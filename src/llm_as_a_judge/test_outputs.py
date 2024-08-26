TEST_OUTPUTS = {
    "example1": """
    1. **System-Assigned Managed Identity**:
    1. **Compromise of the Virtual Machine (VM):**
       - **SSH Brute Force Attack:** Since the Network Security Group (NSG) allows inbound SSH traffic from any source, an attacker could attempt to brute force the SSH credentials of the VM.
       - **Exploitation of Vulnerabilities:** If the VM's operating system or any installed software has vulnerabilities, an attacker could exploit these to gain access.
    """,
    
    "example2": """
    1. Initial Access:
       - The attacker exploits a vulnerability in the web application running on VM1.
       - This allows them to execute arbitrary code on the server.
    
    2. Privilege Escalation:
       - Using the initial foothold, the attacker discovers the VM's system-assigned managed identity.
       - They leverage this identity to access Azure resources with elevated privileges.
    
    3. Data Exfiltration:
       - The attacker uses the managed identity's permissions to access a storage account.
       - They download sensitive data from the storage account to their local machine.
    
    4. Lateral Movement:
       - The attacker scans the internal network from VM1.
       - They discover other VMs in the same virtual network and attempt to compromise them.
    """
}