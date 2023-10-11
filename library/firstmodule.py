#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import os, platform

def my_module():

    fields = {
            "hostname": {"default": True, "type": "str"}
    }

    module = AnsibleModule( argument_spec=fields, supports_check_mode=True )
    
    kernel = platform.platform(aliased=True)
    original_hostname = platform.node()
    new_hostname = module.params['hostname']

    os.system(f'hostnamectl set-hostname {new_hostname}')
    os.system('systemctl restart systemd-hostnamed')

    result = dict( changed=True, kernel_version=kernel, original_hostname=original_hostname, updated_hostname=new_hostname )
    module.exit_json(**result)


if __name__ == '__main__':
    my_module()
