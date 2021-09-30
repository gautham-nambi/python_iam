# README
## Ansible setup
```
sudo pip install ansible
```
## Run application on AWS using Ansible
```
ansible-playbook -vvv -i hosts --extra-vars='ansible_user=ubuntu' task.yml
```
## API
```
GET /list-users/                          Lists all IAM users
GET /users/<username>/access-key-details/ Lists all access keys and details
GET /users/<username>/tags/               Lists all tags for the user
```
