# README
## Ansible setup
```
sudo pip install ansible
```
## Run application on AWS using Ansible
```
ansible-playbook -vvv -i hosts --extra-vars='ansible_user=ubuntu' task.yml
```